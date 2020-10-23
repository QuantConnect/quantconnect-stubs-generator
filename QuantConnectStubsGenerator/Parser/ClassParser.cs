using System.Collections.Generic;
using System.Linq;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Parser
{
    public class ClassParser : BaseParser
    {
        public ClassParser(ParseContext context, SemanticModel model) : base(context, model)
        {
        }

        protected override void EnterClass(BaseTypeDeclarationSyntax node)
        {
            var cls = ParseClass(node);

            if (_currentNamespace.HasClass(cls.Type))
            {
                var existingClass = _currentNamespace.GetClassByType(cls.Type);

                // Some classes in C# exist multiple times with varying amounts of generics
                // We keep the one with the most generics
                if (existingClass.Type.TypeParameters.Count >= cls.Type.TypeParameters.Count)
                {
                    // Add documentation if the existing class has been registered without it and it is available here
                    existingClass.Summary ??= cls.Summary;

                    _currentClass = existingClass;
                    return;
                }
            }

            if (_currentClass != null)
            {
                cls.ParentClass = _currentClass;
                _currentClass.InnerClasses.Add(cls);
            }

            _currentNamespace.RegisterClass(cls);
            _currentClass = cls;
        }

        private Class ParseClass(BaseTypeDeclarationSyntax node)
        {
            return new Class(_typeConverter.GetType(node, true))
            {
                Static = HasModifier(node, "static"),
                Summary = ParseSummary(node),
                Interface = node is InterfaceDeclarationSyntax,
                InheritsFrom = ParseInheritedTypes(node).ToList(),
                MetaClass = ParseMetaClass(node)
            };
        }

        private string ParseSummary(BaseTypeDeclarationSyntax node)
        {
            string summary = null;

            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                summary = doc["summary"].GetText();
            }

            if (HasModifier(node, "protected"))
            {
                summary = AppendSummary(summary, "This class is protected.");
            }

            return summary;
        }

        private IEnumerable<PythonType> ParseInheritedTypes(BaseTypeDeclarationSyntax node)
        {
            var types = new List<PythonType>();

            var symbol = _model.GetDeclaredSymbol(node);
            if (symbol == null)
            {
                return types;
            }

            var currentType = _typeConverter.GetType(node, true);

            if (symbol.BaseType != null)
            {
                var ns = symbol.BaseType.ContainingNamespace.Name;
                var name = symbol.BaseType.Name;

                if (!ShouldSkipBaseType(currentType, ns, name))
                {
                    types.Add(_typeConverter.GetType(symbol.BaseType));
                }
            }

            foreach (var typeSymbol in symbol.Interfaces)
            {
                var type = _typeConverter.GetType(typeSymbol);

                // In C# a class can be extended multiple times with different amounts of generics
                // In Python this is not possible, so we keep the type with the most generics
                var existingType = types.FirstOrDefault(t => t.Namespace == type.Namespace && t.Name == type.Name);
                if (existingType != null)
                {
                    if (existingType.TypeParameters.Count < type.TypeParameters.Count)
                    {
                        existingType.TypeParameters = type.TypeParameters;
                    }

                    continue;
                }

                // "Cannot create consistent method ordering" errors appear when a Python class
                // extends from both System.Collections.ISomething and System.Collections.Generic.ISomething[T]
                // We keep the latter as it contains more type information
                if (type.Namespace == "System.Collections.Generic"
                    && type.Name.StartsWith("I")
                    && type.TypeParameters.Count > 0)
                {
                    var existing = types
                        .FirstOrDefault(t => t.Namespace == "System.Collections" && t.Name == type.Name);

                    if (existing != null)
                    {
                        types.Remove(existing);
                    }
                }

                // "Cannot create consistent method ordering" errors appear when a Python class
                // extends from multiple classes in the System.Collections.Generic namespace
                if (type.Namespace == "System.Collections.Generic" &&
                    types.Any(t => t.Namespace == "System.Collections.Generic"))
                {
                    continue;
                }

                types.Add(type);
            }

            // Ensure classes don't extend from both typing.List and typing.Dict, that causes conflicting definitions
            var listType = types.FirstOrDefault(type => type.ToPythonString().StartsWith("typing.List["));
            var dictType = types.FirstOrDefault(type => type.ToPythonString().StartsWith("typing.Dict["));

            if (listType != null && dictType != null)
            {
                types.Remove(listType);
            }

            types = types.Select(type => ValidateInheritedType(currentType, type)).ToList();

            return types;
        }

        private PythonType ParseMetaClass(BaseTypeDeclarationSyntax node)
        {
            if (node is InterfaceDeclarationSyntax || HasModifier(node, "abstract"))
            {
                return new PythonType("ABCMeta", "abc");
            }

            return null;
        }

        private PythonType ValidateInheritedType(PythonType currentType, PythonType inheritedType)
        {
            if (inheritedType.IsNamedTypeParameter)
            {
                return inheritedType;
            }

            // Python classes can't reference themselves or any of their parent classes in their inherited types
            if (currentType.GetBaseName() == inheritedType.GetBaseName()
                && currentType.Namespace == inheritedType.Namespace)
            {
                return ToAnyAlias(inheritedType);
            }

            inheritedType.TypeParameters = inheritedType.TypeParameters
                .Select(type => ValidateInheritedType(currentType, type))
                .ToList();

            return inheritedType;
        }

        private PythonType ToAnyAlias(PythonType type)
        {
            var alias = type.Name.Replace('.', '_');
            if (type.Namespace != null)
            {
                alias = $"{type.Namespace.Replace('.', '_')}_{alias}";
            }

            return new PythonType("Any", "typing")
            {
                Alias = alias
            };
        }

        private bool ShouldSkipBaseType(PythonType currentType, string ns, string name)
        {
            // System.Object extends from System.Object in the AST, we skip this base type in Python
            if (currentType.Namespace == "System" && currentType.Name == "Object" && ns == "System" && name == "Object")
            {
                return true;
            }

            // We don't parse a ValueType, so we can't extend from it without errors
            return ns == "System" && name == "ValueType";
        }
    }
}

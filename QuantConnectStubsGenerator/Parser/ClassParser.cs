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
            var type = _typeConverter.GetType(node);

            // Prevent multiple registrations of partial classes
            if (_currentNamespace.HasClass(type))
            {
                _currentClass = _currentNamespace.GetClassByType(type);
                return;
            }

            var cls = ParseClass(node);

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
            return new Class(_typeConverter.GetType(node))
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

            if (symbol.BaseType != null)
            {
                var ns = symbol.BaseType.ContainingNamespace.Name;
                var name = symbol.BaseType.Name;

                // Don't make classes extend from System.Object, System.Enum or System.ValueType to reduce noise
                var isObject = ns == "System" && name == "Object";
                var isEnum = ns == "System" && name == "Enum";
                var isValueType = ns == "System" && name == "ValueType";

                if (!isObject && !isEnum && !isValueType)
                {
                    types.Add(_typeConverter.GetType(symbol.BaseType));
                }
            }

            var currentType = _typeConverter.GetType(node);

            // C# classes can extend the same interface twice with different generics, Python classes can't
            var usedInterfaces = new HashSet<INamedTypeSymbol>();
            foreach (var typeSymbol in symbol.Interfaces)
            {
                if (usedInterfaces.Add(typeSymbol.ConstructedFrom))
                {
                    types.Add(_typeConverter.GetType(typeSymbol));
                }
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
            return new PythonType("Any", "typing")
            {
                Alias = $"{type.Namespace.Replace('.', '_')}_{type.Name.Replace('.', '_')}"
            };
        }
    }
}

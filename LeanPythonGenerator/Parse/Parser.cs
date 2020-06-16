using System.Linq;
using LeanPythonGenerator.Model;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

namespace LeanPythonGenerator.Parse
{
    /// <summary>
    /// The parser which is responsible for parsing all relevant information in all C# files to the ParseContext.
    /// </summary>
    public partial class Parser : CSharpSyntaxWalker
    {
        private readonly ParseContext _context;
        private readonly SemanticModel _model;

        private Namespace _currentNamespace;
        private Class _currentClass;

        public Parser(ParseContext context, SemanticModel model)
        {
            _context = context;
            _model = model;
        }

        public override void VisitNamespaceDeclaration(NamespaceDeclarationSyntax node)
        {
            _currentNamespace = _context.GetNamespaceByName(node.Name.ToString());

            base.VisitNamespaceDeclaration(node);

            _currentNamespace = null;
        }

        public override void VisitClassDeclaration(ClassDeclarationSyntax node)
        {
            if (!EnterClass(node))
            {
                return;
            }

            base.VisitClassDeclaration(node);

            ExitClass();
        }

        public override void VisitStructDeclaration(StructDeclarationSyntax node)
        {
            if (!EnterClass(node))
            {
                return;
            }

            base.VisitStructDeclaration(node);

            ExitClass();
        }

        public override void VisitEnumDeclaration(EnumDeclarationSyntax node)
        {
            if (!EnterClass(node))
            {
                return;
            }

            var enumType = new PythonType("Enum", "enum");
            _currentClass.InheritsFrom.Add(enumType);
            _currentNamespace.UsedTypes.Add(enumType);

            base.VisitEnumDeclaration(node);

            ExitClass();
        }

        public override void VisitInterfaceDeclaration(InterfaceDeclarationSyntax node)
        {
            if (!EnterClass(node))
            {
                return;
            }

            base.VisitInterfaceDeclaration(node);

            ExitClass();
        }

        public override void VisitPropertyDeclaration(PropertyDeclarationSyntax node)
        {
            if (node.Modifiers.Any(modifier => modifier.Text == "private"))
            {
                return;
            }

            var writeable = node.AccessorList?.Accessors.Any(accessor =>
            {
                return accessor.Keyword.Text == "set"
                       && accessor.Modifiers.All(modifier => modifier.Text != "private");
            }) ?? false;

            var property = new Property(node.Identifier.Text)
            {
                Type = GetType(node.Type),
                ReadOnly = !writeable
            };

            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                property.Summary = doc["summary"].GetText();
            }

            if (node.Modifiers.Any(modifier => modifier.Text == "protected"))
            {
                property.Summary = PrefixSummary(property.Summary, "This property is protected.");
            }

            _currentClass.Properties.Add(property);
        }

        public override void VisitEnumMemberDeclaration(EnumMemberDeclarationSyntax node)
        {
            var property = new Property(node.Identifier.Text)
            {
                Value = node.EqualsValue != null
                    ? node.EqualsValue.Value.ToString()
                    : _currentClass.Properties.Count.ToString()
            };


            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                property.Summary = doc["summary"].GetText();
            }

            _currentClass.Properties.Add(property);
        }

        private bool EnterClass(BaseTypeDeclarationSyntax node)
        {
            if (node.Modifiers.Any(modifier => modifier.Text == "private"))
            {
                return false;
            }

            var cls = _currentClass == null
                ? _currentNamespace.GetClassByType(GetType(node))
                : new Class(GetType(node));

            if (_currentClass == null)
            {
                _currentClass = cls;
            }
            else
            {
                cls.ParentClass = _currentClass;
                _currentClass.InnerClasses.Add(cls);
                _currentClass = cls;
            }

            CheckForInheritedTypes(node);
            CheckForClassSummary(node);

            return true;
        }

        private void ExitClass()
        {
            _currentClass = _currentClass.ParentClass;
        }

        private void CheckForInheritedTypes(BaseTypeDeclarationSyntax node)
        {
            var symbol = _model.GetDeclaredSymbol(node);

            if (symbol == null)
            {
                return;
            }

            if (symbol.BaseType != null)
            {
                var ns = symbol.BaseType.ContainingNamespace.Name;
                var name = symbol.BaseType.Name;

                // Don't make every object extend from System.Object and every enum from System.Enum
                var isObject = ns == "System" && name == "Object";
                var isEnum = ns == "System" && name == "Enum";

                if (!isObject && !isEnum)
                {
                    _currentClass.InheritsFrom.Add(GetType(symbol.BaseType));
                }
            }

            foreach (var typeSymbol in symbol.Interfaces)
            {
                _currentClass.InheritsFrom.Add(GetType(typeSymbol));
            }
        }

        private void CheckForClassSummary(BaseTypeDeclarationSyntax node)
        {
            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                _currentClass.Summary = doc["summary"].GetText();
            }

            if (node.Modifiers.Any(modifier => modifier.Text == "protected"))
            {
                _currentClass.Summary = PrefixSummary(_currentClass.Summary, "This class is protected.");
            }
        }

        private string PrefixSummary(string currentSummary, string prefix)
        {
            if (currentSummary != null)
            {
                return currentSummary.Contains(prefix)
                    ? currentSummary
                    : prefix + "\n\n" + currentSummary;
            }

            return prefix;
        }
    }
}

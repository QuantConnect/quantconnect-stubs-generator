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
            if (node.Modifiers.Any(modifier => modifier.Text == "private"))
            {
                return;
            }

            var cls = _currentClass == null
                ? _currentNamespace.GetClassByType(ParseType(node))
                : new Class(ParseType(node));

            EnterClass(cls);

            CheckForClassSummary(node);
            CheckForInheritedTypes(node);

            base.VisitClassDeclaration(node);
            ExitClass();
        }

        public override void VisitStructDeclaration(StructDeclarationSyntax node)
        {
            if (node.Modifiers.Any(modifier => modifier.Text == "private"))
            {
                return;
            }

            EnterClass(new Class(ParseType(node)));

            CheckForClassSummary(node);
            CheckForInheritedTypes(node);

            base.VisitStructDeclaration(node);
            ExitClass();
        }

        public override void VisitEnumDeclaration(EnumDeclarationSyntax node)
        {
            if (node.Modifiers.Any(modifier => modifier.Text == "private"))
            {
                return;
            }

            var cls = new Class(ParseType(node));
            var enumType = new PythonType("Enum", "enum");
            cls.InheritsFrom.Add(enumType);

            EnterClass(cls);

            _currentNamespace.UsedTypes.Add(enumType);
            CheckForClassSummary(node);

            base.VisitEnumDeclaration(node);
            ExitClass();
        }

        public override void VisitInterfaceDeclaration(InterfaceDeclarationSyntax node)
        {
            if (node.Modifiers.Any(modifier => modifier.Text == "private"))
            {
                return;
            }

            var cls = _currentClass == null
                ? _currentNamespace.GetClassByType(ParseType(node))
                : new Class(ParseType(node));

            EnterClass(cls);

            CheckForClassSummary(node);
            CheckForInheritedTypes(node);

            base.VisitInterfaceDeclaration(node);
            ExitClass();
        }

        private void CheckForClassSummary(SyntaxNode node)
        {
            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                _currentClass.Summary = doc["summary"].GetText();
            }
        }

        private void CheckForInheritedTypes(BaseTypeDeclarationSyntax node)
        {
            var symbol = _model.GetDeclaredSymbol(node);

            if (symbol == null)
            {
                return;
            }

            foreach (var typeSymbol in symbol.Interfaces)
            {
                _currentClass.InheritsFrom.Add(ParseType(typeSymbol));
            }
        }

        private void EnterClass(Class cls)
        {
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
        }

        private void ExitClass()
        {
            _currentClass = _currentClass.ParentClass;
        }
    }
}

using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Parser
{
    // ReSharper disable once ClassNeverInstantiated.Global
    public class MethodParser : BaseParser
    {
        public MethodParser(ParseContext context, SemanticModel model) : base(context, model)
        {
        }

        public override void VisitMethodDeclaration(MethodDeclarationSyntax node)
        {
            // TODO: Implement

            base.VisitMethodDeclaration(node);
        }

        public override void VisitConstructorDeclaration(ConstructorDeclarationSyntax node)
        {
            // TODO: Implement

            base.VisitConstructorDeclaration(node);
        }

        public override void VisitDelegateDeclaration(DelegateDeclarationSyntax node)
        {
            // TODO: Implement

            base.VisitDelegateDeclaration(node);
        }
    }
}

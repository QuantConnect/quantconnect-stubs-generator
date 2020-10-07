using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using QuantConnectStubsGenerator.Model;

namespace QuantConnectStubsGenerator.Parser
{
    // ReSharper disable once ClassNeverInstantiated.Global
    public class PropertyParser : BaseParser
    {
        public PropertyParser(ParseContext context, SemanticModel model) : base(context, model)
        {
        }

        public override void VisitPropertyDeclaration(PropertyDeclarationSyntax node)
        {
            // TODO: Implement

            base.VisitPropertyDeclaration(node);
        }

        public override void VisitFieldDeclaration(FieldDeclarationSyntax node)
        {
            // TODO: Implement

            base.VisitFieldDeclaration(node);
        }

        public override void VisitEnumMemberDeclaration(EnumMemberDeclarationSyntax node)
        {
            // TODO: Implement

            base.VisitEnumMemberDeclaration(node);
        }
    }
}

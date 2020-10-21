using System.Linq;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

namespace QuantConnectStubsGenerator.Parser
{
    public class PropertyParser : BaseParser
    {
        public PropertyParser(ParseContext context, SemanticModel model) : base(context, model)
        {
        }

        public override void VisitPropertyDeclaration(PropertyDeclarationSyntax node)
        {
            if (HasModifier(node, "private"))
            {
                return;
            }

            if (_currentClass.Properties.Any(p => p.Name == node.Identifier.Text))
            {
                return;
            }

            var property = new Property(node.Identifier.Text)
            {
                Type = _typeConverter.GetType(node.Type),
                ReadOnly = ((IPropertySymbol) _typeConverter.GetSymbol(node)).IsReadOnly,
                Static = _currentClass.Static || HasModifier(node, "static"),
                Abstract = _currentClass.Interface || HasModifier(node, "abstract")
            };

            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                property.Summary = doc["summary"].GetText();
            }

            if (HasModifier(node, "protected"))
            {
                property.Summary = AppendSummary(property.Summary, "This property is protected.");
            }

            _currentClass.Properties.Add(property);
        }

        public override void VisitFieldDeclaration(FieldDeclarationSyntax node)
        {
            if (HasModifier(node, "private"))
            {
                return;
            }

            foreach (var variable in node.Declaration.Variables)
            {
                var property = new Property(variable.Identifier.Text)
                {
                    Type = _typeConverter.GetType(node.Declaration.Type),
                    ReadOnly = HasModifier(node, "readonly") || HasModifier(node, "const"),
                    Static = _currentClass.Static || HasModifier(node, "static") || HasModifier(node, "const"),
                    Abstract = _currentClass.Interface || HasModifier(node, "abstract")
                };

                if (variable.Initializer != null)
                {
                    property.Value = FormatValue(variable.Initializer.Value.ToString());
                }

                var doc = ParseDocumentation(node);
                if (doc["summary"] != null)
                {
                    property.Summary = doc["summary"].GetText();
                }

                if (HasModifier(node, "protected"))
                {
                    property.Summary = AppendSummary(property.Summary, "This field is protected.");
                }

                _currentClass.Properties.Add(property);
            }
        }

        public override void VisitEnumMemberDeclaration(EnumMemberDeclarationSyntax node)
        {
            var property = new Property(node.Identifier.Text)
            {
                Value = node.EqualsValue != null
                    ? FormatValue(node.EqualsValue.Value.ToString())
                    : _currentClass.Properties.Count.ToString(),
                Static = true,
                Abstract = _currentClass.Interface || HasModifier(node, "abstract")
            };

            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                property.Summary = doc["summary"].GetText();
            }

            _currentClass.Properties.Add(property);
        }
    }
}

using System.Linq;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;

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
                Type = PrefixTypeIfNecessary(_typeConverter.GetType(node.Type)),
                ReadOnly = ((IPropertySymbol) _typeConverter.GetSymbol(node)).IsReadOnly,
                Static = _currentClass.Static || HasModifier(node, "static"),
                Abstract = _currentClass.Interface || HasModifier(node, "abstract")
            };

            // This is a dirty workaround for TradingEconomicsEarnings.Symbol
            // TradingEconomicsEarnings extends from BaseData, which has a Symbol property of type Symbol
            // Somehow the Symbol property on TradingEconomicsEarnings is of type string though, causing Mypy errors
            // TODO: Find a way to do this in a generic way without hardcoding TradingEconomicsEarnings.Symbol
            if (_currentClass.Type.Namespace == "QuantConnect.Data.Custom.TradingEconomics"
                && _currentClass.Type.Name == "TradingEconomicsEarnings"
                && property.Name == "Symbol")
            {
                property.Type = new PythonType("Symbol", "QuantConnect")
                {
                    Alias = "_QuantConnect_Symbol"
                };
            }

            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                property.Summary = doc["summary"].GetText();
            }

            if (HasModifier(node, "protected"))
            {
                property.Summary = PrefixSummary(property.Summary, "This property is protected.");
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
                    Type = PrefixTypeIfNecessary(_typeConverter.GetType(node.Declaration.Type)),
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
                    property.Summary = PrefixSummary(property.Summary, "This field is protected.");
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

        /// <summary>
        /// The QuantConnect and Oanda namespaces contain a lot of properties with the same name as a type.
        /// These types are aliased with an underscore prefix so that type hints still work.
        /// </summary>
        private PythonType PrefixTypeIfNecessary(PythonType type)
        {
            if (type.Namespace == null || type.Alias != null || type.IsNamedTypeParameter)
            {
                return type;
            }

            if (type.Namespace.StartsWith("QuantConnect") || type.Namespace.StartsWith("Oanda"))
            {
                var formattedNamespace = type.Namespace.Replace('.', '_');
                var formattedName = type.Name.Replace('.', '_');
                type.Alias = $"_{formattedNamespace}_{formattedName}";
            }

            type.TypeParameters = type.TypeParameters.Select(PrefixTypeIfNecessary).ToList();

            return type;
        }
    }
}

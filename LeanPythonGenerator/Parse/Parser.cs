using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.Xml;
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

        /// <summary>
        /// If _currentClass is A.B.C, _topClass is A.
        /// </summary>
        private Class _topClass;

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
            _topClass.UsedTypes.Add(enumType);

            base.VisitEnumDeclaration(node);

            ExitClass();
        }

        public override void VisitInterfaceDeclaration(InterfaceDeclarationSyntax node)
        {
            if (!EnterClass(node))
            {
                return;
            }

            _currentClass.Interface = true;

            base.VisitInterfaceDeclaration(node);

            ExitClass();
        }

        public override void VisitPropertyDeclaration(PropertyDeclarationSyntax node)
        {
            if (HasModifier(node, "private"))
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
                ReadOnly = !writeable,
                Static = _currentClass.Static || HasModifier(node, "static"),
                Abstract = _currentClass.Interface || HasModifier(node, "abstract")
            };

            if (property.Abstract)
            {
                _topClass.UsedTypes.Add(new PythonType("abstractmethod", "abc"));
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
                    Type = GetType(node.Declaration.Type),
                    ReadOnly = HasModifier(node, "readonly") || HasModifier(node, "const"),
                    Static = _currentClass.Static || HasModifier(node, "static"),
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

        public override void VisitMethodDeclaration(MethodDeclarationSyntax node)
        {
            if (HasModifier(node, "private"))
            {
                return;
            }

            // Skip extension methods like IEnumerable.GetEnumerator() in Slice
            if (GetType(node).ToString().Contains("System."))
            {
                return;
            }

            var classContainingMethod = _currentClass;
            var isExtensionMethod = false;

            if (node.ParameterList.Parameters.Count > 0)
            {
                var firstParameter = node.ParameterList.Parameters[0];
                if (firstParameter.Modifiers.Any(modifier => modifier.Text == "this"))
                {
                    var classType = GetType(firstParameter.Type);

                    // Skip extension methods on non-QC data types
                    if (classType.Namespace == null
                        || classType.Namespace == "typing"
                        || classType.Namespace == "<global namespace>"
                        || classType.Namespace.StartsWith("System."))
                    {
                        return;
                    }

                    var ns = _context.GetNamespaceByName(classType.Namespace);
                    classContainingMethod = ns.GetClassByType(classType);
                    isExtensionMethod = true;
                }
            }

            var method = new Method(node.Identifier.Text, GetType(node.ReturnType))
            {
                Abstract = classContainingMethod.Interface || HasModifier(node, "abstract"),
                Static = !isExtensionMethod && (classContainingMethod.Static || HasModifier(node, "static"))
            };

            var symbol = _model.GetDeclaredSymbol(node);
            if (symbol != null)
            {
                method.Overload = symbol
                    .ContainingType
                    .GetMembers()
                    .Count(member => member.Name == method.Name) > 1;
            }

            if (method.Abstract)
            {
                _topClass.UsedTypes.Add(new PythonType("abstractmethod", "abc"));
            }

            if (method.Overload)
            {
                _topClass.UsedTypes.Add(new PythonType("overload", "typing"));
            }

            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                method.Summary = doc["summary"].GetText();
            }

            if (HasModifier(node, "protected"))
            {
                method.Summary = PrefixSummary(method.Summary, "This method is protected.");
            }

            var docStrings = new List<string>();

            foreach (var parameterSyntax in node.ParameterList.Parameters)
            {
                // Skip the parameter which marks this method as an extension method
                if (parameterSyntax.Modifiers.Any(modifier => modifier.Text == "this"))
                {
                    continue;
                }

                var originalName = parameterSyntax.Identifier.Text;
                var parameter = new Parameter(FormatParameterName(originalName), GetType(parameterSyntax.Type));

                if (parameterSyntax.Modifiers.Any(modifier => modifier.Text == "params"))
                {
                    parameter.VarArgs = true;
                    parameter.Type = parameter.Type.TypeParameters[0];
                }

                if (parameterSyntax.Default != null)
                {
                    parameter.Value = FormatValue(parameterSyntax.Default.Value.ToString());
                }

                var paramNodes = doc.GetElementsByTagName("param");
                for (var i = 0; i < paramNodes.Count; i++)
                {
                    var element = (XmlElement) paramNodes[i];
                    if (element.Attributes["name"]?.Value == originalName)
                    {
                        docStrings.Add($":param {parameter.Name}: {element.GetText()}");
                    }
                }

                method.Parameters.Add(parameter);
            }

            if (doc["returns"] != null)
            {
                docStrings.Add($":returns: {doc["returns"].GetText()}");
            }

            docStrings = docStrings.Select(str => str.Replace('\n', ' ')).ToList();

            if (docStrings.Count > 0)
            {
                var paramText = string.Join("\n", docStrings);
                method.Summary = method.Summary != null
                    ? method.Summary + "\n\n" + paramText
                    : paramText;
            }

            classContainingMethod.Methods.Add(method);
        }

        private bool EnterClass(BaseTypeDeclarationSyntax node)
        {
            if (HasModifier(node, "private"))
            {
                return false;
            }

            Class cls;
            if (_currentClass == null)
            {
                // GetType() stores the used types in _topClass
                _topClass = new Class(new PythonType("Stub", "Stub"));

                cls = _currentNamespace.GetClassByType(GetType(node));
                cls.UsedTypes.UnionWith(_topClass.UsedTypes);

                _topClass = null;
            }
            else
            {
                cls = new Class(GetType(node));
            }

            if (_currentClass == null)
            {
                _currentClass = cls;
                _topClass = cls;
            }
            else
            {
                cls.ParentClass = _currentClass;
                _currentClass.InnerClasses.Add(cls);
                _currentClass = cls;
            }

            cls.Static = HasModifier(node, "static");

            if (cls.Type.TypeParameters.Count > 0)
            {
                _topClass.UsedTypes.Add(new PythonType("Generic", "typing"));
            }

            CheckForInheritedTypes(node);
            CheckForClassSummary(node);

            return true;
        }

        private void ExitClass()
        {
            _currentClass = _currentClass.ParentClass;

            if (_currentClass == null)
            {
                _topClass = null;
            }
        }

        private void CheckForInheritedTypes(BaseTypeDeclarationSyntax node)
        {
            var symbol = _model.GetDeclaredSymbol(node);

            if (symbol == null)
            {
                return;
            }

            if (node is InterfaceDeclarationSyntax || HasModifier(node, "abstract"))
            {
                var abcType = new PythonType("ABC", "abc");
                _currentClass.InheritsFrom.Add(abcType);
                _topClass.UsedTypes.Add(abcType);
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

            if (HasModifier(node, "protected"))
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

        private bool HasModifier(MemberDeclarationSyntax node, string modifier)
        {
            return node.Modifiers.Any(m => m.Text == modifier);
        }

        private string FormatValue(string value)
        {
            // null to None
            if (value == "null")
            {
                return "None";
            }

            // Boolean true
            if (value == "true")
            {
                return "True";
            }

            // Boolean false
            if (value == "false")
            {
                return "False";
            }

            // If the value is a number, remove a potential suffix like "m" in 1.0m
            if (Regex.IsMatch(value, @"^\d"))
            {
                if (Regex.IsMatch(value, "[^0-9]$"))
                {
                    return value.Substring(0, value.Length - 1);
                }

                return value;
            }

            // Strings
            if (value.StartsWith("@\"") && value.EndsWith("\""))
            {
                value = value.Substring(1);
            }

            // If the value contains certain characters it doesn't have a Python equivalent
            if (value.Contains("new ") || value.Contains("<") || value.Contains("(") || value.Contains("@\""))
            {
                return "None";
            }

            return value;
        }

        private string FormatParameterName(string name)
        {
            // Remove "@" prefix
            if (name.StartsWith("@"))
            {
                name = name.Substring(1);
            }

            // Escape keywords
            return name switch
            {
                "from" => "_from",
                "enum" => "_enum",
                _ => name
            };
        }
    }
}

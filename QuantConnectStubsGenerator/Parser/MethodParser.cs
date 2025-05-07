/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

using System;
using System.Linq;
using System.Xml;
using Microsoft.CodeAnalysis;
using System.Collections.Generic;
using QuantConnectStubsGenerator.Model;
using QuantConnectStubsGenerator.Utility;
using Microsoft.CodeAnalysis.CSharp.Syntax;

namespace QuantConnectStubsGenerator.Parser
{
    public class MethodParser : BaseParser
    {
        private bool SkipTypeNormalization => !_currentClass?.Type.Namespace.StartsWith("QuantConnect") ?? true;

        public MethodParser(ParseContext context, SemanticModel model) : base(context, model)
        {
        }

        public override void VisitMethodDeclaration(MethodDeclarationSyntax node)
        {
            PythonType genericType = null;
            if (node.TypeParameterList != null)
            {
                if (node.TypeParameterList.Parameters.Count > 1
                    || !node.Identifier.Text.Equals("history", StringComparison.InvariantCultureIgnoreCase))
                {
                    // skip, multiple generics or any different to history, we don't expect users to use those
                    return;
                }
                var parameterType = node.TypeParameterList.Parameters.First();
                genericType = _typeConverter.GetType(parameterType, skipTypeNormalization: SkipTypeNormalization);
            }

            var avoidImplicitConversionTypes = ShouldAvoidImplicitConversionTypes(node);
            var returnType = _typeConverter.GetType(node.ReturnType, skipTypeNormalization: SkipTypeNormalization);

            VisitMethod(
                node,
                node.Identifier.Text,
                node.ParameterList.Parameters,
                returnType,
                genericType,
                avoidImplicitConversionTypes);

            // Make the current class extend from typing.Iterable if this is an applicable GetEnumerator() method
            ExtendIterableIfNecessary(node, returnType);

            // Add __contains__ and __len__ methods to containers in System.Collections.Generic
            AddContainerMethodsIfNecessary(node);
        }

        private bool ShouldAvoidImplicitConversionTypes(MethodDeclarationSyntax node)
        {
            return HasAttribute(node.AttributeLists, "StubsAvoidImplicits") || _currentClass.GetClassAndBaseClasses(_context).Any(cls => cls.AvoidImplicitTypes);
        }

        public override void VisitConstructorDeclaration(ConstructorDeclarationSyntax node)
        {
            if (HasModifier(node, "static"))
            {
                return;
            }

            VisitMethod(node, "__init__", node.ParameterList.Parameters, new PythonType("None"), null, false);
        }

        public override void VisitDelegateDeclaration(DelegateDeclarationSyntax node)
        {
            VisitMethod(
                node,
                node.Identifier.Text,
                node.ParameterList.Parameters,
                _typeConverter.GetType(node.ReturnType, skipTypeNormalization: SkipTypeNormalization), null, false);
        }

        public override void VisitIndexerDeclaration(IndexerDeclarationSyntax node)
        {
            if (ShouldSkip(node))
            {
                return;
            }

            var returnType = _typeConverter.GetType(node.Type, skipTypeNormalization: SkipTypeNormalization);

            // Improve the autocomplete on data[symbol] if data is a Slice and symbol a Symbol
            // In C# this is of type dynamic, which by default gets converted to typing.Any
            // To improve the autocomplete a bit we convert it to Union[TradeBar, QuoteBar, List[Tick], Any]
            if (_currentClass?.Type.ToPythonString() == "QuantConnect.Data.Slice")
            {
                returnType = new PythonType("Union", "typing")
                {
                    TypeParameters =
                    {
                        new PythonType("TradeBar", "QuantConnect.Data.Market"),
                        new PythonType("QuoteBar", "QuantConnect.Data.Market"),
                        new PythonType("List", "System.Collections.Generic")
                        {
                            TypeParameters = {new PythonType("Tick", "QuantConnect.Data.Market")}
                        },
                        new PythonType("Any", "typing")
                    }
                };
            }

            if (returnType.Namespace == "System" && returnType.Name == "Object")
            {
                returnType = new PythonType("Any", "typing");
            }

            VisitMethod(node, "__getitem__", node.ParameterList.Parameters, returnType, null, false);

            var symbol = _typeConverter.GetSymbol(node);
            if (symbol is IPropertySymbol propertySymbol && !propertySymbol.IsReadOnly)
            {
                VisitMethod(node, "__setitem__", node.ParameterList.Parameters, new PythonType("None"), null, false);

                var valueParameter = new Parameter("value", returnType);
                _currentClass.Methods.Last().Parameters.Add(valueParameter);
            }
        }

        private void VisitMethod(
            MemberDeclarationSyntax node,
            string name,
            SeparatedSyntaxList<ParameterSyntax> parameterList,
            PythonType returnType,
            PythonType genericType,
            bool avoidImplicitConversionTypes)
        {
            if (_currentClass == null || ShouldSkip(node))
            {
                return;
            }

            // Some methods in the AST have parameters without names
            // Because these parameters cause syntax errors in the generated Python code we skip those methods
            if (parameterList.Any(parameter => FormatParameterName(parameter.Identifier.Text) == ""))
            {
                return;
            }

            var originalReturnType = returnType;

            var method = new Method(name, returnType)
            {
                Class = _currentClass,
                Static = HasModifier(node, "static"),
                File = _model.SyntaxTree.FilePath,
                DeprecationReason = GetDeprecationReason(node)
            };

            var doc = ParseDocumentation(node);
            if (doc["summary"] != null)
            {
                method.Summary = doc["summary"].GetText();
            }

            if (HasModifier(node, "protected"))
            {
                method.Summary = AppendSummary(method.Summary, "This method is protected.");
            }

            if (method.DeprecationReason != null)
            {
                method.Summary = AppendSummary(method.Summary, method.DeprecationReason);
            }

            var docStrings = new List<string>();
            var outTypes = new List<PythonType>();

            foreach (var parameter in parameterList)
            {
                var parsedParameter = ParseParameter(parameter, avoidImplicitConversionTypes);

                if (parsedParameter == null)
                {
                    continue;
                }

                foreach (XmlElement paramNode in doc.GetElementsByTagName("param"))
                {
                    if (paramNode.Attributes["name"]?.Value != parameter.Identifier.Text)
                    {
                        continue;
                    }

                    var text = paramNode.GetText();

                    if (text.Trim().Length == 0)
                    {
                        continue;
                    }

                    if (CheckDocSuggestsPandasDataFrame(text))
                    {
                        parsedParameter.Type = new PythonType("DataFrame", "pandas");
                    }

                    docStrings.Add($":param {parsedParameter.Name}: {text}");
                    break;
                }

                method.Parameters.Add(parsedParameter);

                if (parameter.Modifiers.Any(m => m.Text == "out"))
                {
                    var actualType = parsedParameter.Type;

                    // Python.NET allows passing None to out parameters
                    parsedParameter.Type = new PythonType("Optional", "typing")
                    {
                        TypeParameters = { actualType }
                    };

                    outTypes.Add(actualType);
                }
            }

            // Python.NET returns a tuple if a method has out parameters
            // The first item is the return value of the method, the following items are the out parameters
            if (outTypes.Count > 0)
            {
                var tupleType = new PythonType("Tuple", "typing");
                tupleType.TypeParameters.Add(method.ReturnType);
                outTypes.ForEach(type => tupleType.TypeParameters.Add(type));
                method.ReturnType = tupleType;
            }

            var returnsParts = new List<string>();

            if (doc["returns"] != null)
            {
                var text = doc["returns"].GetText();

                if (text.Trim().Length > 0)
                {
                    returnsParts.Add(text);
                }
            }

            if (returnsParts.Count > 0)
            {
                var parts = returnsParts.Select(part => part.EndsWith(".") ? part : part + ".");
                var text = string.Join(" ", parts);

                docStrings.Add($":returns: {text}");

                if (CheckDocSuggestsPandasDataFrame(text))
                {
                    method.ReturnType = new PythonType("DataFrame", "pandas");
                }
            }

            docStrings = docStrings.Select(str => str.Replace('\n', ' ')).ToList();

            if (docStrings.Count > 0)
            {
                var paramText = string.Join("\n", docStrings);
                method.Summary = method.Summary != null
                    ? method.Summary + "\n\n" + paramText
                    : paramText;
            }
            method.GenericType = genericType;
            _currentClass.Methods.Add(method);

            ImprovePythonAccessorIfNecessary(method);
            ImproveDictionaryDefinitionIfNecessary(node, method);
        }

        private Parameter ParseParameter(ParameterSyntax syntax, bool avoidImplicitConversionTypes)
        {
            avoidImplicitConversionTypes |= HasAttribute(syntax.AttributeLists, "StubsAvoidImplicits");
            var originalName = syntax.Identifier.Text;
            var parameter = new Parameter(FormatParameterName(originalName), _typeConverter.GetType(syntax.Type, skipTypeNormalization: SkipTypeNormalization));

            if (syntax.Modifiers.Any(modifier => modifier.Text == "params"))
            {
                parameter.VarArgs = true;
                var iterableType = new PythonType("Iterable", "typing") { TypeParameters = parameter.Type.TypeParameters };
                parameter.Type = PythonType.CreateUnion(parameter.Type.TypeParameters[0], iterableType);
            }

            if (!avoidImplicitConversionTypes)
            {
                // Symbol parameters can be both a Symbol or a string in most methods
                if (parameter.Type.Equals(PythonType.SymbolType))
                {
                    parameter.Type = PythonType.ImplicitConversionParameterSymbolType;
                }

                // IDataConsolidator parameters can be either IDataConsolidator, PythonConsolidator or timedelta
                if (parameter.Type.Namespace == "QuantConnect.Data.Consolidators"
                    && parameter.Type.Name == "IDataConsolidator")
                {
                    parameter.Type = PythonType.CreateUnion(parameter.Type,
                        new PythonType("PythonConsolidator", "QuantConnect.Python"), new PythonType("timedelta", "datetime"));
                }

                // datetime parameters also accept dates
                if (parameter.Type.Namespace == "datetime" && parameter.Type.Name == "datetime")
                {
                    parameter.Type = PythonType.CreateUnion(parameter.Type, new PythonType("date", "datetime"));
                }
            }

            // Methods like AddData<T> and History<T> have Python implementations accepting "T" as first parameter
            // We set the types of these parameters to typing.Type instead of the default typing.Any
            if (_model.SyntaxTree.FilePath.EndsWith(".Python.cs")
                && (parameter.Name == "type" || parameter.Name == "dataType" || parameter.Name == "T"))
            {
                parameter.Type = new PythonType("Type", "typing");
            }

            // System.Object parameters can accept anything
            if (parameter.Type.Namespace == "System" && parameter.Type.Name == "Object")
            {
                parameter.Type = new PythonType("Any", "typing");
            }

            if (syntax.Default != null)
            {
                parameter.Value = FormatValue(syntax.Default.Value.ToString());
            }

            return parameter;
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
                "lambda" => "_lambda",
                _ => name
            };
        }

        private void ExtendIterableIfNecessary(MethodDeclarationSyntax node, PythonType returnType)
        {
            if (node.Identifier.Text != "GetEnumerator")
            {
                return;
            }

            // Some GetEnumerator() methods return an IEnumerator, some return an IEnumerator<T>
            // typing.Iterable requires a type parameter, so we don't extend it if an IEnumerator is returned
            var typeParameters = returnType.TypeParameters;
            if (typeParameters.Count == 0)
            {
                return;
            }

            var iterableType = new PythonType("Iterable", "typing")
            {
                TypeParameters = typeParameters
            };

            if (!_currentClass.InheritsFrom.Any(t => t.Namespace == "typing" && t.Name == "Iterable"))
            {
                _currentClass.InheritsFrom.Add(iterableType);
            }

            if (_currentClass.Methods.All(m => m.Name != "__iter__"))
            {
                var iteratorType = new PythonType("Iterator", "typing")
                {
                    TypeParameters = typeParameters
                };
                _currentClass.Methods.Add(new Method("__iter__", iteratorType) { Class = _currentClass });
            }
        }

        private void AddContainerMethodsIfNecessary(MethodDeclarationSyntax node)
        {
            if (node.Identifier.Text != "Contains" && node.Identifier.Text != "ContainsKey")
            {
                return;
            }

            if (_currentNamespace.Name != "System.Collections.Generic")
            {
                return;
            }

            AddContainerMethods(node);
        }

        private void AddContainerMethods(MethodDeclarationSyntax node)
        {
            VisitMethod(node, "__contains__", node.ParameterList.Parameters, _typeConverter.GetType(node.ReturnType, skipTypeNormalization: SkipTypeNormalization), null, false);

            if (_currentClass.Methods.All(m => m.Name != "__len__"))
            {
                _currentClass.Methods.Add(new Method("__len__", new PythonType("int")) { Class = _currentClass });
            }
        }

        /// <summary>
        /// There are several Python-friendly accessors like Slice.Get(Type) instead of Slice.Get&lt;T&gt;().
        /// If we spot such a Python-friendly accessor, we remove the non-Python-friendly accessor and improve
        /// the Python-friendly accessor's definition.
        /// </summary>
        private void ImprovePythonAccessorIfNecessary(Method newMethod)
        {
            if (newMethod.Parameters.Count != 1 || newMethod.Parameters[0].Type.ToPythonString() != "typing.Type")
            {
                return;
            }

            var existingMethod = _currentClass.Methods
                .FirstOrDefault(m => m.Name == newMethod.Name && m.Parameters.Count == 0);

            if (existingMethod == null)
            {
                return;
            }

            var typeParameter = existingMethod.ReturnType;
            while (!typeParameter.IsNamedTypeParameter && typeParameter.TypeParameters.Count > 0)
            {
                typeParameter = typeParameter.TypeParameters[0];
            }

            if (!typeParameter.IsNamedTypeParameter)
            {
                return;
            }

            newMethod.Parameters[0].Type = typeParameter;
            newMethod.ReturnType = existingMethod.ReturnType;

            _currentClass.Methods.Remove(existingMethod);
        }

        private void ImproveDictionaryDefinitionIfNecessary(MemberDeclarationSyntax node, Method method)
        {
            // We add container methods to classes that implement Count and ContainsKey
            // because Python.Net does this to add support for operators like 'in' to work with these types
            if (node is MethodDeclarationSyntax methodNode &&
                method.Name == "ContainsKey" &&
                method.Parameters.Count == 1 &&
                _currentClass.Properties.Any(property => property.Name == "Count"))
            {
                AddContainerMethods(methodNode);
            }
        }

        /// <summary>
        /// Returns whether the provided documentation string suggests that a certain type is a pandas DataFrame.
        /// </summary>
        private bool CheckDocSuggestsPandasDataFrame(string doc)
        {
            return doc.Contains("pandas DataFrame") || doc.Contains("pandas.DataFrame");
        }
    }
}


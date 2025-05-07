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

using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using NUnit.Framework;
using QuantConnectStubsGenerator.Model;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace QuantConnectStubsGenerator.Tests
{
    [TestFixture]
    public class RendererTests
    {
        [TestCaseSource(nameof(RenderTestCases))]
        public void GeneratesEventContainerClassForEventsDelegates(Dictionary<string, string> testFiles,
            string[] expectedGeneratedFiles)
        {
            var testGenerator = new TestGenerator
            {
                Files = testFiles
            };

            testGenerator.GenerateModelsAndRender(out var context, out var renderedNamespaces);

            Assert.AreEqual(expectedGeneratedFiles.Length, renderedNamespaces.Count);

            for (var i = 0; i < expectedGeneratedFiles.Length; i++)
            {
                var expectedFile = expectedGeneratedFiles[i];
                var renderedFile = renderedNamespaces[i];
                // Remove all whitespace and new lines
                var expectedFileWithoutWhitespace = string.Concat(expectedFile.Where(c => !char.IsWhiteSpace(c)));
                var renderedFileWithoutWhitespace = string.Concat(renderedFile.Where(c => !char.IsWhiteSpace(c)));
                Assert.AreEqual(expectedFileWithoutWhitespace, renderedFileWithoutWhitespace);
            }
        }

        private static TestCaseData[] RenderTestCases => new[]
        {
            // SkipsPropertyIfThereIsAMethodWithTheSameName
            new TestCaseData(
                new Dictionary<string, string>()
                {
                    {
                        "Test1.cs",
                        @"
namespace QuantConnect.Namespace1
{
    public interface IInterface
    {
        string test();
    }

    public class BaseClass : IInterface
    {
        public string test()
        {
            return ""Test"";
        }
    }
}"
                    },
                    {
                        "Test2.cs",
                        @"
using QuantConnect.Namespace1;

namespace QuantConnect.Namespace2
{
    public interface IInterface
    {
        int test2();
    }

    public class TestClass : BaseClass, IInterface
    {
        public int Test { get; set; }

        public int test2()
        {
            return 0;
        }
    }
}"
                    }
                },
                new[]
                {
                    @"
from typing import overload
from enum import Enum
import abc

import QuantConnect.Namespace1
import System

class IInterface(metaclass=abc.ABCMeta):
    """"""This class has no documentation.""""""

    def test(self) -> str:
        ...

class BaseClass(System.Object, QuantConnect.Namespace1.IInterface):
    """"""This class has no documentation.""""""

    def test(self) -> str:
        ...
",
                @"
from typing import overload
from enum import Enum
import abc

import QuantConnect.Namespace1
import QuantConnect.Namespace2

class IInterface(metaclass=abc.ABCMeta):
    """"""This class has no documentation.""""""

    def test_2(self) -> int:
        ...

class TestClass(QuantConnect.Namespace1.BaseClass, QuantConnect.Namespace2.IInterface):
    """"""This class has no documentation.""""""

    def test_2(self) -> int:
        ...
"
                }).SetName("SkipsPropertyIfThereIsAMethodWithTheSameName"),

            // CSharpEnumeratorsArePythonIterables
            new TestCaseData(
                new Dictionary<string, string>()
                {
                    {
                        "Test.cs",
                        @"
using System;
using System.Collections.Generic;

namespace QuantConnect.Test
{
    public class TestEnumerable1 : IEnumerable<int>
    {
        public IEnumerator<int> GetEnumerator()
        {
            yield return 1;
        }
        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }

    public class TestDerivedEnumerable1 : TestEnumerable
    {
    }

    /// <summary>
    /// This will not inherit typing.Iterable directly, but IEnumerable[string] will.
    /// __iter__ will be generated for IEnumerable[string], not for this class.
    /// </summary>
    public class TestEnumerable2 : List<string>
    {
    }
}"
                    }
                },
                new[]
                {
                @"
from typing import overload
from enum import Enum
import typing

import QuantConnect.Test
import System
import System.Collections.Generic

TestEnumerable = typing.Any


class TestEnumerable1(System.Object, typing.Iterable[int]):
    """"""This class has no documentation.""""""

    def __iter__(self) -> typing.Iterator[int]:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[int]:
        ...


class TestDerivedEnumerable1(TestEnumerable):
    """"""This class has no documentation.""""""


class TestEnumerable2(typing.List[str]):
    """"""
    This will not inherit typing.Iterable directly, but IEnumerable[string] will.
    __iter__ will be generated for IEnumerable[string], not for this class.
    """"""
"
                }).SetName("CSharpEnumeratorsArePythonIterables"),

            // GeneratesIterableOverloadsForEnumerableParameters
            new TestCaseData(
                new Dictionary<string, string>()
                {
                    {
                        "Test.cs",
                        @"
using System;
using System.Collections.Generic;

namespace QuantConnect.Test
{
    public class TestClass
    {
        public TestClass(int someParam, IEnumerable<int> enumerable)
        {
        }

        public TestClass(List<int> enumerable)
        {
        }

        public void Method1(IList<string> enumerable)
        {
        }

        public void Method2(DateTime someParam, IList<List<string>> enumerable)
        {
        }
    }
}"
                    }
                },
                new[]
                {
                @"
from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect.Test
import System


class TestClass(System.Object):
    """"""This class has no documentation.""""""

    @overload
    def __init__(self, some_param: int, enumerable: typing.Iterable[int]) -> None:
        ...

    @overload
    def __init__(self, enumerable: typing.List[int]) -> None:
        ...

    def method_1(self, enumerable: typing.List[str]) -> None:
        ...

    def method_2(self, some_param: typing.Union[datetime.datetime, datetime.date], enumerable: typing.List[typing.List[str]]) -> None:
        ...
"
                }).SetName("GeneratesIterableOverloadsForEnumerableParameters"),

            // GeneratesEventContainerClassForEventsDelegates
            new TestCaseData(
                new Dictionary<string, string>()
                {
                    {
                        "Test.cs",
                        @"
using System;
using System.Collections.Generic;

namespace QuantConnect.Test
{
    public class TestEventArgs : EventArgs
    {
        public string Message { get; }

        public TestEventArgs(string message)
        {
            Message = message;
        }
    }

    public delegate void TestEventDelegate(object sender, IndicatorDataPoint updated);

    public class TestClass
    {
        public event TestEventDelegate TestEvent;
    }
}"
                    }
                },
                new[]
                {
                @"
from typing import overload
from enum import Enum
import typing

import QuantConnect.Test
import System

IndicatorDataPoint = typing.Any

QuantConnect_Test__EventContainer_Callable = typing.TypeVar(""QuantConnect_Test__EventContainer_Callable"")
QuantConnect_Test__EventContainer_ReturnType = typing.TypeVar(""QuantConnect_Test__EventContainer_ReturnType"")


class TestEventArgs(System.EventArgs):
    """"""This class has no documentation.""""""

    @property
    def message(self) -> str:
        ...

    def __init__(self, message: str) -> None:
        ...

class TestClass(System.Object):
    """"""This class has no documentation.""""""

    @property
    def test_event(self) -> _EventContainer[typing.Callable[[System.Object, IndicatorDataPoint], None], None]:
        ...

    @test_event.setter
    def test_event(self, value: _EventContainer[typing.Callable[[System.Object, IndicatorDataPoint], None], None]) -> None:
        ...

class _EventContainer(typing.Generic[QuantConnect_Test__EventContainer_Callable, QuantConnect_Test__EventContainer_ReturnType]):
    """"""This class is used to provide accurate autocomplete on events and cannot be imported.""""""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Test__EventContainer_ReturnType:
        """"""Fires the event.""""""
        ...

    def __iadd__(self, item: QuantConnect_Test__EventContainer_Callable) -> typing.Self:
        """"""Registers an event handler.""""""
        ...

    def __isub__(self, item: QuantConnect_Test__EventContainer_Callable) -> typing.Self:
        """"""Unregisters an event handler.""""""
        ...
"
                }).SetName("GeneratesEventContainerClassForEventsDelegates"),

            // GeneratesContainerMethodsForDictionaries
            new TestCaseData(
                new Dictionary<string, string>()
                {
                    {
                        "IDictionary.cs",
                        @"
namespace System.Collections
{
    public interface IDictionary : ICollection
    {
    }

    public interface IDictionary : ICollection
    {
    }
}
"
                    },
                    {
                        "KeyValuePair.cs",
                        @"
namespace System.Collections.Generic
{
    public readonly struct KeyValuePair<TKey, TValue>
    {
    }
}
"
                    },
                    {
                        "Test.cs",
                        @"
using System;
using System.Collections;
using System.Collections.Generic;

namespace QuantConnect.Test
{
    public class TestDictionary<TKey, TValue> : IDictionary
    {
        private readonly Dictionary<TValue, TKey> _data = new();

        public int Count => _data.Count

        public bool ContainsKey(TKey key)
        {
            return data.ContainsKey(key);
        }
    }

    public class TestDictionary2<TKey, TValue> : IEnumerable<KeyValuePair<TKey, TValue>>
    {
        private readonly List<KeyValuePair<TKey, TValue>> _data = new();

        public int Count => _data.Count

        public bool ContainsKey(TKey key)
        {
            return data.ContainsKey(key);
        }
    }
}"
                    }
                },
                new[]
                {
                    @"
from typing import overload
from enum import Enum
import abc

import System.Collections

class IDictionary(System.Collections.ICollection, metaclass=abc.ABCMeta):
    """"""This class has no documentation.""""""
",
                    @"
from typing import overload
from enum import Enum
import typing

import System.Collections.Generic

System_Collections_Generic_KeyValuePair_TKey = typing.TypeVar(""System_Collections_Generic_KeyValuePair_TKey"")
System_Collections_Generic_KeyValuePair_TValue = typing.TypeVar(""System_Collections_Generic_KeyValuePair_TValue"")

class KeyValuePair(typing.Generic[System_Collections_Generic_KeyValuePair_TKey, System_Collections_Generic_KeyValuePair_TValue]):
    """"""This class has no documentation.""""""
",
                    @"
from typing import overload
from enum import Enum
import typing

import QuantConnect.Test
import System
import System.Collections
import System.Collections.Generic

QuantConnect_Test_TestDictionary_TKey = typing.TypeVar(""QuantConnect_Test_TestDictionary_TKey"")
QuantConnect_Test_TestDictionary_TValue = typing.TypeVar(""QuantConnect_Test_TestDictionary_TValue"")
QuantConnect_Test_TestDictionary2_TKey = typing.TypeVar(""QuantConnect_Test_TestDictionary2_TKey"")
QuantConnect_Test_TestDictionary2_TValue = typing.TypeVar(""QuantConnect_Test_TestDictionary2_TValue"")

class TestDictionary(typing.Generic[QuantConnect_Test_TestDictionary_TKey, QuantConnect_Test_TestDictionary_TValue], System.Object, System.Collections.IDictionary):
    """"""This class has no documentation.""""""

    @property
    def count(self) -> int:
        ...

    def __contains__(self, key: QuantConnect_Test_TestDictionary_TKey) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def contains_key(self, key: QuantConnect_Test_TestDictionary_TKey) -> bool:
        ...

class TestDictionary2(typing.Generic[QuantConnect_Test_TestDictionary2_TKey, QuantConnect_Test_TestDictionary2_TValue], System.Object, typing.Iterable[System.Collections.Generic.KeyValuePair[QuantConnect_Test_TestDictionary2_TKey, QuantConnect_Test_TestDictionary2_TValue]]):
    """"""This class has no documentation.""""""

    @property
    def count(self) -> int:
        ...

    def __contains__(self, key: QuantConnect_Test_TestDictionary2_TKey) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def contains_key(self, key: QuantConnect_Test_TestDictionary2_TKey) -> bool:
        ...
"
                }).SetName("GeneratesContainerMethodsForDictionaries"),

            // GeneratesMethodsWithSymbolImplicitConversionForInheritedGenericClasses
            new TestCaseData(
                new Dictionary<string, string>()
                {
                    {
                        "Symbol.cs",
                        @"
namespace QuantConnect
{
    public class Symbol
    {
    }
}"
                    },
                    {
                        "Test.cs",
                        @"
using System;
using System.Collections;
using System.Collections.Generic;

namespace QuantConnect.Test
{
    public class TestGenericClass<T1, T2>
    {
        public T1 TestMethod1(T1 t1Param, T2 t2Param) {}

        /// <summary>
        /// This method will not be explicitly added to TestClass because it does not need
        /// the Symbol implicit conversion support, given that non of its parameters is directly T1
        /// (which will be set to Symbol in the class below)
        /// </summary>
        public T2 TestMethod2(List<T1> t1Param, T2 t2Param) {}

        public List<Dictionary<T1, T2>> TestMethod3(T1 t1Param, List<Dictionary<T1, List<T2>>> t2Param) {}
    }

    public class TestClass : TestGenericClass<Symbol, DateTime>
    {
    }
}"
                    }
                },
                new[]
                {
                    @"
from typing import overload
from enum import Enum
import QuantConnect
import System


class Symbol(System.Object):
    """"""This class has no documentation.""""""
",
                    @"
from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect
import QuantConnect.Data.Market
import QuantConnect.Test
import System
import System.Collections.Generic

QuantConnect_Test_TestGenericClass_T1 = typing.TypeVar(""QuantConnect_Test_TestGenericClass_T1"")
QuantConnect_Test_TestGenericClass_T2 = typing.TypeVar(""QuantConnect_Test_TestGenericClass_T2"")

class TestGenericClass(typing.Generic[QuantConnect_Test_TestGenericClass_T1, QuantConnect_Test_TestGenericClass_T2], System.Object):
    """"""This class has no documentation.""""""

    def test_method_1(self, t_1_param: QuantConnect_Test_TestGenericClass_T1, t_2_param: QuantConnect_Test_TestGenericClass_T2) -> QuantConnect_Test_TestGenericClass_T1:
        ...

    def test_method_2(self, t_1_param: typing.List[QuantConnect_Test_TestGenericClass_T1], t_2_param: QuantConnect_Test_TestGenericClass_T2) -> QuantConnect_Test_TestGenericClass_T2:
        """"""
        This method will not be explicitly added to TestClass because it does not need
        the Symbol implicit conversion support, given that non of its parameters is directly T1
        (which will be set to Symbol in the class below)
        """"""
        ...

    def test_method_3(self, t_1_param: QuantConnect_Test_TestGenericClass_T1, t_2_param: typing.List[System.Collections.Generic.Dictionary[QuantConnect_Test_TestGenericClass_T1, typing.List[QuantConnect_Test_TestGenericClass_T2]]]) -> typing.List[System.Collections.Generic.Dictionary[QuantConnect_Test_TestGenericClass_T1, QuantConnect_Test_TestGenericClass_T2]]:
        ...

class TestClass(QuantConnect.Test.TestGenericClass[QuantConnect.Symbol, datetime.datetime]):
    """"""This class has no documentation.""""""

    def test_method_1(self, t_1_param: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract], t_2_param: datetime.datetime) -> QuantConnect.Symbol:
        ...

    def test_method_3(self, t_1_param: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract], t_2_param: typing.List[System.Collections.Generic.Dictionary[QuantConnect.Symbol, typing.List[datetime.datetime]]]) -> typing.List[System.Collections.Generic.Dictionary[QuantConnect.Symbol, datetime.datetime]]:
        ...
"
                }).SetName("GeneratesMethodsWithSymbolImplicitConversionForInheritedGenericClasses"),
        };

        private class TestGenerator : Generator
        {
            private List<StringBuilder> _stringBuilders = new();

            public Dictionary<string, string> Files { get; set; }

            public TestGenerator() : base("/", "/", "/")
            {
            }

            protected override IEnumerable<SyntaxTree> GetSyntaxTrees()
            {
                foreach (var fileContent in Files)
                {
                    yield return CSharpSyntaxTree.ParseText(fileContent.Value, path: fileContent.Key);
                }
            }

            protected override TextWriter CreateWriter(string path)
            {
                var stringBuilder = new StringBuilder();
                _stringBuilders.Add(stringBuilder);
                return new StringWriter(stringBuilder);
            }

            public void GenerateModelsAndRender(out ParseContext context, out List<string> renderedNamespaces)
            {
                context = new ParseContext();
                base.GenerateModels(context);

                _stringBuilders.Clear();
                foreach (var ns in context.GetNamespaces())
                {
                    RenderNamespace(ns, "", context);
                }

                renderedNamespaces = _stringBuilders.Select(builder => builder.ToString()).ToList();
            }
        }
    }
}


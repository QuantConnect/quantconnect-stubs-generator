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
using System;
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
from enum import IntEnum
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
from enum import IntEnum
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
from enum import IntEnum
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
    This will not inherit typing.Iterable directly, but IEnumerable<string> will.
    __iter__ will be generated for IEnumerable<string>, not for this class.
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
using System.Collections;
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

        public void Method3(IList listParam)
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
from enum import IntEnum
import datetime
import typing

import QuantConnect.Test
import System


class TestClass(System.Object):
    """"""This class has no documentation.""""""

    @overload
    def __init__(self, some_param: int, enumerable: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, enumerable: typing.List[int]) -> None:
        ...

    def method_1(self, enumerable: typing.List[str]) -> None:
        ...

    def method_2(self, some_param: typing.Union[datetime.datetime, datetime.date], enumerable: typing.List[typing.List[str]]) -> None:
        ...

    def method_3(self, list_param: typing.List[typing.Any]) -> None:
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
from enum import IntEnum
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
    def test_event(self) -> _EventContainer[typing.Callable[[System.Object, IndicatorDataPoint], typing.Any], typing.Any]:
        ...

    @test_event.setter
    def test_event(self, value: _EventContainer[typing.Callable[[System.Object, IndicatorDataPoint], typing.Any], typing.Any]) -> None:
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
from enum import IntEnum
import abc

import System.Collections

class IDictionary(System.Collections.ICollection, metaclass=abc.ABCMeta):
    """"""This class has no documentation.""""""
",
                    @"
from typing import overload
from enum import IntEnum
import typing

import System.Collections.Generic

System_Collections_Generic_KeyValuePair_TKey = typing.TypeVar(""System_Collections_Generic_KeyValuePair_TKey"")
System_Collections_Generic_KeyValuePair_TValue = typing.TypeVar(""System_Collections_Generic_KeyValuePair_TValue"")

class KeyValuePair(typing.Generic[System_Collections_Generic_KeyValuePair_TKey, System_Collections_Generic_KeyValuePair_TValue]):
    """"""This class has no documentation.""""""
",
                    @"
from typing import overload
from enum import IntEnum
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
from enum import IntEnum
import QuantConnect
import System


class Symbol(System.Object):
    """"""This class has no documentation.""""""
",
                    @"
from typing import overload
from enum import IntEnum
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

            // GeneratesOperatorsMagicMethods
            new TestCaseData(
                new Dictionary<string, string>()
                {
                    {
                        "System.cs",
                        @"
namespace System
{
    public interface IComparable
    {
    }

    public interface IComparable<T>
    {
    }
}"
                    },
                    {
                        "Test.cs",
                        @"
using System;

namespace QuantConnect.Test
{
    public class TestClass
    {
        /// <summary>
        /// Addition operator
        /// </summary>
        /// <param name=""a"">Left operand</param>
        /// <param name=""b"">Right operand</param>
        /// <returns>Addition result</returns>
        public static TestClass operator +(TestClass a, TestClass b)
        {
            return new TestClass();
        }
        /// <summary>
        /// Subtraction operator
        /// </summary>
        /// <param name=""a"">Left operand</param>
        /// <param name=""b"">Right operand</param>
        /// <returns>Subtraction result</returns>
        public static TestClass operator -(TestClass a, TestClass b)
        {
            return new TestClass();
        }
        public static TestClass operator *(TestClass a, TestClass b)
        {
            return new TestClass();
        }
        public static TestClass operator /(TestClass a, TestClass b)
        {
            return new TestClass();
        }
        public static TestClass operator %(TestClass a, TestClass b)
        {
            return new TestClass();
        }
        public static bool operator ==(TestClass a, TestClass b)
        {
            return true;
        }
        public static bool operator !=(TestClass a, TestClass b)
        {
            return false;
        }
        public static bool operator >(TestClass a, TestClass b)
        {
            return true;
        }
        public static bool operator <(TestClass a, TestClass b)
        {
            return false;
        }
        public static bool operator >=(TestClass a, TestClass b)
        {
            return true;
        }
        public static bool operator <=(TestClass a, TestClass b)
        {
            return false;
        }
        public static TestClass operator &(TestClass a, TestClass b)
        {
            return new TestClass();
        }
        public static TestClass operator |(TestClass a, TestClass b)
        {
            return new TestClass();
        }
        public static TestClass operator ^(TestClass a, TestClass b)
        {
            return new TestClass();
        }
        public static TestClass operator >>(TestClass a, int b)
        {
            return new TestClass();
        }
        public static TestClass operator <<(TestClass a, int b)
        {
            return new TestClass();
        }

        /// <summary>
        /// Unary + operator
        /// </summary>
        public static TestClass operator +(TestClass operand)
        {
            return new TestClass();
        }

        /// <summary>
        /// Unary - operator
        /// </summary>
        public static TestClass operator -(TestClass operand)
        {
            return new TestClass();
        }
    }

    public class TestComparableClass1 : IComparable
    {
        public int CompareTo(object obj)
        {
            return 0;
        }
    }

    public class TestComparableClass2 : IComparable<TestComparableClass2>
    {
        public int CompareTo(TestComparableClass2 obj)
        {
            return 0;
        }
    }

    public class TestComparableClass3 : IComparable<TestComparableClass2>
    {
        public int CompareTo(TestComparableClass2 obj)
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
from enum import IntEnum
import abc
import typing

import System

System_IComparable_T = typing.TypeVar(""System_IComparable_T"")

class IComparable(typing.Generic[System_IComparable_T], metaclass=abc.ABCMeta):
    """"""This class has no documentation.""""""

",
                    @"
from typing import overload
from enum import IntEnum
import typing

import QuantConnect.Test
import System

QuantConnect_Test_TestComparableClass2 = typing.Any

class TestClass(System.Object):
    """"""This class has no documentation.""""""

    def __add__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        """"""
        Addition operator

        :param b: Right operand
        :returns: Addition result.
        """"""
        ...

    def __and__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        ...

    def __eq__(self, b: QuantConnect.Test.TestClass) -> bool:
        ...

    def __ge__(self, b: QuantConnect.Test.TestClass) -> bool:
        ...

    def __gt__(self, b: QuantConnect.Test.TestClass) -> bool:
        ...

    def __iadd__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        """"""
        Addition operator

        :param b: Right operand
        :returns: Addition result.
        """"""
        ...

    def __iand__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        ...

    def __ilshift__(self, b: int) -> QuantConnect.Test.TestClass:
        ...

    def __imod__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        ...

    def __imul__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        ...

    def __ior__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        ...

    def __irshift__(self, b: int) -> QuantConnect.Test.TestClass:
        ...

    def __isub__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        """"""
        Subtraction operator

        :param b: Right operand
        :returns: Subtraction result.
        """"""
        ...

    def __itruediv__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        ...

    def __ixor__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        ...

    def __le__(self, b: QuantConnect.Test.TestClass) -> bool:
        ...

    def __lshift__(self, b: int) -> QuantConnect.Test.TestClass:
        ...

    def __lt__(self, b: QuantConnect.Test.TestClass) -> bool:
        ...

    def __mod__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        ...

    def __mul__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        ...

    def __ne__(self, b: QuantConnect.Test.TestClass) -> bool:
        ...

    def __neg__(self) -> QuantConnect.Test.TestClass:
        """"""Unary - operator""""""
        ...

    def __or__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        ...

    def __pos__(self) -> QuantConnect.Test.TestClass:
        """"""Unary + operator""""""
        ...

    def __rshift__(self, b: int) -> QuantConnect.Test.TestClass:
        ...

    def __sub__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        """"""
        Subtraction operator

        :param b: Right operand
        :returns: Subtraction result.
        """"""
        ...

    def __truediv__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        ...

    def __xor__(self, b: QuantConnect.Test.TestClass) -> QuantConnect.Test.TestClass:
        ...

class TestComparableClass1(System.Object, System.IComparable):
    """"""This class has no documentation.""""""

    def __ge__(self, other: typing.Any) -> bool:
        ...

    def __gt__(self, other: typing.Any) -> bool:
        ...

    def __le__(self, other: typing.Any) -> bool:
        ...

    def __lt__(self, other: typing.Any) -> bool:
        ...

    def compare_to(self, obj: typing.Any) -> int:
        ...

class TestComparableClass2(System.Object, System.IComparable[QuantConnect_Test_TestComparableClass2]):
    """"""This class has no documentation.""""""

    def __ge__(self, other: QuantConnect.Test.TestComparableClass2) -> bool:
        ...

    def __gt__(self, other: QuantConnect.Test.TestComparableClass2) -> bool:
        ...

    def __le__(self, other: QuantConnect.Test.TestComparableClass2) -> bool:
        ...

    def __lt__(self, other: QuantConnect.Test.TestComparableClass2) -> bool:
        ...

    def compare_to(self, obj: QuantConnect.Test.TestComparableClass2) -> int:
        ...

class TestComparableClass3(System.Object, System.IComparable[QuantConnect.Test.TestComparableClass2]):
    """"""This class has no documentation.""""""

    def __ge__(self, other: QuantConnect.Test.TestComparableClass2) -> bool:
        ...

    def __gt__(self, other: QuantConnect.Test.TestComparableClass2) -> bool:
        ...

    def __le__(self, other: QuantConnect.Test.TestComparableClass2) -> bool:
        ...

    def __lt__(self, other: QuantConnect.Test.TestComparableClass2) -> bool:
        ...

    def compare_to(self, obj: QuantConnect.Test.TestComparableClass2) -> int:
        ...
"
                }).SetName("GeneratesOperatorsMagicMethods"),

            // DoesntReplacePartialMatchesWhenSnakeCasingParameterNamesInSummary
            new TestCaseData(
                new Dictionary<string, string>()
                {
                    {
                        "Test.cs",
                        @"
namespace QuantConnect.TestNamespace
{

    public class TestClass
    {
        /// <summary>
        /// This is a test method for the security type parameter. The partial matches should not be replaced.
        /// The first parameter is an upper case character, which will be replaced with a lower case character, 
        /// but it shouldn't be replaced in the rest of the summary.
        /// The third parameter name will be snake-cased, but when replacing in the string, 
        /// the last parameter should be left untouched so that is also correctly snake-cased afterwards.
        /// </summary>
        /// <param name=""T"">Test param 1</param>
        /// <param name=""securityType"">Test param 2</param>
        /// <param name=""someParam"">Test param 3</param>
        /// <param name=""someParamWithSuffix"">Test param 4</param>
        public void TestMethod(string T, string securityType, string someParam, string someParamWithSuffix)
        {
        }
    }
}"
                    },
                },
                new[]
                {
                    @"
from typing import overload
from enum import IntEnum
import QuantConnect.TestNamespace
import System


class TestClass(System.Object):
    """"""This class has no documentation.""""""

    def test_method(self, t: str, security_type: str, some_param: str, some_param_with_suffix: str) -> None:
        """"""
        This is a test method for the security type parameter. The partial matches should not be replaced.
        The first parameter is an upper case character, which will be replaced with a lower case character,
        but it shouldn't be replaced in the rest of the summary.
        The third parameter name will be snake-cased, but when replacing in the string,
        the last parameter should be left untouched so that is also correctly snake-cased afterwards.

        :param t: Test param 1
        :param security_type: Test param 2
        :param some_param: Test param 3
        :param some_param_with_suffix: Test param 4
        """"""
        ...
",
                }).SetName("DoesntReplacePartialMatchesWhenSnakeCasingParameterNamesInSummary"),

            // BracketsAreReplacedWithAngularBracketsInDocstringsToAvoidMarkdownIssues
            new TestCaseData(
                new Dictionary<string, string>()
                {
                    {
                        "Test1.cs",
                        @"
namespace QuantConnect.Namespace
{
    /// <summary>
    /// A ticket might be in the following format: [Ticker][2 digit day code][1 char month code][2/1 digit year code].
    /// Another test: [sds]sdsd[] 222 [] [abc][].
    /// </summary>
    public class TestClass
    {
        /// <summary>
        /// A ticket might be in the following format: [Ticker][2 digit day code][1 char month code][2/1 digit year code].
        /// Another test: [sds]sdsd[] 222 [] [abc][].
        /// </summary>
        public int TestProperty { get; set; }

        /// <summary>
        /// A ticket might be in the following format: [Ticker][2 digit day code][1 char month code][2/1 digit year code].
        /// Another test: [sds]sdsd[] 222 [] [abc][].
        /// </summary>
        /// <param name=""someArg"">Test in argument: [sds]sdsd[] 222 [] [abc][]</param>
        /// <returns>Test in returns: [sds]sdsd[] 222 [] [abc][]</returns>
        public int TestMethod(int someArg)
        {
            return someArg;
        }
    }
}"
                    },
                },
                new[]
                {
                    @"
from typing import overload
from enum import IntEnum
import QuantConnect.Namespace
import System


class TestClass(System.Object):
    """"""
    A ticket might be in the following format: <Ticker><2 digit day code><1 char month code><2/1 digit year code>.
    Another test: <sds>sdsd<> 222 <> <abc><>.
    """"""

    @property
    def test_property(self) -> int:
        """"""
        A ticket might be in the following format: <Ticker><2 digit day code><1 char month code><2/1 digit year code>.
        Another test: <sds>sdsd<> 222 <> <abc><>.
        """"""
        ...

    @test_property.setter
    def test_property(self, value: int) -> None:
        ...

    def test_method(self, some_arg: int) -> int:
        """"""
        A ticket might be in the following format: <Ticker><2 digit day code><1 char month code><2/1 digit year code>.
        Another test: <sds>sdsd<> 222 <> <abc><>.

        :param some_arg: Test in argument: <sds>sdsd<> 222 <> <abc><>
        :returns: Test in returns: <sds>sdsd<> 222 <> <abc><>.
        """"""
        ...
",
                }).SetName("BracketsAreReplacedWithAngularBracketsInDocstringsToAvoidMarkdownIssues"),

            // CodeReferencesInDocsAreSnakeCased
            new TestCaseData(
                new Dictionary<string, string>()
                {
                    {
                        "Test1.cs",
                        @"
using QuantConnect.TestNamespace;

namespace QuantConnect.TestNamespace
{
    public class ReferencedClass
    {
        public class InnerClass
        {
            public int TestField = 0;
            public const int TestConstField = 0;
            public static readonly int TestReadonlyField = 0;
            public int TestReadonlyProperty { get; }
            public int TestProperty { get; set; }

            public int TestMethod1(int x, string y)
            {
                return x;
            }
            public int TestMethod2()
            {
                return 0;
            }
        }
    }
}

namespace QuantConnect.Namespace
{
    public class TestClass
    {
        public ReferencedClass ReferencedClassInstance { get; set; }

        public void ReferencedMethod()
        {
        }

        /// <summary>
        /// A method reference: <see cref=""ReferencedMethod""/>.
        /// A param reference: <paramref name=""argName""/>.
        /// A class reference: <see cref=""ReferencedClass""/>.
        /// A nested class reference: <see cref=""ReferencedClass.InnerClass""/>.
        /// A field reference: <see cref=""ReferencedClass.InnerClass.TestField""/>.
        /// A const field reference: <see cref=""ReferencedClass.InnerClass.TestConstField""/>.
        /// A readonly field reference <see cref=""ReferencedClass.InnerClass.TestReadonlyField""/>.
        /// A readonly property reference <see cref=""ReferencedClass.InnerClass.TestReadonlyProperty""/>.
        /// A property reference: <see cref=""ReferencedClass.InnerClass.TestProperty""/>.
        /// A method with args reference: <see cref=""ReferencedClass.InnerClass.TestMethod1(int, string)""/>.
        /// A method without args reference <see cref=""ReferencedClass.InnerClass.TestMethod2""/>.
        /// </summary>
        /// <param name=""argName"">Argument description. Reference in param node <see cref=""ReferencedMethod""/></param>
        /// <returns>Return <paramref name=""argName""/> untouched. Reference in returns node <see cref=""ReferencedMethod""/></returns>
        public int TestMethod(int argName)
        {
            return argName;
        }
    }
}"
                    },
                },
                new[]
                {
                    @"
from typing import overload
from enum import IntEnum
import QuantConnect.TestNamespace
import System


class ReferencedClass(System.Object):
    """"""This class has no documentation.""""""

    class InnerClass(System.Object):
        """"""This class has no documentation.""""""

        @property
        def test_field(self) -> int:
            ...

        @test_field.setter
        def test_field(self, value: int) -> None:
            ...

        TEST_CONST_FIELD: int = 0

        TEST_READONLY_FIELD: int = 0

        @property
        def test_readonly_property(self) -> int:
            ...

        @property
        def test_property(self) -> int:
            ...

        @test_property.setter
        def test_property(self, value: int) -> None:
            ...

        def test_method_1(self, x: int, y: str) -> int:
            ...

        def test_method_2(self) -> int:
            ...
",
                    @"
from typing import overload
from enum import IntEnum
import QuantConnect.Namespace
import QuantConnect.TestNamespace
import System


class TestClass(System.Object):
    """"""This class has no documentation.""""""

    @property
    def referenced_class_instance(self) -> QuantConnect.TestNamespace.ReferencedClass:
        ...

    @referenced_class_instance.setter
    def referenced_class_instance(self, value: QuantConnect.TestNamespace.ReferencedClass) -> None:
        ...

    def referenced_method(self) -> None:
        ...

    def test_method(self, arg_name: int) -> int:
        """"""
        A method reference: referenced_method.
        A param reference: arg_name.
        A class reference: ReferencedClass.
        A nested class reference: ReferencedClass.InnerClass.
        A field reference: ReferencedClass.InnerClass.test_field.
        A const field reference: ReferencedClass.InnerClass.TEST_CONST_FIELD.
        A readonly field reference ReferencedClass.InnerClass.TEST_READONLY_FIELD.
        A readonly property reference ReferencedClass.InnerClass.test_readonly_property.
        A property reference: ReferencedClass.InnerClass.test_property.
        A method with args reference: ReferencedClass.InnerClass.test_method_1(int, string).
        A method without args reference ReferencedClass.InnerClass.test_method_2.

        :param arg_name: Argument description. Reference in param node referenced_method
        :returns: Return arg_name untouched. Reference in returns node referenced_method.
        """"""
        ...
",
                }).SetName("CodeReferencesInDocsAreSnakeCased"),
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


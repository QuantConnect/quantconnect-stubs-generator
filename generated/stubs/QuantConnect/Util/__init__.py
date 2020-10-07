import QuantConnect
import QuantConnect.Interfaces
import QuantConnect.Securities
import abc
import datetime
import typing


IsoDateTimeConverter = typing.Any
JsonConverter = typing.Any
System_Collections_Generic_IEqualityComparer = typing.Any
System_IDisposable = typing.Any
System_Collections_Generic_ISet = typing.Any
System_IO_TextWriter = typing.Any
Color = typing.Any
System_Collections_Generic_Queue = typing.Any


QuantConnect_Util_TypeChangeJsonConverter_T = typing.TypeVar('QuantConnect_Util_TypeChangeJsonConverter_T')
QuantConnect_Util_TypeChangeJsonConverter_TResult = typing.TypeVar('QuantConnect_Util_TypeChangeJsonConverter_TResult')
QuantConnect_Util_BusyCollection_T = typing.TypeVar('QuantConnect_Util_BusyCollection_T')
QuantConnect_Util_ListComparer_T = typing.TypeVar('QuantConnect_Util_ListComparer_T')
QuantConnect_Util_SingleValueListConverter_T = typing.TypeVar('QuantConnect_Util_SingleValueListConverter_T')
QuantConnect_Util_ReferenceWrapper_T = typing.TypeVar('QuantConnect_Util_ReferenceWrapper_T')
QuantConnect_Util_MemoizingEnumerable_T = typing.TypeVar('QuantConnect_Util_MemoizingEnumerable_T')
QuantConnect_Util_CircularQueue_T = typing.TypeVar('QuantConnect_Util_CircularQueue_T')
QuantConnect_Util_BusyBlockingCollection_T = typing.TypeVar('QuantConnect_Util_BusyBlockingCollection_T')
QuantConnect_Util_ConcurrentSet_T = typing.TypeVar('QuantConnect_Util_ConcurrentSet_T')
QuantConnect_Util_FixedSizeQueue_T = typing.TypeVar('QuantConnect_Util_FixedSizeQueue_T')
QuantConnect_Util_NullStringValueConverter_T = typing.TypeVar('QuantConnect_Util_NullStringValueConverter_T')
QuantConnect_Util_FixedSizeHashQueue_T = typing.TypeVar('QuantConnect_Util_FixedSizeHashQueue_T')
QuantConnect_Util_IReadOnlyRef_T = typing.TypeVar('QuantConnect_Util_IReadOnlyRef_T')
QuantConnect_Util_Ref_T = typing.TypeVar('QuantConnect_Util_Ref_T')


class DateTimeJsonConverter(IsoDateTimeConverter):
    """
    Provides a json converter that allows defining the date time format used
    """


class TypeChangeJsonConverter(typing.Generic[QuantConnect_Util_TypeChangeJsonConverter_T, QuantConnect_Util_TypeChangeJsonConverter_TResult], JsonConverter, metaclass=abc.ABCMeta):
    """
    Provides a base class for a JsonConverter that serializes a
    an input type as some other output type
    """


class BusyCollection(typing.Generic[QuantConnect_Util_BusyCollection_T], QuantConnect.Interfaces.IBusyCollection[QuantConnect_Util_BusyCollection_T]):
    """
    A non blocking IBusyCollection{T} implementation
    """


class ListComparer(typing.Generic[QuantConnect_Util_ListComparer_T], System_Collections_Generic_IEqualityComparer):
    """
    An implementation of IEqualityComparer{T} for List{T}.
    Useful when using a List{T} as the key of a collection.
    """


class SingleValueListConverter(typing.Generic[QuantConnect_Util_SingleValueListConverter_T], JsonConverter):
    """
    Reads json and always produces a List, even if the input has just an object
    """


class ReaderWriterLockSlimExtensions:
    """
    Provides extension methods to make working with the ReaderWriterLockSlim class easier
    """


class StreamReaderEnumerable(typing.List[str], System_IDisposable):
    """
    Converts a StreamReader into an enumerable of string
    """


class ReferenceWrapper(typing.Generic[QuantConnect_Util_ReferenceWrapper_T]):
    """
    We wrap a T instance, a value type, with a class, a reference type, to achieve thread safety when assigning new values
    and reading from multiple threads. This is possible because assignments are atomic operations in C# for reference types (among others).
    """


class MemoizingEnumerable(typing.Generic[QuantConnect_Util_MemoizingEnumerable_T], typing.List[QuantConnect_Util_MemoizingEnumerable_T]):
    """
    Defines an enumerable that can be enumerated many times while
    only performing a single enumeration of the root enumerable
    """


class Validate:
    """
    Provides methods for validating strings following a certain format, such as an email address
    """


    class RegularExpression:
        """
        Provides static storage of compiled regular expressions to preclude parsing on each invocation
        """


class RateGate(System_IDisposable):
    """
    Used to control the rate of some occurrence per unit of time.
    """


class CircularQueue(typing.Generic[QuantConnect_Util_CircularQueue_T]):
    """
    A never ending queue that will dequeue and reenqueue the same item
    """


class SeriesJsonConverter(JsonConverter):
    """
    Json Converter for Series which handles special Pie Series serialization case
    """


class ObjectActivator:
    """
    Provides methods for creating new instances of objects
    """


class LinqExtensions:
    """
    Provides more extension methods for the enumerable types
    """


class BusyBlockingCollection(typing.Generic[QuantConnect_Util_BusyBlockingCollection_T], QuantConnect.Interfaces.IBusyCollection[QuantConnect_Util_BusyBlockingCollection_T]):
    """
    A small wrapper around BlockingCollection{T} used to communicate busy state of the items
    being processed
    """


class ExpressionBuilder:
    """
    Provides methods for constructing expressions at runtime
    """


class LeanDataPathComponents:
    """
    Type representing the various pieces of information emebedded into a lean data file path
    """


class ConcurrentSet(typing.Generic[QuantConnect_Util_ConcurrentSet_T], System_Collections_Generic_ISet):
    """
    Provides a thread-safe set collection that mimics the behavior of HashSet{T}
    and will be keep insertion order
    """


class SecurityExtensions:
    """
    Provides useful infrastructure methods to the Security class.
    These are added in this way to avoid mudding the class's public API
    """


class VersionHelper:
    """
    Provides methods for dealing with lean assembly versions
    """


class FuncTextWriter(System_IO_TextWriter):
    """
    Provides an implementation of TextWriter that redirects Write(string) and WriteLine(string)
    """


class ColorJsonConverter(TypeChangeJsonConverter[Color, str]):
    """
    A JsonConverter implementation that serializes a Color as a string.
    If Color is empty, string is also empty and vice-versa. Meaning that color is autogen.
    """


class SecurityIdentifierJsonConverter(TypeChangeJsonConverter[QuantConnect.SecurityIdentifier, str]):
    """
    A JsonConverter implementation that serializes a SecurityIdentifier as a string
    """


class MarketHoursDatabaseJsonConverter(TypeChangeJsonConverter[QuantConnect.Securities.MarketHoursDatabase, MarketHoursDatabaseJsonConverter.MarketHoursDatabaseJson]):
    """
    Provides json conversion for the MarketHoursDatabase class
    """


    class MarketHoursDatabaseJson:
        """
        Defines the json structure of the market-hours-database.json file
        """


    class MarketHoursDatabaseEntryJson:
        """
        Defines the json structure of a single entry in the market-hours-database.json file
        """


class JsonRoundingConverter(JsonConverter):
    """
    Helper JsonConverter that will round decimal and double types,
    to FractionalDigits fractional digits
    """


class StreamReaderExtensions:
    """
    Extension methods to fetch data from a StreamReader instance
    """


class FixedSizeQueue(typing.Generic[QuantConnect_Util_FixedSizeQueue_T], System_Collections_Generic_Queue):
    """
    Helper method for a limited length queue which self-removes the extra elements.
    http://stackoverflow.com/questions/5852863/fixed-size-queue-which-automatically-dequeues-old-values-upon-new-enques
    """


class PythonUtil:
    """
    Collection of utils for python objects processing
    """


class LeanData:
    """
    Provides methods for generating lean data file content
    """


class DoubleUnixSecondsDateTimeJsonConverter(TypeChangeJsonConverter[typing.Optional[datetime.datetime], typing.Optional[float]]):
    """
    Defines a JsonConverter that serializes DateTime use the number of whole and fractional seconds since unix epoch
    """


class DisposableExtensions:
    """
    Provides extensions methods for IDisposable
    """


class NullStringValueConverter(typing.Generic[QuantConnect_Util_NullStringValueConverter_T], JsonConverter):
    """
    Converts the string "null" into a new instance of T.
    This converter only handles deserialization concerns.
    """


class WorkerThread(System_IDisposable):
    """
    This worker tread is required to guarantee all python operations are
    executed by the same thread, to enable complete debugging functionality.
    We don't use the main thread, to avoid any chance of blocking the process
    """


class EnumeratorExtensions:
    """
    Provides convenience of linq extension methods for IEnumerator{T} types
    """


class FixedSizeHashQueue(typing.Generic[QuantConnect_Util_FixedSizeHashQueue_T], typing.List[QuantConnect_Util_FixedSizeHashQueue_T]):
    """
    Provides an implementation of an add-only fixed length, unique queue system
    """


class Composer:
    """
    Provides methods for obtaining exported MEF instances
    """


class IReadOnlyRef(typing.Generic[QuantConnect_Util_IReadOnlyRef_T], metaclass=abc.ABCMeta):
    """
    Represents a read-only reference to any value, T
    """


class Ref(typing.Generic[QuantConnect_Util_Ref_T], IReadOnlyRef[QuantConnect_Util_Ref_T]):
    """
    Represents a reference to any value, T
    """


class XElementExtensions:
    """
    Provides extension methods for the XML to LINQ types
    """



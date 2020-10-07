import QuantConnect.Interfaces
import abc
import enum
import typing


System_IO_TextWriter = typing.Any
System_IEquatable = typing.Any
System_EventArgs = typing.Any
JsonConverter = typing.Any
System_IComparable = typing.Any


QuantConnect_ExtendedDictionary_T = typing.TypeVar('QuantConnect_ExtendedDictionary_T')


class Compression:
    """
    Compression class manages the opening and extraction of compressed files (zip, tar, tar.gz).
    """


class ZipStreamWriter(System_IO_TextWriter):
    """
    Provides an implementation of TextWriter to write to a zip file
    """


class TradingDayType(enum.Enum):
    """
    Enum lists available trading events
    """


class TradingDay:
    """
    Class contains trading events associated with particular day in TradingCalendar
    """


class OS:
    """
    Operating systems class for managing anything that is operation system specific.
    """


class Market:
    """
    Markets Collection: Soon to be expanded to a collection of items specifying the market hour, timezones and country codes.
    """


class SecurityIdentifier(System_IEquatable):
    """
    Defines a unique identifier for securities
    """


class SeriesSampler:
    """
    A type capable of taking a chart and resampling using a linear interpolation strategy
    """


class RealTimeSynchronizedTimer:
    """
    Real time timer class for precise callbacks on a millisecond resolution in a self managed thread.
    """


class SymbolCache:
    """
    Provides a string->Symbol mapping to allow for user defined strings to be lifted into a Symbol
    This is mainly used via the Symbol implicit operator, but also functions that create securities
    should also call Set to add new mappings
    """


    class Cache:
        """
        This class has no documentation.
        """


class TimeZoneOffsetProvider:
    """
    Represents the discontinuties in a single time zone and provides offsets to UTC.
    This type assumes that times will be asked in a forward marching manner.
    This type is not thread safe.
    """


class Time:
    """
    Time helper class collection for working with trading dates
    """


    class DateTimeWithZone:
        """
        Live charting is sensitive to timezone so need to convert the local system time to a UTC and display in browser as UTC.
        """


class ExtendedDictionary(typing.Generic[QuantConnect_ExtendedDictionary_T], QuantConnect.Interfaces.IExtendedDictionary[Symbol, QuantConnect_ExtendedDictionary_T], metaclass=abc.ABCMeta):
    """
    Provides a base class for types holding instances keyed by Symbol
    """


class AlgorithmSettings(QuantConnect.Interfaces.IAlgorithmSettings):
    """
    This class includes user settings for the algorithm which can be changed in the IAlgorithm.Initialize method
    """


class Field:
    """
    Provides static properties to be used as selectors with the indicator system
    """


class SymbolRepresentation:
    """
    Public static helper class that does parsing/generation of symbol representations (options, futures)
    """


    class FutureTickerProperties:
        """
        Class contains future ticker properties returned by ParseFutureTicker()
        """


    class OptionTickerProperties:
        """
        Class contains option ticker properties returned by ParseOptionTickerIQFeed()
        """


class DateFormat:
    """
    Shortcut date format strings
    """


class Holding:
    """
    Singular holding of assets from backend live nodes:
    """


class BrokerageEnvironment(enum.Enum):
    """
    Represents the types of environments supported by brokerages for trading
    """


class Language(enum.Enum):
    """
    Multilanguage support enum: which language is this project for the interop bridge converter.
    """


class UserPlan(enum.Enum):
    """
    User / Algorithm Job Subscription Level
    """


class ServerType(enum.Enum):
    """
    Live server types available through the web IDE. / QC deployment.
    """


class SecurityType(enum.Enum):
    """
    Type of tradable security / underlying asset
    """


class AccountType(enum.Enum):
    """
    Account type: margin or cash
    """


class MarketDataType(enum.Enum):
    """
    Market data style: is the market data a summary (OHLC style) bar, or is it a time-price value.
    """


class DataFeedEndpoint(enum.Enum):
    """
    Datafeed enum options for selecting the source of the datafeed.
    """


class StoragePermissions(enum.Enum):
    """
    Cloud storage permission options.
    """


class TickType(enum.Enum):
    """
    Types of tick data
    """


class DelistingType(enum.Enum):
    """
    Specifies the type of QuantConnect.Data.Market.Delisting data
    """


class SplitType(enum.Enum):
    """
    Specifies the type of QuantConnect.Data.Market.Split data
    """


class Resolution(enum.Enum):
    """
    Resolution of data requested.
    """


class OptionRight(enum.Enum):
    """
    Specifies the different types of options
    """


class OptionStyle(enum.Enum):
    """
    Specifies the style of an option
    """


class SettlementType(enum.Enum):
    """
    Specifies the type of settlement in derivative deals
    """


class AlgorithmControl:
    """
    Wrapper for algorithm status enum to include the charting subscription.
    """


class AlgorithmStatus(enum.Enum):
    """
    States of a live deployment.
    """


class SubscriptionTransportMedium(enum.Enum):
    """
    Specifies where a subscription's data comes from
    """


class Period(enum.Enum):
    """
    enum Period - Enum of all the analysis periods, AS integers. Reference "Period" Array to access the values
    """


class DataNormalizationMode(enum.Enum):
    """
    Specifies how data is normalized before being sent into an algorithm
    """


class MarketCodes:
    """
    Global Market Short Codes and their full versions: (used in tick objects)
    """


class ChannelStatus:
    """
    Defines the different channel status values
    """


class USHoliday:
    """
    US Public Holidays - Not Tradeable:
    """


class Currencies:
    """
    Provides commonly used currency pairs and symbols
    """


class DataProviderEventArgs(System_EventArgs, metaclass=abc.ABCMeta):
    """
    Defines a base class for IDataProviderEvents
    """


class InvalidConfigurationDetectedEventArgs(DataProviderEventArgs):
    """
    Event arguments for the IDataProviderEvents.InvalidConfigurationDetected event
    """


class NumericalPrecisionLimitedEventArgs(DataProviderEventArgs):
    """
    Event arguments for the IDataProviderEvents.NumericalPrecisionLimited event
    """


class DownloadFailedEventArgs(DataProviderEventArgs):
    """
    Event arguments for the IDataProviderEvents.DownloadFailed event
    """


class ReaderErrorDetectedEventArgs(DataProviderEventArgs):
    """
    Event arguments for the IDataProviderEvents.ReaderErrorDetected event
    """


class StartDateLimitedEventArgs(DataProviderEventArgs):
    """
    Event arguments for the IDataProviderEvents.StartDateLimited event
    """


class NewTradableDateEventArgs(DataProviderEventArgs):
    """
    Event arguments for the NewTradableDate event
    """


class IsolatorLimitResultProvider:
    """
    Provides access to the NullIsolatorLimitResultProvider and extension methods supporting ScheduledEvent
    """


class StringExtensions:
    """
    Provides extension methods for properly parsing and serializing values while properly using
    an IFormatProvider/CultureInfo when applicable
    """


class TimeZones:
    """
    Provides access to common time zones
    """


class RealTimeProvider(ITimeProvider):
    """
    Provides an implementation of ITimeProvider that
    uses DateTime.UtcNow to provide the current time
    """


class TimeKeeper(QuantConnect.Interfaces.ITimeKeeper):
    """
    Provides a means of centralizing time for various time zones.
    """


class LocalTimeKeeper:
    """
    Represents the current local time. This object is created via the TimeKeeper to
    manage conversions to local time.
    """


class Isolator:
    """
    Isolator class - create a new instance of the algorithm and ensure it doesn't
    exceed memory or time execution limits.
    """


class Expiry:
    """
    Provides static functions that can be used to compute a future DateTime (expiry) given a DateTime.
    """


class Series:
    """
    Chart Series Object - Series data and properties for a chart:
    """


class SeriesType(enum.Enum):
    """
    Available types of charts
    """


class ScatterMarkerSymbol(enum.Enum):
    """
    Shape or symbol for the marker in a scatter plot
    """


class ITimeProvider(metaclass=abc.ABCMeta):
    """
    Provides access to the current time in UTC. This doesn't necessarily
    need to be wall-clock time, but rather the current time in some system
    """


class ChartPoint:
    """
    Single Chart Point Value Type for QCAlgorithm.Plot();
    """


class Parse:
    """
    Provides methods for parsing strings using CultureInfo.InvariantCulture
    """


class SymbolJsonConverter(JsonConverter):
    """
    Defines a JsonConverter to be used when deserializing to
    the Symbol class.
    """


class IIsolatorLimitResultProvider(metaclass=abc.ABCMeta):
    """
    Provides an abstraction for managing isolator limit results.
    This is originally intended to be used by the training feature to permit a single
    algorithm time loop to extend past the default of ten minutes
    """


class IsolatorLimitResult:
    """
    Represents the result of the Isolator limiter callback
    """


class Extensions:
    """
    Extensions function collections - group all static extensions functions here.
    """


class TimeUpdatedEventArgs(System_EventArgs):
    """
    Event arguments class for the LocalTimeKeeper.TimeUpdated event
    """


class AlphaRuntimeStatistics:
    """
    Contains insight population run time statistics
    """


class Result:
    """
    Base class for backtesting and live results that packages result data.
    LiveResultBacktestResult
    """


class Globals:
    """
    Provides application level constant values
    """


class SymbolValueJsonConverter(JsonConverter):
    """
    Defines a JsonConverter to be used when you only want to serialize
    the Symbol.Value property instead of the full Symbol
    instance
    """


class Symbol(System_IEquatable, System_IComparable):
    """
    Represents a unique security identifier. This is made of two components,
    the unique SID and the Value. The value is the current ticker symbol while
    the SID is constant over the life of a security
    """


class TradingCalendar:
    """
    Class represents trading calendar, populated with variety of events relevant to currently trading instruments
    """


class Chart:
    """
    Single Parent Chart Object for Custom Charting
    """


class ChartType(enum.Enum):
    """
    Type of chart - should we draw the series as overlayed or stacked
    """



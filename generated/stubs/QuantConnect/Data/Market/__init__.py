import QuantConnect
import QuantConnect.Data
import abc
import enum
import typing


QuantConnect_Data_Market_DataDictionary_T = typing.TypeVar('QuantConnect_Data_Market_DataDictionary_T')


class Ticks(DataDictionary[typing.List[Tick]]):
    """
    Ticks collection which implements an IDictionary-string-list of ticks. This way users can iterate over the string indexed ticks of the requested symbol.
    """


class SymbolChangedEvents(DataDictionary[SymbolChangedEvent]):
    """
    Collection of SymbolChangedEvent keyed by the original, requested symbol
    """


class Splits(DataDictionary[Split]):
    """
    Collection of splits keyed by Symbol
    """


class Delistings(DataDictionary[Delisting]):
    """
    Collections of Delisting keyed by Symbol
    """


class IBar(metaclass=abc.ABCMeta):
    """
    Generic bar interface with Open, High, Low and Close.
    """


class Dividends(DataDictionary[Dividend]):
    """
    Collection of dividends keyed by Symbol
    """


class Split(QuantConnect.Data.BaseData):
    """
    Split event from a security
    """


class Tick(QuantConnect.Data.BaseData):
    """
    Tick class is the base representation for tick data. It is grouped into a Ticks object
    which implements IDictionary and passed into an OnData event handler.
    """


class Dividend(QuantConnect.Data.BaseData):
    """
    Dividend event from a security
    """


class RenkoType(enum.Enum):
    """
    The type of the RenkoBar
    """


class FuturesContracts(DataDictionary[FuturesContract]):
    """
    Collection of FuturesContract keyed by futures symbol
    """


class TradeBar(QuantConnect.Data.BaseData, IBaseDataBar):
    """
    TradeBar class for second and minute resolution data:
    An OHLC implementation of the QuantConnect BaseData class with parameters for candles.
    """


class FuturesChain(QuantConnect.Data.BaseData, typing.List[FuturesContract]):
    """
    Represents an entire chain of futures contracts for a single underlying
    This type is IEnumerable{FuturesContract}
    """


class RenkoBar(QuantConnect.Data.BaseData, IBaseDataBar):
    """
    Represents a bar sectioned not by time, but by some amount of movement in a value (for example, Closing price moving in $10 bar sizes)
    """


class BarDirection(enum.Enum):
    """
    This class has no documentation.
    """


class OptionContract:
    """
    Defines a single option contract at a specific expiration and strike price
    """


class QuoteBar(QuantConnect.Data.BaseData, IBaseDataBar):
    """
    QuoteBar class for second and minute resolution data:
    An OHLC implementation of the QuantConnect BaseData class with parameters for candles.
    """


class OptionChain(QuantConnect.Data.BaseData, typing.List[OptionContract]):
    """
    Represents an entire chain of option contracts for a single underying security.
    This type is IEnumerable{OptionContract}
    """


class SymbolChangedEvent(QuantConnect.Data.BaseData):
    """
    Symbol changed event of a security. This is generated when a symbol is remapped for a given
    security, for example, at EOD 2014.04.02 GOOG turned into GOOGL, but are the same
    """


class FuturesChains(DataDictionary[FuturesChain]):
    """
    Collection of FuturesChain keyed by canonical futures symbol
    """


class OpenInterest(Tick):
    """
    Defines a data type that represents open interest for given security
    """


class Delisting(QuantConnect.Data.BaseData):
    """
    Delisting event of a security
    """


class OptionContracts(DataDictionary[OptionContract]):
    """
    Collection of OptionContract keyed by option symbol
    """


class Greeks:
    """
    Defines the greeks
    """


class OptionChains(DataDictionary[OptionChain]):
    """
    Collection of OptionChain keyed by canonical option symbol
    """


class QuoteBars(DataDictionary[QuoteBar]):
    """
    Collection of QuoteBar keyed by symbol
    """


class IBaseDataBar(QuantConnect.Data.IBaseData, IBar, metaclass=abc.ABCMeta):
    """
    Represents a type that is both a bar and base data
    """


class Bar(IBar):
    """
    Base Bar Class: Open, High, Low, Close and Period.
    """


class FuturesContract:
    """
    Defines a single futures contract at a specific expiration
    """


class TradeBars(DataDictionary[TradeBar]):
    """
    Collection of TradeBars to create a data type for generic data handler:
    """


class DataDictionary(typing.Generic[QuantConnect_Data_Market_DataDictionary_T], QuantConnect.ExtendedDictionary[QuantConnect_Data_Market_DataDictionary_T], typing.Dict[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]):
    """
    Provides a base class for types holding base data instances keyed by symbol
    """


class DataDictionaryExtensions:
    """
    Provides extension methods for the DataDictionary class
    """



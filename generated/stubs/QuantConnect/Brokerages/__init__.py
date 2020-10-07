import QuantConnect.Interfaces
import abc
import enum
import typing


System_EventArgs = typing.Any
System_Exception = typing.Any
System_IDisposable = typing.Any
System_Attribute = typing.Any


QuantConnect_Brokerages_IOrderBookUpdater_K = typing.TypeVar('QuantConnect_Brokerages_IOrderBookUpdater_K')
QuantConnect_Brokerages_IOrderBookUpdater_V = typing.TypeVar('QuantConnect_Brokerages_IOrderBookUpdater_V')


class BestBidAskUpdatedEventArgs(System_EventArgs):
    """
    Event arguments class for the DefaultOrderBook.BestBidAskUpdated event
    """


class DefaultOrderBook(IOrderBookUpdater[float, float]):
    """
    Represents a full order book for a security.
    It contains prices and order sizes for each bid and ask level.
    The best bid and ask prices are also kept up to date.
    """


class DefaultConnectionHandler(IConnectionHandler):
    """
    A default implementation of IConnectionHandler
    which signals disconnection if no data is received for a given time span
    and attempts to reconnect automatically.
    """


class IWebSocket(metaclass=abc.ABCMeta):
    """
    Wrapper for WebSocket4Net to enhance testability
    """


class ISymbolMapper(metaclass=abc.ABCMeta):
    """
    Provides the mapping between Lean symbols and brokerage specific symbols.
    """


class BrokerageException(System_Exception):
    """
    Represents an error retuned from a broker's server
    """


class ApiPriceProvider(QuantConnect.Interfaces.IPriceProvider):
    """
    An implementation of IPriceProvider which uses QC API to fetch price data
    """


class IOrderBookUpdater(typing.Generic[QuantConnect_Brokerages_IOrderBookUpdater_K, QuantConnect_Brokerages_IOrderBookUpdater_V], metaclass=abc.ABCMeta):
    """
    Represents an orderbook updater interface for a security.
    Provides the ability to update orderbook price level and to be alerted about updates
    """


class WebSocketMessage:
    """
    Defines a message received at a web socket
    """


class WebSocketClientWrapper(IWebSocket):
    """
    Wrapper for System.Net.Websockets.ClientWebSocket to enhance testability
    """


class BaseWebsocketsBrokerage(Brokerage, metaclass=abc.ABCMeta):
    """
    Provides shared brokerage websockets implementation
    """


class WebSocketCloseData:
    """
    Defines data returned from a web socket close event
    """


class Brokerage(QuantConnect.Interfaces.IBrokerage, metaclass=abc.ABCMeta):
    """
    Represents the base Brokerage implementation. This provides logging on brokerage events.
    """


class BrokerageFactory(QuantConnect.Interfaces.IBrokerageFactory, metaclass=abc.ABCMeta):
    """
    Provides a base implementation of IBrokerageFactory that provides a helper for reading data from a job's brokerage data dictionary
    """


class IConnectionHandler(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Provides handling of a brokerage or data feed connection
    """


class WebSocketError:
    """
    Defines data returned from a web socket error
    """


class BitfinexBrokerageModel(DefaultBrokerageModel):
    """
    Provides Bitfinex specific properties
    """


class IBrokerageMessageHandler(metaclass=abc.ABCMeta):
    """
    Provides an plugin point to allow algorithms to directly handle the messages
    that come from their brokerage
    """


class BrokerageMessageEvent:
    """
    Represents a message received from a brokerage
    """


class DowngradeErrorCodeToWarningBrokerageMessageHandler(IBrokerageMessageHandler):
    """
    Provides an implementation of IBrokerageMessageHandler that converts specified error codes into warnings
    """


class IBrokerageModel(metaclass=abc.ABCMeta):
    """
    Models brokerage transactions, fees, and order
    """


class BrokerageModel:
    """
    Provides factory method for creating an IBrokerageModel from the BrokerageName enum
    """


class AlphaStreamsBrokerageModel(DefaultBrokerageModel):
    """
    Provides properties specific to Alpha Streams
    """


class FxcmBrokerageModel(DefaultBrokerageModel):
    """
    Provides FXCM specific properties
    """


class InteractiveBrokersBrokerageModel(DefaultBrokerageModel):
    """
    Provides properties specific to interactive brokers
    """


class BrokerageMessageType(enum.Enum):
    """
    Specifies the type of message received from an IBrokerage implementation
    """


class BrokerageFactoryAttribute(System_Attribute):
    """
    Represents the brokerage factory type required to load a data queue handler
    """


class GDAXBrokerageModel(DefaultBrokerageModel):
    """
    Provides GDAX specific properties
    """


class AlpacaBrokerageModel(DefaultBrokerageModel):
    """
    Alpaca Brokerage Model Implementation for Back Testing.
    """


class DefaultBrokerageMessageHandler(IBrokerageMessageHandler):
    """
    Provides a default implementation o IBrokerageMessageHandler that will forward
    messages as follows:
    Information -> IResultHandler.Debug
    Warning     -> IResultHandler.Error &amp;&amp; IApi.SendUserEmail
    Error       -> IResultHandler.Error &amp;&amp; IAlgorithm.RunTimeError
    """


class TradierBrokerageModel(DefaultBrokerageModel):
    """
    Provides tradier specific properties
    """


class BrokerageName(enum.Enum):
    """
    Specifices what transaction model and submit/execution rules to use
    """


class DefaultBrokerageModel(IBrokerageModel):
    """
    Provides a default implementation of IBrokerageModel that allows all orders and uses
    the default transaction models
    """


class OandaBrokerageModel(DefaultBrokerageModel):
    """
    Oanda Brokerage Model Implementation for Back Testing.
    """


class BinanceBrokerageModel(DefaultBrokerageModel):
    """
    Provides Binance specific properties
    """



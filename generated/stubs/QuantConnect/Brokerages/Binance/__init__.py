import QuantConnect.Brokerages
import QuantConnect.Interfaces
import typing


System_IDisposable = typing.Any


class BinanceBrokerageFactory(QuantConnect.Brokerages.BrokerageFactory):
    """
    Factory method to create binance Websockets brokerage
    """


class BinanceSymbolMapper(QuantConnect.Brokerages.ISymbolMapper):
    """
    Provides the mapping between Lean symbols and Binance symbols.
    """


class BinanceWebSocketWrapper(QuantConnect.Brokerages.WebSocketClientWrapper):
    """
    Wrapper class for a Binance websocket connection
    """


class BinanceOrderSubmitEventArgs:
    """
    Represents a binance submit order event data
    """


class BinanceBrokerage(QuantConnect.Brokerages.BaseWebsocketsBrokerage, QuantConnect.Interfaces.IDataQueueHandler):
    """
    Binance brokerage implementation
    """


class BinanceRestApiClient(System_IDisposable):
    """
    Binance REST API implementation
    """


class BinanceUtil:
    """
    Binance utility methods
    """



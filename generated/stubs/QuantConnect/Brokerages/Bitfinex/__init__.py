import QuantConnect.Brokerages
import QuantConnect.Data
import QuantConnect.Interfaces


class BitfinexWebSocketWrapper(QuantConnect.Brokerages.WebSocketClientWrapper):
    """
    Wrapper class for a Bitfinex websocket connection
    """


class BitfinexBrokerage(QuantConnect.Brokerages.BaseWebsocketsBrokerage, QuantConnect.Interfaces.IDataQueueHandler):
    """
    Bitfinex Brokerage implementation
    """


class BitfinexSymbolMapper(QuantConnect.Brokerages.ISymbolMapper):
    """
    Provides the mapping between Lean symbols and Bitfinex symbols.
    """


class BitfinexSubscriptionManager(QuantConnect.Data.DataQueueHandlerSubscriptionManager):
    """
    Handles Bitfinex data subscriptions with multiple websocket connections
    """


class BitfinexBrokerageFactory(QuantConnect.Brokerages.BrokerageFactory):
    """
    Factory method to create Bitfinex Websockets brokerage
    """



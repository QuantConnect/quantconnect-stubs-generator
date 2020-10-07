import QuantConnect.Brokerages
import QuantConnect.Interfaces


class InteractiveBrokersAccountData:
    """
    This class contains account specific data such as properties, cash balances and holdings
    """


class HistoricalDataType:
    """
    Historical Data Request Return Types
    """


class InteractiveBrokersBrokerageFactory(QuantConnect.Brokerages.BrokerageFactory):
    """
    Factory type for the InteractiveBrokersBrokerage
    """


class InteractiveBrokersSymbolMapper(QuantConnect.Brokerages.ISymbolMapper):
    """
    Provides the mapping between Lean symbols and InteractiveBrokers symbols.
    """


class InteractiveBrokersBrokerage(QuantConnect.Brokerages.Brokerage, QuantConnect.Interfaces.IDataQueueHandler, QuantConnect.Interfaces.IDataQueueUniverseProvider):
    """
    The Interactive Brokers brokerage
    """


class InteractiveBrokersStateManager:
    """
    Holds the brokerage state information (connection status, error conditions, etc.)
    """



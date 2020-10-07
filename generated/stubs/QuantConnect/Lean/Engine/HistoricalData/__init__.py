import QuantConnect.Data
import abc


class SubscriptionDataReaderHistoryProvider(SynchronizingHistoryProvider):
    """
    Provides an implementation of IHistoryProvider that uses BaseData
    instances to retrieve historical data
    """


class SynchronizingHistoryProvider(QuantConnect.Data.HistoryProviderBase, metaclass=abc.ABCMeta):
    """
    Provides an abstract implementation of IHistoryProvider
    which provides synchronization of multiple history results
    """


class SineHistoryProvider(QuantConnect.Data.HistoryProviderBase):
    """
    Implements a History provider that always return a IEnumerable of Slice with prices following a sine function
    """


class BrokerageHistoryProvider(SynchronizingHistoryProvider):
    """
    Provides an implementation of IHistoryProvider that relies on
    a brokerage connection to retrieve historical data
    """



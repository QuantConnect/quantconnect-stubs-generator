import QuantConnect.Brokerages
import QuantConnect.Interfaces
import typing


IGenericMessageListener = typing.Any
IStatusMessageListener = typing.Any


class FxcmBrokerage(QuantConnect.Brokerages.Brokerage, QuantConnect.Interfaces.IDataQueueHandler, IGenericMessageListener, IStatusMessageListener):
    """
    FXCM brokerage - implementation of IDataQueueHandler interface
    """


class FxcmBrokerageFactory(QuantConnect.Brokerages.BrokerageFactory):
    """
    Provides an implementation of IBrokerageFactory that produces a FxcmBrokerage
    """


class FxcmSymbolMapper(QuantConnect.Brokerages.ISymbolMapper):
    """
    Provides the mapping between Lean symbols and FXCM symbols.
    """



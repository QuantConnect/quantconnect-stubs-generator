import QuantConnect.Brokerages
import QuantConnect.Interfaces
import abc
import enum


class OandaBrokerageFactory(QuantConnect.Brokerages.BrokerageFactory):
    """
    Provides an implementations of IBrokerageFactory that produces a OandaBrokerage
    """


class Environment(enum.Enum):
    """
    Represents different environments available for the REST API.
    """


class Server(enum.Enum):
    """
    Represents the server instance that we will be performing the RESTful call.
    """


class OandaBrokerage(QuantConnect.Brokerages.Brokerage, QuantConnect.Interfaces.IDataQueueHandler):
    """
    Oanda Brokerage implementation
    """


class OandaRestApiV20(OandaRestApiBase):
    """
    Oanda REST API v20 implementation
    """


class OandaRestApiBase(QuantConnect.Brokerages.Brokerage, QuantConnect.Interfaces.IDataQueueHandler, metaclass=abc.ABCMeta):
    """
    Oanda REST API base class
    """


class OandaSymbolMapper(QuantConnect.Brokerages.ISymbolMapper):
    """
    Provides the mapping between Lean symbols and Oanda symbols.
    """


class OandaRestApiV1(OandaRestApiBase):
    """
    Oanda REST API v1 implementation
    """



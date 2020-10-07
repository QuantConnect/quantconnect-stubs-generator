import QuantConnect.Brokerages
import QuantConnect.Interfaces
import enum


class GDAXDataQueueHandler(GDAXBrokerage, QuantConnect.Interfaces.IDataQueueHandler):
    """
    An implementation of IDataQueueHandler for GDAX
    """


class GDAXBrokerageFactory(QuantConnect.Brokerages.BrokerageFactory):
    """
    Factory method to create GDAX Websockets brokerage
    """


class GDAXFill:
    """
    Tracks fill messages
    """


class GDAXBrokerage(QuantConnect.Brokerages.BaseWebsocketsBrokerage):
    """
    This class has no documentation.
    """


    class GdaxEndpointType(enum.Enum):
        """
        This class has no documentation.
        """


class AuthenticationToken:
    """
    Contains data used for authentication
    """



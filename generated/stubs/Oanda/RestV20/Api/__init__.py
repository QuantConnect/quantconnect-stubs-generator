import Oanda.RestV20.Client
import abc


class DefaultApi(IDefaultApi):
    """
    This class has no documentation.
    """


class IDefaultApi(Oanda.RestV20.Client.IApiAccessor, metaclass=abc.ABCMeta):
    """
    Represents a collection of functions to interact with the API endpoints
    """



import abc
import typing


System_Exception = typing.Any


Oanda_RestV20_Client_ApiResponse_T = typing.TypeVar('Oanda_RestV20_Client_ApiResponse_T')


class ApiException(System_Exception):
    """
    API Exception
    """


class ApiClient:
    """
    API client is mainly responsible for making the HTTP call to the API backend.
    """


class ApiResponse(typing.Generic[Oanda_RestV20_Client_ApiResponse_T]):
    """
    API Response
    """


class IApiAccessor(metaclass=abc.ABCMeta):
    """
    Represents configuration aspects required to interact with the API endpoints.
    """


class Configuration:
    """
    Represents a set of configuration settings
    """



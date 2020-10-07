import abc
import enum
import typing


QuantConnect_Brokerages_Oanda_RestV1_DataType_Communications_Requests_SmartProperty_T = typing.TypeVar('QuantConnect_Brokerages_Oanda_RestV1_DataType_Communications_Requests_SmartProperty_T')


class CandlesRequest(Request):
    """
    This class has no documentation.
    """


class ECandleFormat(enum.Enum):
    """
    This class has no documentation.
    """


class EGranularity(enum.Enum):
    """
    This class has no documentation.
    """


class ISmartProperty(metaclass=abc.ABCMeta):
    """
    This class has no documentation.
    """


class SmartProperty(typing.Generic[QuantConnect_Brokerages_Oanda_RestV1_DataType_Communications_Requests_SmartProperty_T], ISmartProperty):
    """
    This class has no documentation.
    """


class Request(metaclass=abc.ABCMeta):
    """
    This class has no documentation.
    """



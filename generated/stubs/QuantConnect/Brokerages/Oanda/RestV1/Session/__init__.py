import QuantConnect.Brokerages.Oanda.RestV1.DataType
import QuantConnect.Brokerages.Oanda.RestV1.DataType.Communications
import abc
import typing


QuantConnect_Brokerages_Oanda_RestV1_Session_StreamSession_T = typing.TypeVar('QuantConnect_Brokerages_Oanda_RestV1_Session_StreamSession_T')


class RatesSession(StreamSession[QuantConnect.Brokerages.Oanda.RestV1.DataType.Communications.RateStreamResponse]):
    """
    This class has no documentation.
    """


class EventsSession(StreamSession[QuantConnect.Brokerages.Oanda.RestV1.DataType.Event]):
    """
    This class has no documentation.
    """


class StreamSession(typing.Generic[QuantConnect_Brokerages_Oanda_RestV1_Session_StreamSession_T], metaclass=abc.ABCMeta):
    """
    This class has no documentation.
    """



import QuantConnect.Brokerages.Oanda.RestV1.DataType.Communications
import abc
import enum
import typing


System_Attribute = typing.Any


class Position:
    """
    This class has no documentation.
    """


class IHeartbeat(metaclass=abc.ABCMeta):
    """
    This class has no documentation.
    """


class Order(QuantConnect.Brokerages.Oanda.RestV1.DataType.Communications.Response):
    """
    This class has no documentation.
    """


class Transaction(QuantConnect.Brokerages.Oanda.RestV1.DataType.Communications.Response):
    """
    This class has no documentation.
    """


class IsOptionalAttribute(System_Attribute):
    """
    This class has no documentation.
    """


class MaxValueAttribute(System_Attribute):
    """
    Represents maximum value of a property.
    """


class MinValueAttribute(System_Attribute):
    """
    Represents minimum value of a property.
    """


class Instrument:
    """
    Represents a financial instrument / product provided by Oanda.
    """


class Candle:
    """
    This class has no documentation.
    """


class Price:
    """
    This class has no documentation.
    """


    class State(enum.Enum):
        """
        This class has no documentation.
        """


class TradeData(QuantConnect.Brokerages.Oanda.RestV1.DataType.Communications.Response):
    """
    This class has no documentation.
    """


class Heartbeat:
    """
    This class has no documentation.
    """


class Event(IHeartbeat):
    """
    This class has no documentation.
    """


class Account:
    """
    This class has no documentation.
    """



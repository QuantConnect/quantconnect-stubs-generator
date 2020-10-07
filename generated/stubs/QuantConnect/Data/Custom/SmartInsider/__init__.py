import QuantConnect.Data
import abc
import enum


class SmartInsiderEvent(QuantConnect.Data.BaseData, metaclass=abc.ABCMeta):
    """
    SmartInsider Intention and Transaction events. These are fields
    that are shared between intentions and transactions.
    """


class SmartInsiderExecutionEntity(enum.Enum):
    """
    Entity that intends to or executed the transaction
    """


class SmartInsiderEventType(enum.Enum):
    """
    Describes what will or has taken place in an execution
    """


class SmartInsiderIntention(SmartInsiderEvent):
    """
    Smart Insider Intentions - Intention to execute a stock buyback and details about the future event
    """


class SmartInsiderExecutionHolding(enum.Enum):
    """
    Details regarding the way holdings will be or were processed in a buyback execution
    """


class SmartInsiderExecution(enum.Enum):
    """
    Describes how the transaction was executed
    """


class SmartInsiderTransaction(SmartInsiderEvent):
    """
    Smart Insider Transaction - Execution of a stock buyback and details about the event occurred
    """



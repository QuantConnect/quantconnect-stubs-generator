import abc
import enum


class AdjustmentType(enum.Enum):
    """
    Enum defines types of possible price adjustments in continuous contract modeling.
    """


class IContinuousContractModel(metaclass=abc.ABCMeta):
    """
    Continuous contract model interface. Interfaces is implemented by different classes
    realizing various methods for modeling continuous security series. Primarily, modeling of continuous futures.
    Continuous contracts are used in backtesting of otherwise expiring derivative contracts.
    Continuous contracts are not traded, and are not products traded on exchanges.
    """


class ISecurityDataFilter(metaclass=abc.ABCMeta):
    """
    Security data filter interface. Defines pattern for the user defined data filter techniques.
    """



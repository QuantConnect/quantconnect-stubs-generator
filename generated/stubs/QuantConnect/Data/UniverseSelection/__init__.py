import QuantConnect
import QuantConnect.Data
import abc
import typing


System_IDisposable = typing.Any
INotifyCollectionChanged = typing.Any


class FuncUniverse(Universe):
    """
    Provides a functional implementation of Universe
    """


class CoarseFundamental(QuantConnect.Data.BaseData):
    """
    Defines summary information about a single symbol for a given date
    """


class ConstituentsUniverseData(QuantConnect.Data.BaseData):
    """
    Custom base data class used for ConstituentsUniverse
    """


class FineFundamentalUniverse(Universe):
    """
    Defines a universe that reads fine us equity data
    """


class UniverseDecorator(Universe, metaclass=abc.ABCMeta):
    """
    Provides an implementation of UniverseSelection.Universe that redirects all calls to a
    wrapped (or decorated) universe. This provides scaffolding for other decorators who
    only need to override one or two methods.
    """


class ScheduledUniverse(Universe, ITimeTriggeredUniverse):
    """
    Defines a user that is fired based on a specified IDateRule and ITimeRule
    """


class UniversePythonWrapper(Universe):
    """
    Provides an implementation of Universe that wraps a PyObject object
    """


class CoarseFundamentalUniverse(Universe):
    """
    Defines a universe that reads coarse us equity data
    """


class SubscriptionRequest:
    """
    Defines the parameters required to add a subscription to a data feed.
    """


class UniverseExtensions:
    """
    Provides extension methods for the Universe class
    """


class ConstituentsUniverse(FuncUniverse):
    """
    ConstituentsUniverse allows to perform universe selection based on an
    already preselected set of Symbol.
    """


class BaseDataCollection(QuantConnect.Data.BaseData):
    """
    This type exists for transport of data as a single packet
    """


class FineFundamentalFilteredUniverse(SelectSymbolsUniverseDecorator):
    """
    Provides a universe that can be filtered with a FineFundamental selection function
    """


class SelectSymbolsUniverseDecorator(UniverseDecorator):
    """
    Provides a univese decoration that replaces the implementation of SelectSymbols
    """


class OptionChainUniverse(Universe):
    """
    Defines a universe for a single option chain
    """


class Universe(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Provides a base class for all universes to derive from.
    """


    class UnchangedUniverse(typing.List[str], typing.List[QuantConnect.Symbol]):
        """
        Provides a value to indicate that no changes should be made to the universe.
        This value is intended to be returned by reference via Universe.SelectSymbols
        """


    class Member:
        """
        This class has no documentation.
        """


class FuturesChainUniverseDataCollection(BaseDataCollection):
    """
    Defines the universe selection data type for FuturesChainUniverse
    """


class ITimeTriggeredUniverse(metaclass=abc.ABCMeta):
    """
    A universe implementing this interface will NOT use it's SubscriptionDataConfig to generate data
    that is used to 'pulse' the universe selection function -- instead, the times output by
    GetTriggerTimes are used to 'pulse' the universe selection function WITHOUT data.
    """


class GetSubscriptionRequestsUniverseDecorator(UniverseDecorator):
    """
    Provides a universe decoration that replaces the implementation of GetSubscriptionRequests
    """


class SecurityChanges:
    """
    Defines the additions and subtractions to the algorithm's security subscriptions
    """


class FuturesChainUniverse(Universe):
    """
    Defines a universe for a single futures chain
    """


class OptionChainUniverseDataCollection(BaseDataCollection):
    """
    Defines the universe selection data type for OptionChainUniverse
    """


class UniverseSettings:
    """
    Defines settings required when adding a subscription
    """


class UserDefinedUniverse(Universe, INotifyCollectionChanged, ITimeTriggeredUniverse):
    """
    Represents the universe defined by the user's algorithm. This is
    the default universe where manually added securities live by
    market/security type. They can also be manually generated and
    can be configured to fire on certain interval and will always
    return the internal list of symbols.
    """



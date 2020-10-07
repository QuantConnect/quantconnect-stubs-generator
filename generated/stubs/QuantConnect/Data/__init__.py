import QuantConnect
import QuantConnect.Interfaces
import abc
import enum
import typing


System_IEquatable = typing.Any
IDynamicMetaObjectProvider = typing.Any
System_IDisposable = typing.Any
System_Collections_Generic_KeyValuePair = typing.Any
DynamicMetaObject = typing.Any


class SubscriptionDataConfigList(typing.List[SubscriptionDataConfig]):
    """
    Provides convenient methods for holding several SubscriptionDataConfig
    """


class SubscriptionDataConfig(System_IEquatable):
    """
    Subscription data required including the type of data.
    """


class EventBasedDataQueueHandlerSubscriptionManager(DataQueueHandlerSubscriptionManager):
    """
    Overrides DataQueueHandlerSubscriptionManager methods using events
    """


class DynamicData(BaseData, IDynamicMetaObjectProvider, metaclass=abc.ABCMeta):
    """
    Dynamic Data Class: Accept flexible data, adapting to the columns provided by source.
    """


class SliceExtensions:
    """
    Provides extension methods to slice enumerables
    """


class IBaseData(metaclass=abc.ABCMeta):
    """
    Base Data Class: Type, Timestamp, Key -- Base Features.
    """


class HistoryRequestFactory:
    """
    Helper class used to create new HistoryRequest
    """


class SubscriptionDataSource(System_IEquatable):
    """
    Represents the source location and transport medium for a subscription
    """


class IDataAggregator(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Aggregates ticks and bars based on given subscriptions.
    """


class Slice(QuantConnect.ExtendedDictionary[typing.Any], typing.List[System_Collections_Generic_KeyValuePair]):
    """
    Provides a data structure for all of an algorithm's data at a single time step
    """


class FileFormat(enum.Enum):
    """
    Specifies the format of data in a subscription
    """


class SubscriptionManager:
    """
    Enumerable Subscription Management Class
    """


class HistoryRequest:
    """
    Represents a request for historical data
    """


class DataQueueHandlerSubscriptionManager(metaclass=abc.ABCMeta):
    """
    Count number of subscribers for each channel (Symbol, Socket) pair
    """


class GetSetPropertyDynamicMetaObject(DynamicMetaObject):
    """
    Provides an implementation of DynamicMetaObject that uses get/set methods to update
    values in the dynamic object.
    """


class BaseData(IBaseData, metaclass=abc.ABCMeta):
    """
    Abstract base data class of QuantConnect. It is intended to be extended to define
    generic user customizable data types while at the same time implementing the basics of data where possible
    """


class IndexedBaseData(BaseData, metaclass=abc.ABCMeta):
    """
    Abstract indexed base data class of QuantConnect.
    It is intended to be extended to define customizable data types which are stored
    using an intermediate index source
    """


class HistoryProviderBase(QuantConnect.Interfaces.IHistoryProvider, metaclass=abc.ABCMeta):
    """
    Provides a base type for all history providers
    """


class SubscriptionDataConfigExtensions:
    """
    Helper methods used to determine different configurations properties
    for a given set of SubscriptionDataConfig
    """


class ISubscriptionEnumeratorFactory(metaclass=abc.ABCMeta):
    """
    Create an IEnumerator{BaseData}
    """


class Channel:
    """
    Represents a subscription channel
    """


class HistoryProviderInitializeParameters:
    """
    Represents the set of parameters for the IHistoryProvider.Initialize method
    """



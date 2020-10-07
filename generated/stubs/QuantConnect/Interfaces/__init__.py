import abc
import typing


System_IDisposable = typing.Any
System_Collections_Generic_KeyValuePair = typing.Any
System_EventArgs = typing.Any


QuantConnect_Interfaces_IExtendedDictionary_TKey = typing.TypeVar('QuantConnect_Interfaces_IExtendedDictionary_TKey')
QuantConnect_Interfaces_IExtendedDictionary_TValue = typing.TypeVar('QuantConnect_Interfaces_IExtendedDictionary_TValue')
QuantConnect_Interfaces_IBusyCollection_T = typing.TypeVar('QuantConnect_Interfaces_IBusyCollection_T')


class IExtendedDictionary(typing.Generic[QuantConnect_Interfaces_IExtendedDictionary_TKey, QuantConnect_Interfaces_IExtendedDictionary_TValue], metaclass=abc.ABCMeta):
    """
    Represents a generic collection of key/value pairs that implements python dictionary methods.
    """


class IBrokerageFactory(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Defines factory types for brokerages. Every IBrokerage is expected to also implement an IBrokerageFactory.
    """


class ISecurityInitializerProvider(metaclass=abc.ABCMeta):
    """
    Reduced interface which provides an instance which implements ISecurityInitializer
    """


class IBrokerage(IBrokerageCashSynchronizer, System_IDisposable, metaclass=abc.ABCMeta):
    """
    Brokerage interface that defines the operations all brokerages must implement. The IBrokerage implementation
    must have a matching IBrokerageFactory implementation.
    """


class IOptionChainProvider(metaclass=abc.ABCMeta):
    """
    Provides the full option chain for a given underlying.
    """


class IObjectStore(System_IDisposable, typing.List[System_Collections_Generic_KeyValuePair], metaclass=abc.ABCMeta):
    """
    Provides object storage for data persistence.
    """


class ISecurityPrice(metaclass=abc.ABCMeta):
    """
    Reduced interface which allows setting and accessing
    price properties for a Security
    """


class ITimeInForceHandler(metaclass=abc.ABCMeta):
    """
    Handles the time in force for an order
    """


class IOptionPrice(ISecurityPrice, metaclass=abc.ABCMeta):
    """
    Reduced interface for accessing Option
    specific price properties and methods
    """


class IMapFileProvider(metaclass=abc.ABCMeta):
    """
    Provides instances of MapFileResolver at run time
    """


class IMessagingHandler(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Messaging System Plugin Interface.
    Provides a common messaging pattern between desktop and cloud implementations of QuantConnect.
    """


class IPriceProvider(metaclass=abc.ABCMeta):
    """
    Provides access to price data for a given asset
    """


class IDataQueueUniverseProvider(metaclass=abc.ABCMeta):
    """
    This interface allows interested parties to lookup or enumerate the available symbols. Data source exposes it if this feature is available.
    Availability of a symbol doesn't imply that it is possible to trade it. This is a data source specific interface, not broker specific.
    """


class IFactorFileProvider(metaclass=abc.ABCMeta):
    """
    Provides instances of FactorFile at run time
    """


class ObjectStoreErrorRaisedEventArgs(System_EventArgs):
    """
    Event arguments for the IObjectStore.ErrorRaised event
    """


class IFutureChainProvider(metaclass=abc.ABCMeta):
    """
    Provides the full future chain for a given underlying.
    """


class ISubscriptionDataConfigProvider(metaclass=abc.ABCMeta):
    """
    Reduced interface which provides access to registered SubscriptionDataConfig
    """


class IAlgorithm(ISecurityInitializerProvider, IAccountCurrencyProvider, metaclass=abc.ABCMeta):
    """
    Interface for QuantConnect algorithm implementations. All algorithms must implement these
    basic members to allow interaction with the Lean Backtesting Engine.
    """


class ITimeKeeper(metaclass=abc.ABCMeta):
    """
    Interface implemented by TimeKeeper
    """


class IDataChannelProvider(metaclass=abc.ABCMeta):
    """
    Specifies data channel settings
    """


class IAlgorithmSubscriptionManager(ISubscriptionDataConfigService, metaclass=abc.ABCMeta):
    """
    AlgorithmSubscriptionManager interface will manage the subscriptions for the SubscriptionManager
    """


class IDataCacheProvider(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Defines a cache for data
    """


class ISubscriptionDataConfigService(ISubscriptionDataConfigProvider, metaclass=abc.ABCMeta):
    """
    This interface exposes methods for creating a list of SubscriptionDataConfig for a given
    configuration
    """


class IJobQueueHandler(metaclass=abc.ABCMeta):
    """
    Task requestor interface with cloud system
    """


class IApi(System_IDisposable, metaclass=abc.ABCMeta):
    """
    API for QuantConnect.com
    """


class IRegressionAlgorithmDefinition(metaclass=abc.ABCMeta):
    """
    Defines a C# algorithm as a regression algorithm to be run as part of the test suite.
    This interface also allows the algorithm to declare that it has versions in other languages
    that should yield identical results.
    """


class IHistoryProvider(IDataProviderEvents, metaclass=abc.ABCMeta):
    """
    Provides historical data to an algorithm at runtime
    """


class IDataQueueHandler(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Task requestor interface with cloud system
    """


class ISecurityService(metaclass=abc.ABCMeta):
    """
    This interface exposes methods for creating a new Security
    """


class IDataProvider(metaclass=abc.ABCMeta):
    """
    Fetches a remote file for a security.
    Must save the file to Globals.DataFolder.
    """


class IBrokerageCashSynchronizer(metaclass=abc.ABCMeta):
    """
    Defines live brokerage cash synchronization operations.
    """


class IAccountCurrencyProvider(metaclass=abc.ABCMeta):
    """
    A reduced interface for an account currency provider
    """


class IOrderProperties(metaclass=abc.ABCMeta):
    """
    Contains additional properties and settings for an order
    """


class IBusyCollection(typing.Generic[QuantConnect_Interfaces_IBusyCollection_T], System_IDisposable, metaclass=abc.ABCMeta):
    """
    Interface used to handle items being processed and communicate busy state
    """


class IStreamReader(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Defines a transport mechanism for data from its source into various reader methods
    """


class IDataPermissionManager(metaclass=abc.ABCMeta):
    """
    Entity in charge of handling data permissions
    """


class ITradeBuilder(metaclass=abc.ABCMeta):
    """
    Generates trades from executions and market price updates
    """


class IAlgorithmSettings(metaclass=abc.ABCMeta):
    """
    User settings for the algorithm which can be changed in the IAlgorithm.Initialize method
    """


class IDownloadProvider(metaclass=abc.ABCMeta):
    """
    Wrapper on the API for downloading data for an algorithm.
    """


class IDataProviderEvents(metaclass=abc.ABCMeta):
    """
    Events related to data providers
    """



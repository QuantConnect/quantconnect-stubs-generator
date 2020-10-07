import QuantConnect
import QuantConnect.Data
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds.Enumerators
import abc
import typing


System_Collections_Generic_IEnumerator = typing.Any
System_IDisposable = typing.Any
System_EventArgs = typing.Any


QuantConnect_Lean_Engine_DataFeeds_UpdateData_T = typing.TypeVar('QuantConnect_Lean_Engine_DataFeeds_UpdateData_T')


class LiveFutureChainProvider(QuantConnect.Interfaces.IFutureChainProvider):
    """
    An implementation of IFutureChainProvider that fetches the list of contracts
    from an external source
    """


class IDataManager(metaclass=abc.ABCMeta):
    """
    IDataManager is the engines view of the Data Manager.
    """


class SubscriptionFrontierTimeProvider(QuantConnect.ITimeProvider):
    """
    A time provider which updates 'now' time based on the current data emit time of all subscriptions
    """


class ZipEntryNameSubscriptionDataSourceReader(ISubscriptionDataSourceReader):
    """
    Provides an implementation of ISubscriptionDataSourceReader that reads zip entry names
    """


class ISubscriptionDataSourceReader(metaclass=abc.ABCMeta):
    """
    Represents a type responsible for accepting an input SubscriptionDataSource
    and returning an enumerable of the source's BaseData
    """


class UniverseSelection:
    """
    Provides methods for apply the results of universe selection to an algorithm
    """


class SubscriptionCollection(typing.List[Subscription]):
    """
    Provides a collection for holding subscriptions.
    """


class BacktestingFutureChainProvider(QuantConnect.Interfaces.IFutureChainProvider):
    """
    An implementation of IFutureChainProvider that reads the list of contracts from open interest zip data files
    """


class LiveOptionChainProvider(QuantConnect.Interfaces.IOptionChainProvider):
    """
    An implementation of IOptionChainProvider that fetches the list of contracts
    from the Options Clearing Corporation (OCC) website
    """


class DataChannelProvider(QuantConnect.Interfaces.IDataChannelProvider):
    """
    Specifies data channel settings
    """


class ApiDataProvider(QuantConnect.Interfaces.IDataProvider):
    """
    An instance of the IDataProvider that will attempt to retrieve files not present on the filesystem from the API
    """


class Subscription(System_Collections_Generic_IEnumerator):
    """
    Represents the data required for a data feed to process a single subscription
    """


class ZipDataCacheProvider(QuantConnect.Interfaces.IDataCacheProvider):
    """
    File provider implements optimized zip archives caching facility. Cache is thread safe.
    """


class CachingFutureChainProvider(QuantConnect.Interfaces.IFutureChainProvider):
    """
    An implementation of IFutureChainProvider that will cache by date future contracts returned by another future chain provider.
    """


class BaseSubscriptionDataSourceReader(ISubscriptionDataSourceReader, metaclass=abc.ABCMeta):
    """
    A base class for implementations of the ISubscriptionDataSourceReader
    """


class RealTimeScheduleEventService(System_IDisposable):
    """
    Allows to setup a real time scheduled event, internally using a Timer,
    that is guaranteed to trigger at or after the requested time, never before.
    """


class DefaultDataProvider(QuantConnect.Interfaces.IDataProvider, System_IDisposable):
    """
    Default file provider functionality that does not attempt to retrieve any data
    """


class IDataFeedTimeProvider(metaclass=abc.ABCMeta):
    """
    Reduced interface which exposes required ITimeProvider for IDataFeed implementations
    """


class CreateStreamReaderErrorEventArgs(System_EventArgs):
    """
    Event arguments for the TextSubscriptionDataSourceReader.CreateStreamReader event
    """


class IndexSubscriptionDataSourceReader(BaseSubscriptionDataSourceReader):
    """
    This ISubscriptionDataSourceReader implementation supports
    the FileFormat.Index and IndexedBaseData types.
    Handles the layer of indirection for the index data source and forwards
    the target source to the corresponding ISubscriptionDataSourceReader
    """


class ManualTimeProvider(QuantConnect.ITimeProvider):
    """
    Provides an implementation of ITimeProvider that can be
    manually advanced through time
    """


class IDataFeedSubscriptionManager(metaclass=abc.ABCMeta):
    """
    DataFeedSubscriptionManager interface will manage the subscriptions for the Data Feed
    """


class CachingOptionChainProvider(QuantConnect.Interfaces.IOptionChainProvider):
    """
    An implementation of IOptionChainProvider that will cache by date option contracts returned by another option chain provider.
    """


class SubscriptionUtils:
    """
    Utilities related to data Subscription
    """


class PendingRemovalsManager:
    """
    Helper class used to managed pending security removals UniverseSelection
    """


    class RemovedMember:
        """
        Helper class used to report removed universe members
        """


class InternalSubscriptionManager:
    """
    Class in charge of handling Leans internal subscriptions
    """


class SingleEntryDataCacheProvider(QuantConnect.Interfaces.IDataCacheProvider):
    """
    Default implementation of the IDataCacheProvider
    Does not cache data.  If the data is a zip, the first entry is returned
    """


class ISubscriptionSynchronizer(metaclass=abc.ABCMeta):
    """
    Provides the ability to synchronize subscriptions into time slices
    """


class SubscriptionDataReader(System_Collections_Generic_IEnumerator, QuantConnect.Lean.Engine.DataFeeds.Enumerators.ITradableDatesNotifier, QuantConnect.Interfaces.IDataProviderEvents):
    """
    Subscription data reader is a wrapper on the stream reader class to download, unpack and iterate over a data file.
    """


class BacktestingOptionChainProvider(QuantConnect.Interfaces.IOptionChainProvider):
    """
    An implementation of IOptionChainProvider that reads the list of contracts from open interest zip data files
    """


class TextSubscriptionDataSourceReader(BaseSubscriptionDataSourceReader):
    """
    Provides an implementations of ISubscriptionDataSourceReader that uses the
    BaseData.Reader(SubscriptionDataConfig,string,DateTime,bool)
    method to read lines of text from a SubscriptionDataSource
    """


class IDataFeed(metaclass=abc.ABCMeta):
    """
    Datafeed interface for creating custom datafeed sources.
    """


class NullDataFeed(IDataFeed):
    """
    Null data feed implementation.
    """


class Synchronizer(ISynchronizer, IDataFeedTimeProvider, System_IDisposable):
    """
    Implementation of the ISynchronizer interface which provides the mechanism to stream data to the algorithm
    """


class ISynchronizer(metaclass=abc.ABCMeta):
    """
    Interface which provides the data to stream to the algorithm
    """


class TimeSlice:
    """
    Represents a grouping of data emitted at a certain time.
    """


class SubscriptionData:
    """
    Store data (either raw or adjusted) and the time at which it should be synchronized
    """


class UpdateData(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_UpdateData_T]):
    """
    Transport type for algorithm update data. This is intended to provide a
    list of base data used to perform updates against the specified target
    """


class ReaderErrorEventArgs(System_EventArgs):
    """
    Event arguments for the TextSubscriptionDataSourceReader.ReaderError event.
    """


class DataManager(QuantConnect.Interfaces.IAlgorithmSubscriptionManager, IDataFeedSubscriptionManager, IDataManager):
    """
    DataManager will manage the subscriptions for both the DataFeeds and the SubscriptionManager
    """


class CollectionSubscriptionDataSourceReader(ISubscriptionDataSourceReader):
    """
    Collection Subscription Factory takes a BaseDataCollection from BaseData factories
    and yields it one point at a time to the algorithm
    """


class TimeSliceFactory:
    """
    Instance base class that will provide methods for creating new TimeSlice
    """


class FileSystemDataFeed(IDataFeed):
    """
    Historical datafeed stream reader for processing files on a local disk.
    """


class BaseDataExchange:
    """
    Provides a means of distributing output from enumerators from a dedicated separate thread
    """


    class DataHandler:
        """
        Handler used to handle data emitted from enumerators
        """


    class EnumeratorHandler:
        """
        Handler used to manage a single enumerator's move next/end of stream behavior
        """


class DataPermissionManager(QuantConnect.Interfaces.IDataPermissionManager):
    """
    Entity in charge of handling data permissions
    """


class CurrencySubscriptionDataConfigManager:
    """
    Helper class to keep track of required internal currency SubscriptionDataConfig.
    This class is used by the UniverseSelection
    """


class PrecalculatedSubscriptionData(SubscriptionData):
    """
    Store data both raw and adjusted and the time at which it should be synchronized
    """


class SubscriptionDataSourceReader:
    """
    Provides a factory method for creating ISubscriptionDataSourceReader instances
    """


class DataFeedPacket:
    """
    Defines a container type to hold data produced by a data feed subscription
    """


class InvalidSourceEventArgs(System_EventArgs):
    """
    Event arguments for the ISubscriptionDataSourceReader.InvalidSource event
    """


class SubscriptionSynchronizer(ISubscriptionSynchronizer, QuantConnect.ITimeProvider):
    """
    Provides the ability to synchronize subscriptions into time slices
    """


class LiveTradingDataFeed(IDataFeed):
    """
    Provides an implementation of IDataFeed that is designed to deal with
    live, remote data sources
    """


    class EnumeratorHandler(BaseDataExchange.EnumeratorHandler):
        """
        Overrides methods of the base data exchange implementation
        """


class PredicateTimeProvider(QuantConnect.ITimeProvider):
    """
    Will generate time steps around the desired ITimeProvider
    Provided step evaluator should return true when the next time step
    is valid and time can advance
    """


class AggregationManager(QuantConnect.Data.IDataAggregator):
    """
    Aggregates ticks and bars based on given subscriptions.
    Current implementation is based on IDataConsolidator that consolidates ticks and put them into enumerator.
    """


class LiveSynchronizer(Synchronizer):
    """
    Implementation of the ISynchronizer interface which provides the mechanism to stream live data to the algorithm
    """



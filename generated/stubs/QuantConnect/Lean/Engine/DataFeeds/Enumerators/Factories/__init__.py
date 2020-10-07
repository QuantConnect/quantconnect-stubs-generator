import QuantConnect.Data
import typing


System_IDisposable = typing.Any


class LiveCustomDataSubscriptionEnumeratorFactory(QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """
    Provides an implementation of ISubscriptionEnumeratorFactory to handle live custom data.
    """


class FineFundamentalSubscriptionEnumeratorFactory(QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """
    Provides an implementation of ISubscriptionEnumeratorFactory that reads
    an entire SubscriptionDataSource into a single FineFundamental
    to be emitted on the tradable date at midnight
    """


class TimeTriggeredUniverseSubscriptionEnumeratorFactory(QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """
    Provides an implementation of ISubscriptionEnumeratorFactory to emit
    ticks based on UserDefinedUniverse.GetTriggerTimes, allowing universe
    selection to fire at planned times.
    """


class BaseDataSubscriptionEnumeratorFactory(QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """
    Provides a default implementation of ISubscriptionEnumeratorFactory that uses
    BaseData factory methods for reading sources
    """


class FuturesChainUniverseSubscriptionEnumeratorFactory(QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """
    Provides an implementation of ISubscriptionEnumeratorFactory for the FuturesChainUniverse in backtesting
    """


class SubscriptionDataReaderSubscriptionEnumeratorFactory(QuantConnect.Data.ISubscriptionEnumeratorFactory, System_IDisposable):
    """
    Provides an implementation of ISubscriptionEnumeratorFactory that used the
    SubscriptionDataReader
    """


class CorporateEventEnumeratorFactory:
    """
    Helper class used to create the corporate event providers
    MappingEventProvider, SplitEventProvider,
    DividendEventProvider, DelistingEventProvider
    """


class BaseDataCollectionSubscriptionEnumeratorFactory(QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """
    Provides an implementation of ISubscriptionEnumeratorFactory that reads
    an entire SubscriptionDataSource into a single BaseDataCollection
    to be emitted on the tradable date at midnight
    """


class OptionChainUniverseSubscriptionEnumeratorFactory(QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """
    Provides an implementation of ISubscriptionEnumeratorFactory for the OptionChainUniverse
    """



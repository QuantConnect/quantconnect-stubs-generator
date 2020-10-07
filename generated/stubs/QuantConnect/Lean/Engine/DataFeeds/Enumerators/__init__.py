import QuantConnect.Data.UniverseSelection
import abc
import typing


System_Collections_Generic_IEnumerator = typing.Any


QuantConnect_Lean_Engine_DataFeeds_Enumerators_BaseDataCollectionAggregatorEnumerator_T = typing.TypeVar('QuantConnect_Lean_Engine_DataFeeds_Enumerators_BaseDataCollectionAggregatorEnumerator_T')
QuantConnect_Lean_Engine_DataFeeds_Enumerators_RateLimitEnumerator_T = typing.TypeVar('QuantConnect_Lean_Engine_DataFeeds_Enumerators_RateLimitEnumerator_T')
QuantConnect_Lean_Engine_DataFeeds_Enumerators_ScannableEnumerator_T = typing.TypeVar('QuantConnect_Lean_Engine_DataFeeds_Enumerators_ScannableEnumerator_T')
QuantConnect_Lean_Engine_DataFeeds_Enumerators_EnqueueableEnumerator_T = typing.TypeVar('QuantConnect_Lean_Engine_DataFeeds_Enumerators_EnqueueableEnumerator_T')
QuantConnect_Lean_Engine_DataFeeds_Enumerators_RefreshEnumerator_T = typing.TypeVar('QuantConnect_Lean_Engine_DataFeeds_Enumerators_RefreshEnumerator_T')


class FastForwardEnumerator(System_Collections_Generic_IEnumerator):
    """
    Provides the ability to fast forward an enumerator based on the age of the data
    """


class OptionChainUniverseDataCollectionEnumerator(BaseDataCollectionAggregatorEnumerator[QuantConnect.Data.UniverseSelection.OptionChainUniverseDataCollection]):
    """
    Enumerates data into OptionChainUniverseDataCollection instances
    """


class SynchronizingEnumerator(System_Collections_Generic_IEnumerator):
    """
    Represents an enumerator capable of synchronizing other base data enumerators in time.
    This assumes that all enumerators have data time stamped in the same time zone
    """


class AuxiliaryDataEnumerator(System_Collections_Generic_IEnumerator):
    """
    Auxiliary data enumerator that will, initialize and call the ITradableDateEventProvider.GetEvents
    implementation each time there is a new tradable day for every ITradableDateEventProvider
    provided.
    """


class DataQueueFuturesChainUniverseDataCollectionEnumerator(System_Collections_Generic_IEnumerator):
    """
    Enumerates live futures symbol universe data into FuturesChainUniverseDataCollection instances
    """


class LiveEquityDataSynchronizingEnumerator(System_Collections_Generic_IEnumerator):
    """
    Represents an enumerator capable of synchronizing live equity data enumerators in time.
    This assumes that all enumerators have data time stamped in the same time zone.
    """


class ITradableDateEventProvider(metaclass=abc.ABCMeta):
    """
    Interface for event providers for new tradable dates
    """


class BaseDataCollectionAggregatorEnumerator(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_Enumerators_BaseDataCollectionAggregatorEnumerator_T], System_Collections_Generic_IEnumerator):
    """
    Provides an implementation of IEnumerator{BaseDataCollection}
    that aggregates an underlying IEnumerator{BaseData} into a single
    data packet
    """


class MappingEventProvider(ITradableDateEventProvider):
    """
    Event provider who will emit SymbolChangedEvent events
    """


class QuoteBarFillForwardEnumerator(System_Collections_Generic_IEnumerator):
    """
    The QuoteBarFillForwardEnumerator wraps an existing base data enumerator
    If the current QuoteBar has null Bid and/or Ask bars, it copies them from the previous QuoteBar
    """


class DividendEventProvider(ITradableDateEventProvider):
    """
    Event provider who will emit Dividend events
    """


class FillForwardEnumerator(System_Collections_Generic_IEnumerator):
    """
    The FillForwardEnumerator wraps an existing base data enumerator and inserts extra 'base data' instances
    on a specified fill forward resolution
    """


class LiveFillForwardEnumerator(FillForwardEnumerator):
    """
    An implementation of the FillForwardEnumerator that uses an ITimeProvider
    to determine if a fill forward bar needs to be emitted
    """


class ConcatEnumerator(System_Collections_Generic_IEnumerator):
    """
    Enumerator that will concatenate enumerators together sequentially enumerating them in the provided order
    """


class DelistingEventProvider(ITradableDateEventProvider):
    """
    Event provider who will emit Delisting events
    """


class ITradableDatesNotifier(metaclass=abc.ABCMeta):
    """
    Interface which will provide an event handler
    who will be fired with each new tradable day
    """


class SubscriptionDataEnumerator(System_Collections_Generic_IEnumerator):
    """
    An IEnumerator{SubscriptionData} which wraps an existing IEnumerator{BaseData}.
    """


class SubscriptionFilterEnumerator(System_Collections_Generic_IEnumerator):
    """
    Implements a wrapper around a base data enumerator to provide a final filtering step
    """


class PriceScaleFactorEnumerator(System_Collections_Generic_IEnumerator):
    """
    This enumerator will update the SubscriptionDataConfig.PriceScaleFactor when required
    and adjust the raw BaseData prices based on the provided SubscriptionDataConfig.
    Assumes the prices of the provided IEnumerator are in raw mode.
    """


class SplitEventProvider(ITradableDateEventProvider):
    """
    Event provider who will emit Split events
    """


class FrontierAwareEnumerator(System_Collections_Generic_IEnumerator):
    """
    Provides an implementation of IEnumerator{BaseData} that will not emit
    data ahead of the frontier as specified by an instance of ITimeProvider.
    An instance of TimeZoneOffsetProvider is used to convert between UTC
    and the data's native time zone
    """


class FuturesChainUniverseDataCollectionAggregatorEnumerator(BaseDataCollectionAggregatorEnumerator[QuantConnect.Data.UniverseSelection.FuturesChainUniverseDataCollection]):
    """
    Aggregates an enumerator into FuturesChainUniverseDataCollection instances
    """


class LiveAuxiliaryDataEnumerator(System_Collections_Generic_IEnumerator):
    """
    Emits auxiliary data points ready to be time synced
    """


class RateLimitEnumerator(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_Enumerators_RateLimitEnumerator_T], System_Collections_Generic_IEnumerator):
    """
    Provides augmentation of how often an enumerator can be called. Time is measured using
    an ITimeProvider instance and calls to the underlying enumerator are limited
    to a minimum time between each call.
    """


class ScannableEnumerator(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_Enumerators_ScannableEnumerator_T], System_Collections_Generic_IEnumerator):
    """
    An implementation of IEnumerator{T} that relies on "consolidated" data
    """


class EnqueueableEnumerator(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_Enumerators_EnqueueableEnumerator_T], System_Collections_Generic_IEnumerator):
    """
    An implementation of IEnumerator{T} that relies on the
    Enqueue method being called and only ends when Stop
    is called
    """


class RefreshEnumerator(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_Enumerators_RefreshEnumerator_T], System_Collections_Generic_IEnumerator):
    """
    Provides an implementation of IEnumerator{T} that will
    always return true via MoveNext.
    """


class DataQueueOptionChainUniverseDataCollectionEnumerator(System_Collections_Generic_IEnumerator):
    """
    Enumerates live options symbol universe data into OptionChainUniverseDataCollection instances
    """



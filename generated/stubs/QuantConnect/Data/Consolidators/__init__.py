import QuantConnect.Data
import QuantConnect.Data.Market
import abc
import typing


System_IDisposable = typing.Any


QuantConnect_Data_Consolidators_IdentityDataConsolidator_T = typing.TypeVar('QuantConnect_Data_Consolidators_IdentityDataConsolidator_T')
QuantConnect_Data_Consolidators_TradeBarConsolidatorBase_T = typing.TypeVar('QuantConnect_Data_Consolidators_TradeBarConsolidatorBase_T')
QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T = typing.TypeVar('QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T')
QuantConnect_Data_Consolidators_DataConsolidator_TInput = typing.TypeVar('QuantConnect_Data_Consolidators_DataConsolidator_TInput')
QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T = typing.TypeVar('QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T')
QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated = typing.TypeVar('QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated')


class CalendarType:
    """
    This class has no documentation.
    """


class SequentialConsolidator(IDataConsolidator):
    """
    This consolidator wires up the events on its First and Second consolidators
    such that data flows from the First to Second consolidator. It's output comes
    from the Second.
    """


class IdentityDataConsolidator(typing.Generic[QuantConnect_Data_Consolidators_IdentityDataConsolidator_T], DataConsolidator[QuantConnect_Data_Consolidators_IdentityDataConsolidator_T]):
    """
    Represents the simplest DataConsolidator implementation, one that is defined
    by a straight pass through of the data. No projection or aggregation is performed.
    """


class DynamicDataConsolidator(TradeBarConsolidatorBase[QuantConnect.Data.DynamicData]):
    """
    A data csolidator that can make trade bars from DynamicData derived types. This is useful for
    aggregating Quandl and other highly flexible dynamic custom data types.
    """


class TickConsolidator(TradeBarConsolidatorBase[QuantConnect.Data.Market.Tick]):
    """
    A data consolidator that can make bigger bars from ticks over a given
    time span or a count of pieces of data.
    """


class TickQuoteBarConsolidator(PeriodCountConsolidatorBase[QuantConnect.Data.Market.Tick, QuantConnect.Data.Market.QuoteBar]):
    """
    Consolidates ticks into quote bars. This consolidator ignores trade ticks
    """


class IDataConsolidator(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Represents a type capable of taking BaseData updates and firing events containing new
    'consolidated' data. These types can be used to produce larger bars, or even be used to
    transform the data before being sent to another component. The most common usage of these
    types is with indicators.
    """


class TradeBarConsolidatorBase(typing.Generic[QuantConnect_Data_Consolidators_TradeBarConsolidatorBase_T], PeriodCountConsolidatorBase[QuantConnect_Data_Consolidators_TradeBarConsolidatorBase_T, QuantConnect.Data.Market.TradeBar], metaclass=abc.ABCMeta):
    """
    A data consolidator that can make bigger bars from any base data
    
    This type acts as the base for other consolidators that produce bars on a given time step or for a count of data.
    """


class RenkoConsolidator(IDataConsolidator):
    """
    This consolidator can transform a stream of BaseData instances into a stream of RenkoBar
    """


class Calendar:
    """
    Helper class that provides Func{DateTime,CalendarInfo} used to define consolidation calendar
    """


class CalendarInfo:
    """
    This class has no documentation.
    """


class OpenInterestConsolidator(PeriodCountConsolidatorBase[QuantConnect.Data.Market.Tick, QuantConnect.Data.Market.OpenInterest]):
    """
    Type capable of consolidating open interest
    """


class BaseDataConsolidator(TradeBarConsolidatorBase[QuantConnect.Data.BaseData]):
    """
    Type capable of consolidating trade bars from any base data instance
    """


class FilteredIdentityDataConsolidator(typing.Generic[QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T], IdentityDataConsolidator[QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T]):
    """
    Provides an implementation of IDataConsolidator that preserve the input
    data unmodified. The input data is filtering by the specified predicate function
    """


class DataConsolidator(typing.Generic[QuantConnect_Data_Consolidators_DataConsolidator_TInput], IDataConsolidator, metaclass=abc.ABCMeta):
    """
    Represents a type that consumes BaseData instances and fires an event with consolidated
    and/or aggregated data.
    """


class PeriodCountConsolidatorBase(typing.Generic[QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T, QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated], DataConsolidator[QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T], metaclass=abc.ABCMeta):
    """
    Provides a base class for consolidators that emit data based on the passing of a period of time
    or after seeing a max count of data points.
    """


class TradeBarConsolidator(TradeBarConsolidatorBase[QuantConnect.Data.Market.TradeBar]):
    """
    A data consolidator that can make bigger bars from smaller ones over a given
    time span or a count of pieces of data.
    
    Use this consolidator to turn data of a lower resolution into data of a higher resolution,
    for example, if you subscribe to minute data but want to have a 15 minute bar.
    """


class QuoteBarConsolidator(PeriodCountConsolidatorBase[QuantConnect.Data.Market.QuoteBar, QuantConnect.Data.Market.QuoteBar]):
    """
    Consolidates QuoteBars into larger QuoteBars
    """



import abc
import typing


System_IDisposable = typing.Any
System_Exception = typing.Any


class ScheduleManager(IEventSchedule):
    """
    Provides access to the real time handler's event scheduling feature
    """


class FuncTimeRule(ITimeRule):
    """
    Uses a function to define a time rule as a projection of date times to date times
    """


class TimeConsumer:
    """
    Represents a timer consumer instance
    """


class FluentScheduledEventBuilder(IFluentSchedulingDateSpecifier, IFluentSchedulingRunnable):
    """
    Provides a builder class to allow for fluent syntax when constructing new events
    """


class IFluentSchedulingDateSpecifier(metaclass=abc.ABCMeta):
    """
    Specifies the date rule component of a scheduled event
    """


class IFluentSchedulingTimeSpecifier(metaclass=abc.ABCMeta):
    """
    Specifies the time rule component of a scheduled event
    """


class IFluentSchedulingRunnable(IFluentSchedulingTimeSpecifier, metaclass=abc.ABCMeta):
    """
    Specifies the callback component of a scheduled event, as well as final filters
    """


class ScheduledEvent(System_IDisposable):
    """
    Real time self scheduling event
    """


class DateRules:
    """
    Helper class used to provide better syntax when defining date rules
    """


class FuncDateRule(IDateRule):
    """
    Uses a function to define an enumerable of dates over a requested start/end period
    """


class IEventSchedule(metaclass=abc.ABCMeta):
    """
    Provides the ability to add/remove scheduled events from the real time handler
    """


class TimeRules:
    """
    Helper class used to provide better syntax when defining time rules
    """


class IDateRule(metaclass=abc.ABCMeta):
    """
    Specifies dates that events should be fired, used in conjunction with the ITimeRule
    """


class CompositeTimeRule(ITimeRule):
    """
    Combines multiple time rules into a single rule that emits for each rule
    """


class TimeMonitor(System_IDisposable):
    """
    Helper class that will monitor timer consumers and request more time if required.
    Used by IsolatorLimitResultProvider
    """


class ITimeRule(metaclass=abc.ABCMeta):
    """
    Specifies times times on dates for events, used in conjunction with IDateRule
    """


class ScheduledEventException(System_Exception):
    """
    Throw this if there is an exception in the callback function of the scheduled event
    """



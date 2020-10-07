import QuantConnect.Scheduling
import abc


class BacktestingRealTimeHandler(BaseRealTimeHandler, IRealTimeHandler):
    """
    Pseudo realtime event processing for backtesting to simulate realtime events in fast forward.
    """


class BaseRealTimeHandler(QuantConnect.Scheduling.IEventSchedule, metaclass=abc.ABCMeta):
    """
    Base class for the real time handler LiveTradingRealTimeHandler
    and BacktestingRealTimeHandler implementations
    """


class LiveTradingRealTimeHandler(BaseRealTimeHandler, IRealTimeHandler):
    """
    Live trading realtime event processing.
    """


class IRealTimeHandler(QuantConnect.Scheduling.IEventSchedule, metaclass=abc.ABCMeta):
    """
    Real time event handler, trigger functions at regular or pretimed intervals
    """


class ScheduledEventFactory:
    """
    Provides methods for creating common scheduled events
    """



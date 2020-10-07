import abc


class BaseResultsHandler(metaclass=abc.ABCMeta):
    """
    Provides base functionality to the implementations of IResultHandler
    """


class LiveTradingResultHandler(BaseResultsHandler, IResultHandler):
    """
    Live trading result handler implementation passes the messages to the QC live trading interface.
    """


class BacktestingResultHandler(BaseResultsHandler, IResultHandler):
    """
    Backtesting result handler passes messages back from the Lean to the User.
    """


class IResultHandler(metaclass=abc.ABCMeta):
    """
    Handle the results of the backtest: where should we send the profit, portfolio updates:
    Backtester or the Live trading platform:
    """


class RegressionResultHandler(BacktestingResultHandler):
    """
    Provides a wrapper over the BacktestingResultHandler that logs all order events
    to a separate file
    """



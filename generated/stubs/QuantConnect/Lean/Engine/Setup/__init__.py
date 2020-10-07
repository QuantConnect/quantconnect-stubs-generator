import abc
import typing


System_Exception = typing.Any
System_IDisposable = typing.Any


class BacktestingSetupHandler(ISetupHandler):
    """
    Backtesting setup handler processes the algorithm initialize method and sets up the internal state of the algorithm class.
    """


class AlgorithmSetupException(System_Exception):
    """
    Defines an exception generated in the course of invoking ISetupHandler.Setup
    """


class ConsoleSetupHandler(ISetupHandler):
    """
    Console setup handler to initialize and setup the Lean Engine properties for a local backtest
    """


class ISetupHandler(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Interface to setup the algorithm. Pass in a raw algorithm, return one with portfolio, cash, etc already preset.
    """


class SetupHandlerParameters:
    """
    Defines the parameters for ISetupHandler
    """


class BaseSetupHandler:
    """
    Base class that provides shared code for
    the ISetupHandler implementations
    """


class BrokerageSetupHandler(ISetupHandler):
    """
    Defines a set up handler that initializes the algorithm instance using values retrieved from the user's brokerage account
    """



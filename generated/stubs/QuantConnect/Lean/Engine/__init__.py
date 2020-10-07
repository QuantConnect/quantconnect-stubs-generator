import QuantConnect
import typing


System_IDisposable = typing.Any


class AlgorithmTimeLimitManager(QuantConnect.IIsolatorLimitResultProvider):
    """
    Provides an implementation of IIsolatorLimitResultProvider that tracks the algorithm
    manager's time loops and enforces a maximum amount of time that each time loop may take to execute.
    The isolator uses the result provided by IsWithinLimit to determine if it should
    terminate the algorithm for violation of the imposed limits.
    """


class Engine:
    """
    LEAN ALGORITHMIC TRADING ENGINE: ENTRY POINT.
    
    The engine loads new tasks, create the algorithms and threads, and sends them
    to Algorithm Manager to be executed. It is the primary operating loop.
    """


class LeanEngineAlgorithmHandlers(System_IDisposable):
    """
    Provides a container for the algorithm specific handlers
    """


class AlgorithmManager:
    """
    Algorithm manager class executes the algorithm and generates and passes through the algorithm events.
    """


class LeanEngineSystemHandlers(System_IDisposable):
    """
    Provides a container for the system level handlers
    """



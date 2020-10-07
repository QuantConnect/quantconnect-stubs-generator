import abc


class IExceptionInterpreter(metaclass=abc.ABCMeta):
    """
    Defines an exception interpreter. Interpretations are invoked on IAlgorithm.RunTimeError
    """


class InvalidTokenPythonExceptionInterpreter(IExceptionInterpreter):
    """
    Interprets InvalidTokenPythonExceptionInterpreter instances
    """


class PythonExceptionInterpreter(IExceptionInterpreter):
    """
    Interprets PythonExceptionInterpreter instances
    """


class DllNotFoundPythonExceptionInterpreter(IExceptionInterpreter):
    """
    Interprets DllNotFoundPythonExceptionInterpreter instances
    """


class StackExceptionInterpreter(IExceptionInterpreter):
    """
    Interprets exceptions using the configured interpretations
    """


class UnsupportedOperandPythonExceptionInterpreter(IExceptionInterpreter):
    """
    Interprets UnsupportedOperandPythonExceptionInterpreter instances
    """


class NoMethodMatchPythonExceptionInterpreter(IExceptionInterpreter):
    """
    Interprets NoMethodMatchPythonExceptionInterpreter instances
    """


class KeyErrorPythonExceptionInterpreter(IExceptionInterpreter):
    """
    Interprets KeyErrorPythonExceptionInterpreter instances
    """


class ScheduledEventExceptionInterpreter(IExceptionInterpreter):
    """
    Interprets ScheduledEventException instances
    """



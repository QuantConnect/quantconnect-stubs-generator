import abc
import enum
import typing


System_IDisposable = typing.Any


class FunctionalLogHandler(ILogHandler):
    """
    ILogHandler implementation that writes log output to result handler
    """


class LogType(enum.Enum):
    """
    Error level
    """


class RegressionFileLogHandler(FileLogHandler):
    """
    Provides an implementation of ILogHandler that writes all log messages to a file on disk
    without timestamps.
    """


class CompositeLogHandler(ILogHandler):
    """
    Provides an ILogHandler implementation that composes multiple handlers
    """


class WhoCalledMe:
    """
    Provides methods for determining higher stack frames
    """


class Log:
    """
    Logging management class.
    """


class LogEntry:
    """
    Log entry wrapper to make logging simpler:
    """


class CompositeNLogHandler(ILogHandler):
    """
    Provides an ILogHandler implementation that composes multiple handlers
    """


class NLogHandler(ILogHandler):
    """
    Provides an implementation of ILogHandler that writes all log messages to a file on disk.
    """


class ConsoleLogHandler(ILogHandler):
    """
    ILogHandler implementation that writes log output to console.
    """


class LogHandlerExtensions:
    """
    Logging extensions.
    """


class FileLogHandler(ILogHandler):
    """
    Provides an implementation of ILogHandler that writes all log messages to a file on disk.
    """


class ILogHandler(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Interface for redirecting log output
    """


class QueueLogHandler(ILogHandler):
    """
    ILogHandler implementation that queues all logs and writes them when instructed.
    """



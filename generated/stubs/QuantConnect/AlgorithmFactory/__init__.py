import enum
import typing


System_MarshalByRefObject = typing.Any


class DebuggerHelper:
    """
    Helper class used to start a new debugging session
    """


    class DebuggingMethod(enum.Enum):
        """
        The different implemented debugging methods
        """


class Loader(System_MarshalByRefObject):
    """
    Loader creates and manages the memory and exception space of the algorithm, ensuring if it explodes the Lean Engine is intact.
    """



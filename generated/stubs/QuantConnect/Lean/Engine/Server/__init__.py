import abc
import typing


System_IDisposable = typing.Any


class LocalLeanManager(ILeanManager):
    """
    NOP implementation of the ILeanManager interface
    """


class ILeanManager(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Provides scope into Lean that is convenient for managing a lean instance
    """



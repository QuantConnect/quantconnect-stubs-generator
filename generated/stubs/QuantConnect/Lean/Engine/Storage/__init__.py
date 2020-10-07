import QuantConnect.Interfaces
import typing


System_Exception = typing.Any


class StorageLimitExceededException(System_Exception):
    """
    Exception thrown when the object store storage limit has been exceeded
    """


class LocalObjectStore(QuantConnect.Interfaces.IObjectStore):
    """
    A local disk implementation of IObjectStore.
    """



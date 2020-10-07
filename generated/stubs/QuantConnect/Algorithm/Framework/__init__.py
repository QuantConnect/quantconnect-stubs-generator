import abc


class NotifiedSecurityChanges:
    """
    Provides convenience methods for updating collections in responses to securities changed events
    """


class INotifiedSecurityChanges(metaclass=abc.ABCMeta):
    """
    Types implementing this interface will be called when the algorithm's set of securities changes
    """



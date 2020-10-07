import abc


class PricingStreamSession(StreamSession):
    """
    Pricing streaming session
    """


class StreamSession(metaclass=abc.ABCMeta):
    """
    StreamSession abstract class used to model streaming sessions
    """


class TransactionStreamSession(StreamSession):
    """
    Transaction streaming session
    """



import abc


class IRefillStrategy(metaclass=abc.ABCMeta):
    """
    Provides a strategy for making tokens available for consumption in the ITokenBucket
    """


class ITokenBucket(metaclass=abc.ABCMeta):
    """
    Defines a token bucket for rate limiting
    See: https://en.wikipedia.org/wiki/Token_bucket
    """


class ThreadSleepStrategy(ISleepStrategy):
    """
    Provides a CPU non-intensive means of waiting for more tokens to be available in ITokenBucket.
    This strategy should be the most commonly used as it either sleeps or yields the currently executing thread,
    allowing for other threads to execute while the current thread is blocked and waiting for new tokens to become
    available in the bucket for consumption.
    """


class LeakyBucket(ITokenBucket):
    """
    Provides an implementation of ITokenBucket that implements the leaky bucket algorithm
    See: https://en.wikipedia.org/wiki/Leaky_bucket
    """


class BusyWaitSleepStrategy(ISleepStrategy):
    """
    Provides a CPU intensive means of waiting for more tokens to be available in ITokenBucket.
    This strategy is only viable when the requested number of tokens is expected to become available in an
    extremely short period of time. This implementation aims to keep the current thread executing to prevent
    potential content switches arising from a thread yielding or sleeping strategy.
    """


class TokenBucket:
    """
    Provides extension methods for interacting with ITokenBucket instances as well
    as access to the NullTokenBucket via TokenBucket.Null
    """


class FixedIntervalRefillStrategy(IRefillStrategy):
    """
    Provides a refill strategy that has a constant, quantized refill rate.
    For example, after 1 minute passes add 5 units. If 59 seconds has passed, it will add zero unit,
    but if 2 minutes have passed, then 10 units would be added.
    """


class ISleepStrategy(metaclass=abc.ABCMeta):
    """
    Defines a strategy for sleeping the current thread of execution. This is currently used via the
    ITokenBucket.Consume in order to wait for new tokens to become available for consumption.
    """



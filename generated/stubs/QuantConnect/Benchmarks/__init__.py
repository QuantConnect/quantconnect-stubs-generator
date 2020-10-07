import abc


class IBenchmark(metaclass=abc.ABCMeta):
    """
    Specifies how to compute a benchmark for an algorithm
    """


class FuncBenchmark(IBenchmark):
    """
    Creates a benchmark defined by a function
    """


class SecurityBenchmark(IBenchmark):
    """
    Creates a benchmark defined by the closing price of a Security instance
    """



import abc


class WorkItem:
    """
    This class has no documentation.
    """


class IWorkQueue(metaclass=abc.ABCMeta):
    """
    Work queue abstraction
    """


class WorkQueue(IWorkQueue):
    """
    This class has no documentation.
    """


class WeightedWorkScheduler:
    """
    This singleton class will create a thread pool to processes work
    that will be prioritized based on it's weight
    """



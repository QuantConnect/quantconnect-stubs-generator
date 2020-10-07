import abc


class IOptionExerciseModel(metaclass=abc.ABCMeta):
    """
    Represents a model that simulates option exercise and lapse events
    """


class DefaultExerciseModel(IOptionExerciseModel):
    """
    Represents the default option exercise model (physical, cash settlement)
    """



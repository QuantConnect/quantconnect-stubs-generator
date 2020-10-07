import QuantConnect.Algorithm.Framework
import abc


class StandardDeviationExecutionModel(ExecutionModel):
    """
    Execution model that submits orders while the current market prices is at least the configured number of standard
    deviations away from the mean in the favorable direction (below/above for buy/sell respectively)
    """


    class SymbolData:
        """
        This class is protected.
        """


class VolumeWeightedAveragePriceExecutionModel(ExecutionModel):
    """
    Execution model that submits orders while the current market price is more favorable that the current volume weighted average price.
    """


    class SymbolData:
        """
        This class is protected.
        """


class NullExecutionModel(ExecutionModel):
    """
    Provides an implementation of IExecutionModel that does nothing
    """


class ExecutionModel(IExecutionModel):
    """
    Provides a base class for execution models
    """


class ImmediateExecutionModel(ExecutionModel):
    """
    Provides an implementation of IExecutionModel that immediately submits
    market orders to achieve the desired portfolio targets
    """


class IExecutionModel(QuantConnect.Algorithm.Framework.INotifiedSecurityChanges, metaclass=abc.ABCMeta):
    """
    Algorithm framework model that executes portfolio targets
    """


class ExecutionModelPythonWrapper(ExecutionModel):
    """
    Provides an implementation of IExecutionModel that wraps a PyObject object
    """



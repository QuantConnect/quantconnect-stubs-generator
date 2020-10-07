import QuantConnect.Brokerages
import QuantConnect.Data
import QuantConnect.Data.Consolidators
import QuantConnect.Data.Custom
import QuantConnect.Orders.Fees
import QuantConnect.Orders.Fills
import QuantConnect.Orders.Slippage
import QuantConnect.Securities
import QuantConnect.Securities.Volatility


class PythonSlice(QuantConnect.Data.Slice):
    """
    Provides a data structure for all of an algorithm's data at a single time step
    """


class SlippageModelPythonWrapper(QuantConnect.Orders.Slippage.ISlippageModel):
    """
    Wraps a PyObject object that represents a model that simulates market order slippage
    """


class PythonInitializer:
    """
    Helper class for Python initialization
    """


class BrokerageMessageHandlerPythonWrapper(QuantConnect.Brokerages.IBrokerageMessageHandler):
    """
    Provides a wrapper for IBrokerageMessageHandler implementations written in python
    """


class BuyingPowerModelPythonWrapper(QuantConnect.Securities.IBuyingPowerModel):
    """
    Wraps a PyObject object that represents a security's model of buying power
    """


class FeeModelPythonWrapper(QuantConnect.Orders.Fees.FeeModel):
    """
    Provides an order fee model that wraps a PyObject object that represents a model that simulates order fees
    """


class PandasConverter:
    """
    Collection of methods that converts lists of objects in pandas.DataFrame
    """


class FillModelPythonWrapper(QuantConnect.Orders.Fills.FillModel):
    """
    Wraps a PyObject object that represents a model that simulates order fill events
    """


class DataConsolidatorPythonWrapper(QuantConnect.Data.Consolidators.IDataConsolidator):
    """
    Provides an Data Consolidator that wraps a PyObject object that represents a custom Python consolidator
    """


class PythonData(QuantConnect.Data.DynamicData):
    """
    Dynamic data class for Python algorithms.
    Stores properties of python instances in DynamicData dictionary
    """


class PythonWrapper:
    """
    Provides extension methods for managing python wrapper classes
    """


class PythonConsolidator:
    """
    Provides a base class for python consolidators, necessary to use event handler.
    """


class PandasData:
    """
    Organizes a list of data to create pandas.DataFrames
    """


class BrokerageModelPythonWrapper(QuantConnect.Brokerages.IBrokerageModel):
    """
    Provides an implementation of IBrokerageModel that wraps a PyObject object
    """


class PythonQuandl(QuantConnect.Data.Custom.Quandl):
    """
    Dynamic data class for Python algorithms.
    """


class SecurityInitializerPythonWrapper(QuantConnect.Securities.ISecurityInitializer):
    """
    Wraps a PyObject object that represents a type capable of initializing a new security
    """


class VolatilityModelPythonWrapper(QuantConnect.Securities.Volatility.BaseVolatilityModel):
    """
    Provides a volatility model that wraps a PyObject object that represents a model that computes the volatility of a security
    """


class PythonActivator:
    """
    Provides methods for creating new instances of python custom data objects
    """


class MarginCallModelPythonWrapper(QuantConnect.Securities.IMarginCallModel):
    """
    Provides a margin call model that wraps a PyObject object that represents the model responsible for picking which orders should be executed during a margin call
    """



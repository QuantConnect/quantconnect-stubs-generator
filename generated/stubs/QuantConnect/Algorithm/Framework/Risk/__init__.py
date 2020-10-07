import QuantConnect.Algorithm.Framework
import abc


class MaximumDrawdownPercentPortfolio(RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits the drawdown of the portfolio
    to the specified percentage. Once this is triggered the algorithm will need to be manually restarted.
    """


class MaximumSectorExposureRiskManagementModel(RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits
    the sector exposure to the specified percentage
    """


class TrailingStopRiskManagementModel(RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits the maximum possible loss
    measured from the highest unrealized profit
    """


class MaximumUnrealizedProfitPercentPerSecurity(RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits the unrealized profit
    per holding to the specified percentage
    """


class MaximumDrawdownPercentPerSecurity(RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits the drawdown
    per holding to the specified percentage
    """


class RiskManagementModel(IRiskManagementModel):
    """
    Provides a base class for risk management models
    """


class CompositeRiskManagementModel(RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that combines multiple risk
    models into a single risk management model and properly sets each insights 'SourceModel' property.
    """


class RiskManagementModelPythonWrapper(RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that wraps a PyObject object
    """


class IRiskManagementModel(QuantConnect.Algorithm.Framework.INotifiedSecurityChanges, metaclass=abc.ABCMeta):
    """
    Algorithm framework model that manages an algorithm's risk/downside
    """


class NullRiskManagementModel(RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that does nothing
    """



import QuantConnect.Interfaces
import QuantConnect.Securities
import abc


class OptionSymbolProperties(QuantConnect.Securities.SymbolProperties):
    """
    Represents common properties for a specific option contract
    """


class IQLRiskFreeRateEstimator(metaclass=abc.ABCMeta):
    """
    Defines QuantLib risk free rate estimator for option pricing model.
    """


class EmptyOptionChainProvider(QuantConnect.Interfaces.IOptionChainProvider):
    """
    An implementation of IOptionChainProvider that always returns an empty list of contracts
    """


class IOptionPriceModel(metaclass=abc.ABCMeta):
    """
    Defines a model used to calculate the theoretical price of an option contract.
    """


class OptionPriceModels:
    """
    Static class contains definitions of major option pricing models that can be used in LEAN
    """


class OptionPriceModelResult:
    """
    Result type for IOptionPriceModel.Evaluate
    """


class ConstantQLRiskFreeRateEstimator(IQLRiskFreeRateEstimator):
    """
    Class implements default flat risk free curve, implementing IQLRiskFreeRateEstimator.
    """


class IQLUnderlyingVolatilityEstimator(metaclass=abc.ABCMeta):
    """
    Defines QuantLib underlying volatility estimator for option pricing model. User may define his own estimators,
    including those forward and backward looking ones.
    """


class OptionStrategy:
    """
    Option strategy specification class. Describes option strategy and its parameters for trading.
    """


    class OptionLegData:
        """
        This class is a POCO containing basic data for the option legs of the strategy
        """


    class UnderlyingLegData:
        """
        This class is a POCO containing basic data for the underlying leg of the strategy
        """


class ConstantQLDividendYieldEstimator(IQLDividendYieldEstimator):
    """
    Class implements default flat dividend yield curve estimator, implementing IQLDividendYieldEstimator.
    """


class OptionHolding(QuantConnect.Securities.SecurityHolding):
    """
    Option holdings implementation of the base securities class
    """


class CurrentPriceOptionPriceModel(IOptionPriceModel):
    """
    Provides a default implementation of IOptionPriceModel that does not compute any
    greeks and uses the current price for the theoretical price.
    This is a stub implementation until the real models are implemented
    """


class IQLDividendYieldEstimator(metaclass=abc.ABCMeta):
    """
    Defines QuantLib dividend yield estimator for option pricing model. User may define his own estimators,
    including those forward and backward looking ones.
    """


class OptionExchange(QuantConnect.Securities.SecurityExchange):
    """
    Option exchange class - information and helper tools for option exchange properties
    """


class OptionDataFilter(QuantConnect.Securities.SecurityDataFilter):
    """
    Option packet by packet data filtering mechanism for dynamically detecting bad ticks.
    """


class QLOptionPriceModel(IOptionPriceModel):
    """
    Provides QuantLib(QL) implementation of IOptionPriceModel to support major option pricing models, available in QL.
    """


class OptionCache(QuantConnect.Securities.SecurityCache):
    """
    Option specific caching support
    """


class ConstantQLUnderlyingVolatilityEstimator(IQLUnderlyingVolatilityEstimator):
    """
    Class implements default underlying constant volatility estimator (IQLUnderlyingVolatilityEstimator.), that projects the underlying own volatility
    model into corresponding option pricing model.
    """


class OptionStrategies:
    """
    This class has no documentation.
    """


class Option(QuantConnect.Securities.Security, QuantConnect.Securities.IDerivativeSecurity, QuantConnect.Interfaces.IOptionPrice):
    """
    Option Security Object Implementation for Option Assets
    """


class OptionSymbol:
    """
    Static class contains common utility methods specific to symbols representing the option contracts
    """


class OptionMarginModel(QuantConnect.Securities.SecurityMarginModel):
    """
    Represents a simple option margin model.
    """


class OptionPortfolioModel(QuantConnect.Securities.SecurityPortfolioModel):
    """
    Provides an implementation of ISecurityPortfolioModel for options that supports
    default fills as well as option exercising.
    """



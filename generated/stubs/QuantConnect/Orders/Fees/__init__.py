import abc


class OrderFeeParameters:
    """
    Defines the parameters for IFeeModel.GetOrderFee
    """


class InteractiveBrokersFeeModel(FeeModel):
    """
    Provides the default implementation of IFeeModel
    """


class FxcmFeeModel(FeeModel):
    """
    Provides an implementation of FeeModel that models FXCM order fees
    """


class IFeeModel(metaclass=abc.ABCMeta):
    """
    Represents a model the simulates order fees
    """


class FeeModelExtensions:
    """
    Provide extension method for IFeeModel to enable
    backwards compatibility of invocations.
    """


class BinanceFeeModel(FeeModel):
    """
    Provides an implementation of FeeModel that models Binance order fees
    """


class FeeModel(IFeeModel):
    """
    Base class for any order fee model
    """


class ConstantFeeModel(FeeModel):
    """
    Provides an order fee model that always returns the same order fee.
    """


class OrderFee:
    """
    Defines the result for IFeeModel.GetOrderFee
    """


class GDAXFeeModel(FeeModel):
    """
    Provides an implementation of FeeModel that models GDAX order fees
    """


class AlphaStreamsFeeModel(FeeModel):
    """
    Provides an implementation of FeeModel that models order fees that alpha stream clients pay/receive
    """


class BitfinexFeeModel(FeeModel):
    """
    Provides an implementation of FeeModel that models Bitfinex order fees
    """



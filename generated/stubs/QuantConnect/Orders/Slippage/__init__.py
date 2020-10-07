import abc


class VolumeShareSlippageModel(ISlippageModel):
    """
    Represents a slippage model that is calculated by multiplying the price impact constant
    by the square of the ratio of the order to the total volume.
    """


class ConstantSlippageModel(ISlippageModel):
    """
    Represents a slippage model that uses a constant percentage of slip
    """


class AlphaStreamsSlippageModel(ISlippageModel):
    """
    Represents a slippage model that uses a constant percentage of slip
    """


class ISlippageModel(metaclass=abc.ABCMeta):
    """
    Represents a model that simulates market order slippage
    """



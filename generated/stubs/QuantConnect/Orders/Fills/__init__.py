import abc


class FillModelParameters:
    """
    Defines the parameters for the IFillModel method
    """


class FillModel(IFillModel):
    """
    Provides a base class for all fill models
    """


    class Prices:
        """
        This class has no documentation.
        """


class ImmediateFillModel(FillModel):
    """
    Represents the default fill model used to simulate order fills
    """


class Fill:
    """
    Defines the result for IFillModel.Fill
    """


class IFillModel(metaclass=abc.ABCMeta):
    """
    Represents a model that simulates order fill events
    """


class LatestPriceFillModel(ImmediateFillModel):
    """
    This fill model is provided because currently the data sourced for Crypto
    is limited to one minute snapshots for Quote data. This fill model will
    ignore the trade/quote distinction and return the latest pricing information
    in order to determine the correct fill price
    """



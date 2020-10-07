import QuantConnect.Data
import enum


class EstimizeEstimate(QuantConnect.Data.BaseData):
    """
    Financial estimates for the specified company
    """


class EstimizeRelease(QuantConnect.Data.BaseData):
    """
    Financial releases for the specified company
    """


class EstimizeConsensus(QuantConnect.Data.BaseData):
    """
    Consensus of the specified release
    """


class Source(enum.Enum):
    """
    Source of the Consensus
    """


class Type(enum.Enum):
    """
    Type of the consensus
    """



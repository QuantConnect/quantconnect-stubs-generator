import QuantConnect.Interfaces
import typing


System_MarshalByRefObject = typing.Any


class QCAlgorithm(System_MarshalByRefObject, QuantConnect.Interfaces.IAlgorithm):
    """
    This class has no documentation.
    """


class CandlestickPatterns:
    """
    Provides helpers for using candlestick patterns
    """


class ConstituentUniverseDefinitions:
    """
    Provides helpers for defining constituent universes based on the Morningstar
    asset classification AssetClassification https://www.morningstar.com/
    """


class IndexUniverseDefinitions:
    """
    Provides helpers for defining universes based on index definitions
    """


class DollarVolumeUniverseDefinitions:
    """
    Provides helpers for defining universes based on the daily dollar volume
    """


class UniverseDefinitions:
    """
    Provides helpers for defining universes in algorithms
    """



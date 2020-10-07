import QuantConnect.Data
import QuantConnect.Interfaces
import typing


System_IEquatable = typing.Any


class MapFileRow(System_IEquatable):
    """
    Represents a single row in a map_file. This is a csv file ordered as {date, mapped symbol}
    """


class MappingExtensions:
    """
    Mapping extensions helper methods
    """


class MapFileResolver(typing.List[MapFile]):
    """
    Provides a means of mapping a symbol at a point in time to the map file
    containing that share class's mapping information
    """


    class MapFileRowEntry(System_IEquatable):
        """
        Combines the map file row with the map file path that produced the row
        """


class LocalDiskFactorFileProvider(QuantConnect.Interfaces.IFactorFileProvider):
    """
    Provides an implementation of IFactorFileProvider that searches the local disk
    """


class LocalDiskMapFileProvider(QuantConnect.Interfaces.IMapFileProvider):
    """
    Provides a default implementation of IMapFileProvider that reads from
    the local disk
    """


class ZipEntryName(QuantConnect.Data.BaseData):
    """
    Defines a data type that just produces data points from the zip entry names in a zip file
    """


class FactorFile(typing.List[FactorFileRow]):
    """
    Represents an entire factor file for a specified symbol
    """


class MapFile(typing.List[MapFileRow]):
    """
    Represents an entire map file for a specified symbol
    """


class FactorFileRow:
    """
    Defines a single row in a factor_factor file. This is a csv file ordered as {date, price factor, split factor, reference price}
    """



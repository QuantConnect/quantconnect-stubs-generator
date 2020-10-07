import QuantConnect.Algorithm
import QuantConnect.Lean.Engine.DataFeeds
import enum
import typing


JsonConverter = typing.Any
System_IDisposable = typing.Any


QuantConnect_Report_NullResultValueTypeJsonConverter_T = typing.TypeVar('QuantConnect_Report_NullResultValueTypeJsonConverter_T')


class NullResultValueTypeJsonConverter(typing.Generic[QuantConnect_Report_NullResultValueTypeJsonConverter_T], JsonConverter):
    """
    Removes null values in the Result object's x,y values so that
    deserialization can occur without exceptions.
    """


class Rolling:
    """
    Rolling window functions
    """


class DrawdownCollection:
    """
    Collection of drawdowns for the given period marked by start and end date
    """


class DrawdownPeriod:
    """
    Represents a period of time where the drawdown ranks amongst the top N drawdowns.
    """


class Program:
    """
    Lean Report creates a PDF strategy summary from the backtest and live json objects.
    """


class DeedleUtil:
    """
    Utility extension methods for Deedle series/frames
    """


class ResultsUtil:
    """
    Utility methods for dealing with the Result objects
    """


class PointInTimePortfolio:
    """
    Lightweight portfolio at a point in time
    """


    class PointInTimeHolding:
        """
        Holding of an asset at a point in time
        """


class ReportKey:
    """
    Helper shortcuts for report injection points.
    """


class Crisis:
    """
    Crisis events utility class
    """


class CrisisEvent(enum.Enum):
    """
    Crisis Events
    """


class Report:
    """
    This class has no documentation.
    """


class Metrics:
    """
    Strategy metrics collection such as usage of funds and asset allocations
    """


class OrderTypeNormalizingJsonConverter(JsonConverter):
    """
    Normalizes the "Type" field to a value that will allow for
    successful deserialization in the OrderJsonConverter class.
    """


class PortfolioLooperAlgorithm(QuantConnect.Algorithm.QCAlgorithm):
    """
    Fake algorithm that initializes portfolio and algorithm securities. Never ran.
    """


class PortfolioLooper(System_IDisposable):
    """
    Runs LEAN to calculate the portfolio at a given time from Order objects.
    Generates and returns PointInTimePortfolio objects that represents
    the holdings and other miscellaneous metrics at a point in time by reprocessing the orders
    as they were filled.
    """


class MockDataFeed(QuantConnect.Lean.Engine.DataFeeds.IDataFeed):
    """
    Fake IDataFeed
    """



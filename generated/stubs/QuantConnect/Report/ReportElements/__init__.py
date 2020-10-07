import abc


class IReportElement(metaclass=abc.ABCMeta):
    """
    Common interface for template elements of the report
    """


class SharpeRatioReportElement(ReportElement):
    """
    This class has no documentation.
    """


class LeverageUtilizationReportElement(ChartReportElement):
    """
    This class has no documentation.
    """


class EstimatedCapacityReportElement(ReportElement):
    """
    This class has no documentation.
    """


class RollingSharpeReportElement(ChartReportElement):
    """
    This class has no documentation.
    """


class CAGRReportElement(ReportElement):
    """
    This class has no documentation.
    """


class AssetAllocationReportElement(ChartReportElement):
    """
    This class has no documentation.
    """


class TextReportElement(ReportElement):
    """
    This class has no documentation.
    """


class ReportElement(IReportElement, metaclass=abc.ABCMeta):
    """
    Common interface for template elements of the report
    """


class PSRReportElement(ReportElement):
    """
    This class has no documentation.
    """


class TradesPerDayReportElement(ReportElement):
    """
    This class has no documentation.
    """


class ChartReportElement(ReportElement, metaclass=abc.ABCMeta):
    """
    This class has no documentation.
    """


class DrawdownReportElement(ChartReportElement):
    """
    This class has no documentation.
    """


class MaxDrawdownReportElement(ReportElement):
    """
    This class has no documentation.
    """


class CrisisReportElement(ChartReportElement):
    """
    This class has no documentation.
    """


class ReturnsPerTradeReportElement(ChartReportElement):
    """
    This class has no documentation.
    """


class CumulativeReturnsReportElement(ChartReportElement):
    """
    This class has no documentation.
    """


class ExposureReportElement(ChartReportElement):
    """
    This class has no documentation.
    """


class MonthlyReturnsReportElement(ChartReportElement):
    """
    This class has no documentation.
    """


class DailyReturnsReportElement(ChartReportElement):
    """
    This class has no documentation.
    """


class TurnoverReportElement(ReportElement):
    """
    This class has no documentation.
    """


class DaysLiveReportElement(ReportElement):
    """
    This class has no documentation.
    """


class AnnualReturnsReportElement(ChartReportElement):
    """
    This class has no documentation.
    """


class InformationRatioReportElement(ReportElement):
    """
    This class has no documentation.
    """


class KellyEstimateReportElement(ReportElement):
    """
    This class has no documentation.
    """


class RollingPortfolioBetaReportElement(ChartReportElement):
    """
    This class has no documentation.
    """


class MarketsReportElement(ReportElement):
    """
    This class has no documentation.
    """



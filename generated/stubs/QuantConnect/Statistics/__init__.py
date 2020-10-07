import QuantConnect.Interfaces
import enum


class TradeStatistics:
    """
    The TradeStatistics class represents a set of statistics calculated from a list of closed trades
    """


class StatisticsBuilder:
    """
    The StatisticsBuilder class creates summary and rolling statistics from trades, equity and benchmark points
    """


class PortfolioStatistics:
    """
    The PortfolioStatistics class represents a set of statistics calculated from equity and benchmark samples
    """


class TradeBuilder(QuantConnect.Interfaces.ITradeBuilder):
    """
    The TradeBuilder class generates trades from executions and market price updates
    """


class StatisticsResults:
    """
    The StatisticsResults class represents total and rolling statistics for an algorithm
    """


class AlgorithmPerformance:
    """
    The AlgorithmPerformance class is a wrapper for TradeStatistics and PortfolioStatistics
    """


class KellyCriterionManager:
    """
    Class in charge of calculating the Kelly Criterion values.
    Will use the sample values of the last year.
    """


class Trade:
    """
    Represents a closed trade
    """


class FitnessScoreManager:
    """
    Implements a fitness score calculator needed to account for strategy volatility,
    returns, drawdown, and factor in the turnover to ensure the algorithm engagement
    is statistically significant
    """


class Statistics:
    """
    Calculate all the statistics required from the backtest, based on the equity curve and the profit loss statement.
    """


class TradeDirection(enum.Enum):
    """
    Direction of a trade
    """


class FillGroupingMethod(enum.Enum):
    """
    The method used to group order fills into trades
    """


class FillMatchingMethod(enum.Enum):
    """
    The method used to match offsetting order fills
    """



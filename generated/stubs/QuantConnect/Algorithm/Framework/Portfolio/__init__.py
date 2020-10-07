import QuantConnect
import QuantConnect.Algorithm.Framework
import abc
import enum
import typing


class UnconstrainedMeanVariancePortfolioOptimizer(IPortfolioOptimizer):
    """
    Provides an implementation of a portfolio optimizer with unconstrained mean variance.
    """


class MinimumVariancePortfolioOptimizer(IPortfolioOptimizer):
    """
    Provides an implementation of a minimum variance portfolio optimizer that calculate the optimal weights
    with the weight range from -1 to 1 and minimize the portfolio variance with a target return of 2%
    """


class AccumulativeInsightPortfolioConstructionModel(PortfolioConstructionModel):
    """
    Provides an implementation of IPortfolioConstructionModel that allocates percent of account
    to each insight, defaulting to 3%.
    For insights of direction InsightDirection.Up, long targets are returned and
    for insights of direction InsightDirection.Down, short targets are returned.
    By default, no rebalancing shall be done.
    Rules:
       1. On active Up insight, increase position size by percent
       2. On active Down insight, decrease position size by percent
       3. On active Flat insight, move by percent towards 0
       4. On expired insight, and no other active insight, emits a 0 target'''
    """


class InsightWeightingPortfolioConstructionModel(EqualWeightingPortfolioConstructionModel):
    """
    Provides an implementation of IPortfolioConstructionModel that generates percent targets based on the
    Insight.Weight. The target percent holdings of each Symbol is given by the Insight.Weight
    from the last active Insight for that symbol.
    For insights of direction InsightDirection.Up, long targets are returned and for insights of direction
    InsightDirection.Down, short targets are returned.
    If the sum of all the last active Insight per symbol is bigger than 1, it will factor down each target
    percent holdings proportionally so the sum is 1.
    It will ignore Insight that have no Insight.Weight value.
    """


class ConfidenceWeightedPortfolioConstructionModel(InsightWeightingPortfolioConstructionModel):
    """
    Provides an implementation of IPortfolioConstructionModel that generates percent targets based on the
    Insight.Confidence. The target percent holdings of each Symbol is given by the Insight.Confidence
    from the last active Insight for that symbol.
    For insights of direction InsightDirection.Up, long targets are returned and for insights of direction
    InsightDirection.Down, short targets are returned.
    If the sum of all the last active Insight per symbol is bigger than 1, it will factor down each target
    percent holdings proportionally so the sum is 1.
    It will ignore Insight that have no Insight.Confidence value.
    """


class EqualWeightingPortfolioConstructionModel(PortfolioConstructionModel):
    """
    Provides an implementation of IPortfolioConstructionModel that gives equal weighting to all
    securities. The target percent holdings of each security is 1/N where N is the number of securities. For
    insights of direction InsightDirection.Up, long targets are returned and for insights of direction
    InsightDirection.Down, short targets are returned.
    """


class MaximumSharpeRatioPortfolioOptimizer(IPortfolioOptimizer):
    """
    Provides an implementation of a portfolio optimizer that maximizes the portfolio Sharpe Ratio.
    The interval of weights in optimization method can be changed based on the long-short algorithm.
    The default model uses flat risk free rate and weight for an individual security range from -1 to 1.
    """


class MeanVarianceOptimizationPortfolioConstructionModel(PortfolioConstructionModel):
    """
    Provides an implementation of Mean-Variance portfolio optimization based on modern portfolio theory.
    The interval of weights in optimization method can be changed based on the long-short algorithm.
    The default model uses the last three months daily price to calculate the optimal weight
    with the weight range from -1 to 1 and minimize the portfolio variance with a target return of 2%
    """


class ReturnsSymbolData:
    """
    Contains returns specific to a symbol required for optimization model
    """


class ReturnsSymbolDataExtensions:
    """
    Extension methods for ReturnsSymbolData
    """


class SectorWeightingPortfolioConstructionModel(EqualWeightingPortfolioConstructionModel):
    """
    Provides an implementation of IPortfolioConstructionModel that generates percent targets based on the
    CompanyReference.IndustryTemplateCode.
    The target percent holdings of each sector is 1/S where S is the number of sectors and
    the target percent holdings of each security is 1/N where N is the number of securities of each sector.
    For insights of direction InsightDirection.Up, long targets are returned and for insights of direction
    InsightDirection.Down, short targets are returned.
    It will ignore Insight for symbols that have no CompanyReference.IndustryTemplateCode value.
    """


class BlackLittermanOptimizationPortfolioConstructionModel(PortfolioConstructionModel):
    """
    Provides an implementation of Black-Litterman portfolio optimization. The model adjusts equilibrium market
    returns by incorporating views from multiple alpha models and therefore to get the optimal risky portfolio
    reflecting those views. If insights of all alpha models have None magnitude or there are linearly dependent
    vectors in link matrix of views, the expected return would be the implied excess equilibrium return.
    The interval of weights in optimization method can be changed based on the long-short algorithm.
    The default model uses the 0.0025 as weight-on-views scalar parameter tau. The optimization method
    maximizes the Sharpe ratio with the weight range from -1 to 1.
    """


class IPortfolioOptimizer(metaclass=abc.ABCMeta):
    """
    Interface for portfolio optimization algorithms
    """


class PortfolioConstructionModel(IPortfolioConstructionModel):
    """
    Provides a base class for portfolio construction models
    """


class PortfolioBias(enum.Enum):
    """
    Specifies the bias of the portfolio (Short, Long/Short, Long)
    """


class IPortfolioConstructionModel(QuantConnect.Algorithm.Framework.INotifiedSecurityChanges, metaclass=abc.ABCMeta):
    """
    Algorithm framework model that
    """


class PortfolioConstructionModelPythonWrapper(PortfolioConstructionModel):
    """
    Provides an implementation of IPortfolioConstructionModel that wraps a PyObject object
    """


class NullPortfolioConstructionModel(PortfolioConstructionModel):
    """
    Provides an implementation of IPortfolioConstructionModel that does nothing
    """


class IPortfolioTarget(metaclass=abc.ABCMeta):
    """
    Represents a portfolio target. This may be a percentage of total portfolio value
    or it may be a fixed number of shares.
    """


class PortfolioTarget(IPortfolioTarget):
    """
    Provides an implementation of IPortfolioTarget that specifies a
    specified quantity of a security to be held by the algorithm
    """


class PortfolioTargetCollection(typing.List[IPortfolioTarget], typing.Dict[QuantConnect.Symbol, IPortfolioTarget]):
    """
    Provides a collection for managing IPortfolioTargets for each symbol
    """



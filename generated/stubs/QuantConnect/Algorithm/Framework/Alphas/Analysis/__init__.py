import abc
import typing


System_IDisposable = typing.Any


class ReadOnlySecurityValuesCollection:
    """
    Defines the security values at a given instant. This is analagous
    to TimeSlice/Slice, but decoupled from the algorithm thread and is
    intended to contain all of the information necessary to score all
    insight at this particular time step
    """


class IInsightScoreFunction(metaclass=abc.ABCMeta):
    """
    Defines a function used to determine how correct a particular insight is.
    The result of calling Evaluate is expected to be within the range [0, 1]
    where 0 is completely wrong and 1 is completely right
    """


class InsightManager(IInsightManager, System_IDisposable):
    """
    Encapsulates the storage and on-line scoring of insights.
    """


class SecurityValues:
    """
    Contains security values required by insight analysis components
    """


class InsightAnalysisContext:
    """
    Defines a context for performing analysis on a single insight
    """


class IInsightManager(System_IDisposable, metaclass=abc.ABCMeta):
    """
    Encapsulates the storage and on-line scoring of insights.
    """


class ISecurityValuesProvider(metaclass=abc.ABCMeta):
    """
    Provides a simple abstraction that returns a security's current price and volatility.
    This facilitates testing by removing the dependency of IAlgorithm on the analysis components
    """


class SecurityValuesProviderExtensions:
    """
    Provides extension methods for ISecurityValuesProvider
    """


class IInsightScoreFunctionProvider(metaclass=abc.ABCMeta):
    """
    Retrieves the registered scoring function for the specified insight/score type
    """



import QuantConnect.Algorithm.Framework.Alphas.Analysis


class DefaultInsightScoreFunctionProvider(QuantConnect.Algorithm.Framework.Alphas.Analysis.IInsightScoreFunctionProvider):
    """
    Default implementation of IInsightScoreFunctionProvider always returns the BinaryInsightScoreFunction
    """


class AlgorithmSecurityValuesProvider(QuantConnect.Algorithm.Framework.Alphas.Analysis.ISecurityValuesProvider):
    """
    Provides an implementation of ISecurityProvider that uses the SecurityManager
    to get the price for the specified symbols
    """



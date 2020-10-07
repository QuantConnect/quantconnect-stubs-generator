import QuantConnect.Securities


class Equity(QuantConnect.Securities.Security):
    """
    Equity Security Type : Extension of the underlying Security class for equity specific behaviours.
    """


class EquityExchange(QuantConnect.Securities.SecurityExchange):
    """
    Equity exchange information
    """


class EquityCache(QuantConnect.Securities.SecurityCache):
    """
    Equity cache override.
    """


class EquityDataFilter(QuantConnect.Securities.SecurityDataFilter):
    """
    Equity security type data filter
    """


class EquityHolding(QuantConnect.Securities.SecurityHolding):
    """
    Holdings class for equities securities: no specific properties here but it is a placeholder for future equities specific behaviours.
    """



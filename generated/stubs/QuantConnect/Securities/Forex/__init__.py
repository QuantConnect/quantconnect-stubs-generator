import QuantConnect.Securities


class ForexDataFilter(QuantConnect.Securities.SecurityDataFilter):
    """
    Forex packet by packet data filtering mechanism for dynamically detecting bad ticks.
    """


class ForexExchange(QuantConnect.Securities.SecurityExchange):
    """
    Forex exchange class - information and helper tools for forex exchange properties
    """


class ForexHolding(QuantConnect.Securities.SecurityHolding):
    """
    FOREX holdings implementation of the base securities class
    """


class Forex(QuantConnect.Securities.Security, QuantConnect.Securities.IBaseCurrencySymbol):
    """
    FOREX Security Object Implementation for FOREX Assets
    """


class ForexCache(QuantConnect.Securities.SecurityCache):
    """
    Forex specific caching support
    """



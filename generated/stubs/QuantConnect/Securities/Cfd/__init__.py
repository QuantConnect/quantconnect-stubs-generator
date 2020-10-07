import QuantConnect.Securities


class CfdCache(QuantConnect.Securities.SecurityCache):
    """
    CFD specific caching support
    """


class CfdDataFilter(QuantConnect.Securities.SecurityDataFilter):
    """
    CFD packet by packet data filtering mechanism for dynamically detecting bad ticks.
    """


class Cfd(QuantConnect.Securities.Security):
    """
    CFD Security Object Implementation for CFD Assets
    """


class CfdExchange(QuantConnect.Securities.SecurityExchange):
    """
    CFD exchange class - information and helper tools for CFD exchange properties
    """


class CfdHolding(QuantConnect.Securities.SecurityHolding):
    """
    CFD holdings implementation of the base securities class
    """



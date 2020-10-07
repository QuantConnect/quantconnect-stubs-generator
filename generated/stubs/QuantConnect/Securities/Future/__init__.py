import QuantConnect.Interfaces
import QuantConnect.Securities


class EmptyFutureChainProvider(QuantConnect.Interfaces.IFutureChainProvider):
    """
    An implementation of IFutureChainProvider that always returns an empty list of contracts
    """


class FutureCache(QuantConnect.Securities.SecurityCache):
    """
    Future specific caching support
    """


class FuturesExpiryFunctions:
    """
    Calculate the date of a futures expiry given an expiry month and year
    """


class FuturesExpiryUtilityFunctions:
    """
    Class to implement common functions used in FuturesExpiryFunctions
    """


class FutureExchange(QuantConnect.Securities.SecurityExchange):
    """
    Future exchange class - information and helper tools for future exchange properties
    """


class FutureHolding(QuantConnect.Securities.SecurityHolding):
    """
    Future holdings implementation of the base securities class
    """


class FutureMarginModel(QuantConnect.Securities.SecurityMarginModel):
    """
    Represents a simple margin model for margin futures. Margin file contains Initial and Maintenance margins
    """


    class MarginRequirementsEntry:
        """
        This class has no documentation.
        """


class Future(QuantConnect.Securities.Security, QuantConnect.Securities.IDerivativeSecurity):
    """
    Futures Security Object Implementation for Futures Assets
    """



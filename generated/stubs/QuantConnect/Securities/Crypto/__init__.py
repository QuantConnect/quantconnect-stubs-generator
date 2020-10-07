import QuantConnect.Securities


class Crypto(QuantConnect.Securities.Security, QuantConnect.Securities.IBaseCurrencySymbol):
    """
    Crypto Security Object Implementation for Crypto Assets
    """


class CryptoHolding(QuantConnect.Securities.SecurityHolding):
    """
    Crypto holdings implementation of the base securities class
    """


class CryptoExchange(QuantConnect.Securities.SecurityExchange):
    """
    Crypto exchange class - information and helper tools for Crypto exchange properties
    """



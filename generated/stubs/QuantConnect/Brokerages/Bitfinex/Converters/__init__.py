import typing


JsonConverter = typing.Any


class TickerConverter(JsonConverter):
    """
    A custom JSON converter for the Bitfinex Ticker class
    """


class TradeExecutionUpdateConverter(JsonConverter):
    """
    A custom JSON converter for the Bitfinex TradeExecutionUpdate class
    """


class PositionConverter(JsonConverter):
    """
    A custom JSON converter for the Bitfinex Position class
    """


class OrderConverter(JsonConverter):
    """
    A custom JSON converter for the Bitfinex Order class
    """


class WalletConverter(JsonConverter):
    """
    A custom JSON converter for the Bitfinex Wallet class
    """



import QuantConnect.Data
import QuantConnect.Data.Market
import typing


JsonConverter = typing.Any


class TiingoSymbolMapper:
    """
    Helper class to map a Lean format ticker to Tiingo format
    """


class TiingoNewsJsonConverter(JsonConverter):
    """
    Helper json converter class used to convert a list of Tiingo news data
    into List{TiingoNews}
    """


class Tiingo:
    """
    Helper class for Tiingo configuration
    """


class TiingoDailyData(TiingoPrice):
    """
    Tiingo daily price data
    https://api.tiingo.com/docs/tiingo/daily
    """


class TiingoNews(QuantConnect.Data.IndexedBaseData):
    """
    Tiingo news data
    https://api.tiingo.com/documentation/news
    """


class TiingoPrice(QuantConnect.Data.Market.TradeBar):
    """
    Tiingo daily price data
    https://api.tiingo.com/docs/tiingo/daily
    """



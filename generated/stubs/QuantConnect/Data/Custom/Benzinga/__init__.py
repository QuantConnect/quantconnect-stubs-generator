import QuantConnect.Data
import typing


JsonConverter = typing.Any


class BenzingaNews(QuantConnect.Data.IndexedBaseData):
    """
    News data powered by Benzinga - https://docs.benzinga.io/benzinga/newsfeed-v2.html
    """


class BenzingaNewsJsonConverter(JsonConverter):
    """
    Helper json converter class used to convert Benzinga news data
    into BenzingaNews
    
    An example schema of the data in a serialized format is provided
    to help you better understand this converter.
    """



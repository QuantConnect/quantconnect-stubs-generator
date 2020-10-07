import QuantConnect.Api
import enum
import typing


JsonConverter = typing.Any


class Dividend:
    """
    Dividend returned from the api
    """


class DividendList(QuantConnect.Api.RestResponse):
    """
    Collection container for a list of dividend objects
    """


class LiveAlgorithmResults(QuantConnect.Api.RestResponse):
    """
    Details a live algorithm from the "live/read" Api endpoint
    """


class LiveResultsData:
    """
    Holds information about the state and operation of the live running algorithm
    """


class Split:
    """
    Split returned from the api
    """


class SplitList(QuantConnect.Api.RestResponse):
    """
    Collection container for a list of split objects
    """


class Node:
    """
    Node class built for API endpoints nodes/read and nodes/create.
    Converts JSON properties from API response into data members for the class.
    Contains all relevant information on a Node to interact through API endpoints.
    """


class NodeList(QuantConnect.Api.RestResponse):
    """
    Rest api response wrapper for node/read, contains sets of node lists for each
    target environment. List are composed of Node objects.
    """


class CreatedNode(QuantConnect.Api.RestResponse):
    """
    Rest api response wrapper for node/create, reads in the nodes information into a
    node object
    """


class SKU:
    """
    Class for generating a SKU for a node with a given configuration
    Every SKU is made up of 3 variables:
    - Target environment (L for live, B for Backtest, R for Research)
    - CPU core count
    - Dedicated RAM (GB)
    """


class NodeType(enum.Enum):
    """
    NodeTypes enum for all possible options of target environments
    Used in conjuction with SKU class as a NodeType is a required parameter for SKU
    """


class NodePrices:
    """
    Class for deserializing node prices from node object
    """


class LiveAlgorithmApiSettingsWrapper:
    """
    Helper class to put BaseLiveAlgorithmSettings in proper format.
    """


class BaseLiveAlgorithmSettings:
    """
    Base class for settings that must be configured per Brokerage to create new algorithms via the API.
    """


class DefaultLiveAlgorithmSettings(BaseLiveAlgorithmSettings):
    """
    Default live algorithm settings
    """


class FXCMLiveAlgorithmSettings(BaseLiveAlgorithmSettings):
    """
    Algorithm setting for trading with FXCM
    """


class InteractiveBrokersLiveAlgorithmSettings(BaseLiveAlgorithmSettings):
    """
    Live algorithm settings for trading with Interactive Brokers
    """


class OandaLiveAlgorithmSettings(BaseLiveAlgorithmSettings):
    """
    Live algorithm settings for trading with Oanda
    """


class TradierLiveAlgorithmSettings(BaseLiveAlgorithmSettings):
    """
    Live algorithm settings for trading with Tradier
    """


class LiveAlgorithm(QuantConnect.Api.RestResponse):
    """
    Live algorithm instance result from the QuantConnect Rest API.
    """


class LiveList(QuantConnect.Api.RestResponse):
    """
    List of the live algorithms running which match the requested status
    """


class LiveLog(QuantConnect.Api.RestResponse):
    """
    Logs from a live algorithm
    """


class Prices:
    """
    Prices rest response wrapper
    """


class PricesList(QuantConnect.Api.RestResponse):
    """
    Collection container for a list of prices objects
    """


class LiveAlgorithmResultsJsonConverter(JsonConverter):
    """
    Custom JsonConverter for LiveResults data for live algorithms
    """



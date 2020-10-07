import abc
import enum
import typing


System_IDisposable = typing.Any
System_Exception = typing.Any
System_IEquatable = typing.Any
IsoDateTimeConverter = typing.Any
StringEnumConverter = typing.Any


QuantConnect_Brokerages_Alpaca_Markets_IDayHistoricalItems_TItem = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_IDayHistoricalItems_TItem')
QuantConnect_Brokerages_Alpaca_Markets_IHistoricalItems_TItem = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_IHistoricalItems_TItem')
QuantConnect_Brokerages_Alpaca_Markets_IAggHistoricalItems_TItem = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_IAggHistoricalItems_TItem')
QuantConnect_Brokerages_Alpaca_Markets_IQuoteBase_TExchange = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_IQuoteBase_TExchange')
QuantConnect_Brokerages_Alpaca_Markets_JsonAggHistoricalItems_TApi = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_JsonAggHistoricalItems_TApi')
QuantConnect_Brokerages_Alpaca_Markets_JsonAggHistoricalItems_TJson = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_JsonAggHistoricalItems_TJson')
QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsBase_TApi = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsBase_TApi')
QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsBase_TJson = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsBase_TJson')
QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItems_TApi = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItems_TApi')
QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItems_TJson = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItems_TJson')
QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsV1_TApi = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsV1_TApi')
QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsV1_TJson = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsV1_TJson')
QuantConnect_Brokerages_Alpaca_Markets_JsonDayHistoricalItems_TApi = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_JsonDayHistoricalItems_TApi')
QuantConnect_Brokerages_Alpaca_Markets_JsonDayHistoricalItems_TJson = typing.TypeVar('QuantConnect_Brokerages_Alpaca_Markets_JsonDayHistoricalItems_TJson')


class ThrottleParameters:
    """
    Helper class for storing parameters required for initializing rate throttler in RestClient class.
    """


class PolygonDataClient(System_IDisposable):
    """
    Provides unified type-safe access for Polygon Data API via HTTP/REST.
    """


class AlpacaTradingClient(System_IDisposable):
    """
    This class has no documentation.
    """


class FakeThrottler(IThrottler):
    """
    This class has no documentation.
    """


class SockClient(System_IDisposable):
    """
    Provides unified type-safe access for Alpaca streaming API.
    """


class IThrottler(metaclass=abc.ABCMeta):
    """
    This class has no documentation.
    """


class RateThrottler(IThrottler, System_IDisposable):
    """
    This class has no documentation.
    """


class RequestValidationException(System_Exception):
    """
    Represents exception information for request input data validation errors.
    """


class RestClientErrorException(System_Exception):
    """
    Represents Alpaca/Polygon REST API specific error information.
    """


class IClock(metaclass=abc.ABCMeta):
    """
    Encapsulates current trading date information from Alpaca REST API.
    """


class IHistoricalTrade(ITimestamps, IHistoricalBase, metaclass=abc.ABCMeta):
    """
    Encapsulates historical trade information from Polygon REST API.
    """


class IExchange(metaclass=abc.ABCMeta):
    """
    Encapsulates exchange information from Ploygon REST API.
    """


class IPortfolioHistory(metaclass=abc.ABCMeta):
    """
    Encapsulates portfolio history information from Alpaca REST API.
    """


class IAggBase(metaclass=abc.ABCMeta):
    """
    Encapsulates basic bar information for Polygon APIs.
    """


class IPortfolioHistoryItem(metaclass=abc.ABCMeta):
    """
    Encapsulates portfolio history information item from Alpaca REST API.
    """


class IStreamAgg(IAggBase, metaclass=abc.ABCMeta):
    """
    Encapsulates bar information from Polygon streaming API.
    """


class IHistoricalQuote(IQuoteBase[str], IQuoteBase[int], ITimestamps, IHistoricalBase, metaclass=abc.ABCMeta):
    """
    Encapsulates historical quote information from Polygon REST API.
    """


class IAsset(metaclass=abc.ABCMeta):
    """
    Encapsulates asset information from Alpaca REST API.
    """


class IAccountBase(metaclass=abc.ABCMeta):
    """
    Encapsulates basic account information from Alpaca streaming API.
    """


class IDayHistoricalItems(typing.Generic[QuantConnect_Brokerages_Alpaca_Markets_IDayHistoricalItems_TItem], IHistoricalItems[QuantConnect_Brokerages_Alpaca_Markets_IDayHistoricalItems_TItem], metaclass=abc.ABCMeta):
    """
    Encapsulates list of single day historical itmes from Polygon REST API.
    """


class IOrder(metaclass=abc.ABCMeta):
    """
    Encapsulates order information from Alpaca REST API.
    """


class IStreamTrade(metaclass=abc.ABCMeta):
    """
    Encapsulates trade information from Polygon streaming API.
    """


class IHistoricalItems(typing.Generic[QuantConnect_Brokerages_Alpaca_Markets_IHistoricalItems_TItem], metaclass=abc.ABCMeta):
    """
    Encapsulates read-only access for historical items in Polygon REST API.
    """


class IPosition(metaclass=abc.ABCMeta):
    """
    Encapsulates position information from Alpaca REST API.
    """


class ITimestamps(metaclass=abc.ABCMeta):
    """
    Encapsulates timestamps information from Polygon REST API.
    """


class ICalendar(metaclass=abc.ABCMeta):
    """
    Encapsulates single trading day information from Alpaca REST API.
    """


class IPositionActionStatus(metaclass=abc.ABCMeta):
    """
    Encapsulates position action status information from Alpaca REST API.
    """


class IAccountActivity(metaclass=abc.ABCMeta):
    """
    Encapsulates account activity information from Alpaca REST API.
    """


class IHistoricalBase(metaclass=abc.ABCMeta):
    """
    Encapsulates base historical information from Polygon REST API.
    """


class ILastTrade(metaclass=abc.ABCMeta):
    """
    Encapsulates last trade information from Polygon REST API.
    """


class IStreamQuote(IQuoteBase[int], metaclass=abc.ABCMeta):
    """
    Encapsulates quote information from Polygon streaming API.
    """


class ILastQuote(IStreamQuote, metaclass=abc.ABCMeta):
    """
    Encapsulates last quote information from Alpaca REST API.
    """


class IAggHistoricalItems(typing.Generic[QuantConnect_Brokerages_Alpaca_Markets_IAggHistoricalItems_TItem], IHistoricalItems[QuantConnect_Brokerages_Alpaca_Markets_IAggHistoricalItems_TItem], metaclass=abc.ABCMeta):
    """
    Encapsulates list of historical aggregates (bars) from Polygon REST API.
    """


class IOrderActionStatus(metaclass=abc.ABCMeta):
    """
    Encapsulates order action status information from Alpaca REST API.
    """


class IAccountUpdate(IAccountBase, metaclass=abc.ABCMeta):
    """
    Encapsulates account update information from Alpaca streaming API.
    """


class IQuoteBase(typing.Generic[QuantConnect_Brokerages_Alpaca_Markets_IQuoteBase_TExchange], metaclass=abc.ABCMeta):
    """
    Encapsulates basic quote information any REST API.
    """


class IAccountConfiguration(metaclass=abc.ABCMeta):
    """
    Encapsulates account configuration settings from Alpaca REST API.
    """


class IAccount(IAccountBase, metaclass=abc.ABCMeta):
    """
    Encapsulates full account information from Alpaca REST API.
    """


class ITradeUpdate(metaclass=abc.ABCMeta):
    """
    Encapsulates trade update information from Alpaca streaming API.
    """


class IAgg(IAggBase, metaclass=abc.ABCMeta):
    """
    Encapsulates bar information from Polygon REST API.
    """


class Environments:
    """
    Provides single entry point for obtaining information about different environments.
    """


class IEnvironment(metaclass=abc.ABCMeta):
    """
    Provides URLs for different APIs available for this SDK on specific environment.
    """


class LiveEnvironment(IEnvironment):
    """
    This class has no documentation.
    """


class PaperEnvironment(IEnvironment):
    """
    This class has no documentation.
    """


class HistoricalRequest(Validation.IRequest):
    """
    Encapsulates request parameters for PolygonDataClient.ListHistoricalTradesAsync(HistoricalRequest,System.Threading.CancellationToken)
    and PolygonDataClient.ListHistoricalQuotesAsync(HistoricalRequest,System.Threading.CancellationToken) method calls.
    """


class AggregationPeriod(System_IEquatable):
    """
    Encapsulates account history period request duration - value and unit pair.
    """


class NewOrderRequest(Validation.IRequest):
    """
    Encapsulates request parameters for AlpacaTradingClient.PostOrderAsync(NewOrderRequest,System.Threading.CancellationToken) call.
    """


class AssetsRequest(Validation.IRequest):
    """
    Encapsulates request parameters for AlpacaTradingClient.ListAssetsAsync(AssetsRequest,System.Threading.CancellationToken) call.
    """


class PortfolioHistoryRequest(Validation.IRequest):
    """
    Encapsulates request parameters for AlpacaTradingClient.GetPortfolioHistoryAsync(PortfolioHistoryRequest,System.Threading.CancellationToken) call.
    """


class AlpacaTradingClientConfiguration:
    """
    Configuration parameters object for AlpacaTradingClient class.
    """


class CalendarRequest(Validation.IRequest):
    """
    Encapsulates request parameters for AlpacaTradingClient.ListCalendarAsync(CalendarRequest,System.Threading.CancellationToken) call.
    """


class AggregatesRequest(Validation.IRequest):
    """
    Encapsulates request parameters for PolygonDataClient.ListAggregatesAsync(AggregatesRequest,System.Threading.CancellationToken) call.
    """


class PolygonDataClientConfiguration:
    """
    Configuration parameters object for PolygonDataClient class.
    """


class HistoryPeriod(System_IEquatable):
    """
    Encapsulates account history period request duration - value and unit pair.
    """


class ListOrdersRequest(Validation.IRequest):
    """
    Encapsulates request parameters for AlpacaTradingClient.ListOrdersAsync(ListOrdersRequest,System.Threading.CancellationToken) call.
    """


class ChangeOrderRequest(Validation.IRequest):
    """
    Encapsulates request parameters for AlpacaTradingClient.PatchOrderAsync(ChangeOrderRequest,System.Threading.CancellationToken) call.
    """


class AccountActivitiesRequest(Validation.IRequest):
    """
    Encapsulates request parameters for AlpacaTradingClient.ListAccountActivitiesAsync(AccountActivitiesRequest,System.Threading.CancellationToken) call.
    """


class SecretKey(SecurityKey):
    """
    Secret API key for Alpaca/Polygon APIs authentication.
    """


class SecurityKey(metaclass=abc.ABCMeta):
    """
    Base class for 'security key' abstraction.
    """


class ActionExtensions:
    """
    This class has no documentation.
    """


class QueryBuilder:
    """
    This class has no documentation.
    """


class UriExtensions:
    """
    This class has no documentation.
    """


class DateTimeHelper:
    """
    This class has no documentation.
    """


class DateConverter(IsoDateTimeConverter):
    """
    This class has no documentation.
    """


class TimeConverter(IsoDateTimeConverter):
    """
    This class has no documentation.
    """


class CustomTimeZone:
    """
    This class has no documentation.
    """


class ExchangeEnumConverter(StringEnumConverter):
    """
    This class has no documentation.
    """


class HttpClientExtensions:
    """
    This class has no documentation.
    """


class NullableHelper:
    """
    This class has no documentation.
    """


class EnumExtensions:
    """
    This class has no documentation.
    """


class Validation:
    """
    This class has no documentation.
    """


    class IRequest(metaclass=abc.ABCMeta):
        """
        This class has no documentation.
        """


class HttpStatusCodeExtensions:
    """
    This class has no documentation.
    """


class ListExtensions:
    """
    This class has no documentation.
    """


class JsonError:
    """
    This class has no documentation.
    """


class JsonAggHistoricalItems(typing.Generic[QuantConnect_Brokerages_Alpaca_Markets_JsonAggHistoricalItems_TApi, QuantConnect_Brokerages_Alpaca_Markets_JsonAggHistoricalItems_TJson], JsonHistoricalItems[QuantConnect_Brokerages_Alpaca_Markets_JsonAggHistoricalItems_TApi, QuantConnect_Brokerages_Alpaca_Markets_JsonAggHistoricalItems_TJson], IAggHistoricalItems[QuantConnect_Brokerages_Alpaca_Markets_JsonAggHistoricalItems_TApi]):
    """
    This class has no documentation.
    """


class JsonStreamTrade(IStreamTrade):
    """
    This class has no documentation.
    """


class JsonConnectionStatus:
    """
    This class has no documentation.
    """


class JsonClock(IClock):
    """
    This class has no documentation.
    """


class JsonOrder(IOrder):
    """
    This class has no documentation.
    """


class JsonOrderActionStatus(IOrderActionStatus):
    """
    This class has no documentation.
    """


class JsonAuthResponse:
    """
    This class has no documentation.
    """


class JsonPortfolioHistory(IPortfolioHistory):
    """
    This class has no documentation.
    """


class JsonTradeUpdate(ITradeUpdate):
    """
    This class has no documentation.
    """


class JsonStreamQuote(IStreamQuote):
    """
    This class has no documentation.
    """


class JsonAuthRequest:
    """
    This class has no documentation.
    """


    class JsonData:
        """
        This class has no documentation.
        """


class JsonLastQuote(ILastQuote):
    """
    This class has no documentation.
    """


    class Last:
        """
        This class has no documentation.
        """


class JsonAccount(IAccount):
    """
    This class has no documentation.
    """


class JsonHistoricalTrade(IHistoricalTrade):
    """
    This class has no documentation.
    """


class JsonHistoricalTradeV1(IHistoricalTrade):
    """
    This class has no documentation.
    """


class JsonChangeOrder:
    """
    This class has no documentation.
    """


class JsonHistoricalQuote(IHistoricalQuote):
    """
    This class has no documentation.
    """


class JsonHistoricalQuoteV1(IHistoricalQuote):
    """
    This class has no documentation.
    """


class JsonNewOrder:
    """
    This class has no documentation.
    """


class JsonPosition(IPosition):
    """
    This class has no documentation.
    """


class JsonUnsubscribeRequest:
    """
    This class has no documentation.
    """


class JsonBarAgg(IAgg):
    """
    This class has no documentation.
    """


class JsonAccountUpdate(IAccountUpdate):
    """
    This class has no documentation.
    """


class JsonHistoricalItemsBase(typing.Generic[QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsBase_TApi, QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsBase_TJson], IHistoricalItems[QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsBase_TApi], metaclass=abc.ABCMeta):
    """
    This class has no documentation.
    """


class JsonHistoricalItems(typing.Generic[QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItems_TApi, QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItems_TJson], JsonHistoricalItemsBase[QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItems_TApi, QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItems_TJson]):
    """
    This class has no documentation.
    """


class JsonHistoricalItemsV1(typing.Generic[QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsV1_TApi, QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsV1_TJson], JsonHistoricalItemsBase[QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsV1_TApi, QuantConnect_Brokerages_Alpaca_Markets_JsonHistoricalItemsV1_TJson], metaclass=abc.ABCMeta):
    """
    This class has no documentation.
    """


class JsonListenRequest:
    """
    This class has no documentation.
    """


    class JsonData:
        """
        This class has no documentation.
        """


class JsonPositionActionStatus(IPositionActionStatus):
    """
    This class has no documentation.
    """


class JsonNewOrderAdvancedAttributes:
    """
    This class has no documentation.
    """


class JsonAccountConfiguration(IAccountConfiguration):
    """
    This class has no documentation.
    """


class JsonMinuteAgg(IAgg):
    """
    This class has no documentation.
    """


class JsonExchange(IExchange):
    """
    This class has no documentation.
    """


class JsonAsset(IAsset):
    """
    This class has no documentation.
    """


class JsonStreamAgg(IStreamAgg):
    """
    This class has no documentation.
    """


class JsonAccountActivity(IAccountActivity):
    """
    This class has no documentation.
    """


class JsonDayHistoricalItems(typing.Generic[QuantConnect_Brokerages_Alpaca_Markets_JsonDayHistoricalItems_TApi, QuantConnect_Brokerages_Alpaca_Markets_JsonDayHistoricalItems_TJson], JsonHistoricalItems[QuantConnect_Brokerages_Alpaca_Markets_JsonDayHistoricalItems_TApi, QuantConnect_Brokerages_Alpaca_Markets_JsonDayHistoricalItems_TJson], IDayHistoricalItems[QuantConnect_Brokerages_Alpaca_Markets_JsonDayHistoricalItems_TApi]):
    """
    This class has no documentation.
    """


class JsonLastTrade(ILastTrade):
    """
    This class has no documentation.
    """


    class Last:
        """
        This class has no documentation.
        """


class JsonCalendar(ICalendar):
    """
    This class has no documentation.
    """


class HistoryPeriodUnit(enum.Enum):
    """
    Period units for portfolio history in the Alpaca REST API.
    """


class OrderStatusFilter(enum.Enum):
    """
    Order statuses filter for RestClient.ListOrdersAsync call from Alpaca REST API.
    """


class JsonAction(enum.Enum):
    """
    This class has no documentation.
    """


class AccountActivityType(enum.Enum):
    """
    Types of account activities
    """


class AggregationType(enum.Enum):
    """
    Historical data aggregation type in Alpaca REST API.
    """


class SortDirection(enum.Enum):
    """
    Supported sort directions in Alpaca REST API.
    """


class OrderType(enum.Enum):
    """
    Supported order types in Alpaca REST API.
    """


class ExchangeType(enum.Enum):
    """
    Supported exchange types in Polygon REST API.
    """


class TimeInForce(enum.Enum):
    """
    Supported order durations in Alpaca REST API.
    """


class ConnectionStatus(enum.Enum):
    """
    Authorization status for Alpaca streaming API.
    """


class DayTradeMarginCallProtection(enum.Enum):
    """
    Day trade margin call protection mode for account. See more information here:
    https://docs.alpaca.markets/user-protections/#day-trade-margin-call-dtmc-protection-at-alpaca
    """


class OrderStatus(enum.Enum):
    """
    Order status in Alpaca REST API.
    """


class AggregationPeriodUnit(enum.Enum):
    """
    Supported aggregation time windows for Alpaca REST API.
    """


class MarketDataType(enum.Enum):
    """
    Supported asset types in Polygon REST API.
    """


class AssetClass(enum.Enum):
    """
    Supported assed classes for Alpaca REST API.
    """


class AccountStatus(enum.Enum):
    """
    User account status in Alpaca REST API.
    """


class AuthStatus(enum.Enum):
    """
    Authorization status for Alpaca streaming API.
    """


class PositionSide(enum.Enum):
    """
    Position side in Alpaca REST API.
    """


class OrderSide(enum.Enum):
    """
    Order side in Alpaca REST API.
    """


class ApiVersion(enum.Enum):
    """
    REST API version number.
    """


class TradeConfirmEmail(enum.Enum):
    """
    Notification level for order fill emails.
    """


class Exchange(enum.Enum):
    """
    Exchanges supported by Alpaca REST API.
    """


class TradeEvent(enum.Enum):
    """
    Trade event in Alpaca trade update stream
    """


class OrderClass(enum.Enum):
    """
    Order class for advanced orders in the Alpaca REST API.
    """


class TickType(enum.Enum):
    """
    Conditions map type for RestClient.GetConditionMapAsync call form Polygon REST API.
    """


class TimeFrame(enum.Enum):
    """
    Supported bar duration for Alpaca REST API.
    """


class AssetStatus(enum.Enum):
    """
    Single asset status in Alpaca REST API.
    """



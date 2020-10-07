import QuantConnect.Brokerages
import QuantConnect.Interfaces
import enum


class TradierPositionsContainer:
    """
    Empty class for deserializing positions held.
    """


class TradierPositions:
    """
    Position array container.
    """


class TradierPosition:
    """
    Individual Tradier position model.
    """


class TradierEventContainer:
    """
    Tradier deserialization container for history
    """


class TradierEvents:
    """
    Events array container.
    """


class TradierEvent:
    """
    Tradier event model:
    """


class TradierEventDetail:
    """
    Common base class for events detail information:
    """


class TradierTradeEvent(TradierEventDetail):
    """
    Trade event in history for tradier:
    """


class TradierJournalEvent(TradierEventDetail):
    """
    Journal event in history:
    """


class TradierDividendEvent(TradierEventDetail):
    """
    Dividend event in history:
    """


class TradierOptionEvent(TradierEventDetail):
    """
    Option event record in history:
    """


class TradierBrokerageFactory(QuantConnect.Brokerages.BrokerageFactory):
    """
    Provides an implementations of IBrokerageFactory that produces a TradierBrokerage
    """


    class Configuration:
        """
        Gets tradier values from configuration
        """


class TradierBrokerage(QuantConnect.Brokerages.Brokerage, QuantConnect.Interfaces.IDataQueueHandler, QuantConnect.Interfaces.IHistoryProvider):
    """
    Tradier Class: IDataQueueHandler implementation
    """


    class ContingentOrderQueue:
        """
        This class has no documentation.
        """


    class TradierCachedOpenOrder:
        """
        This class has no documentation.
        """


    class TradierPlaceOrderRequest:
        """
        This class has no documentation.
        """


class TradierGainLossContainer:
    """
    Gain loss parent class for deserialization
    """


class TradierGainLossClosed:
    """
    Gain loss class
    """


class TradierGainLoss:
    """
    Account only settings for a tradier user:
    """


class TradierUserContainer:
    """
    Model for a TradierUser returned from the API.
    """


class TradierUser:
    """
    User profile array:
    """


class TradierUserAccount:
    """
    Account only settings for a tradier user:
    """


class TokenResponse:
    """
    Token response model from QuantConnect terminal
    """


class TradierBalance:
    """
    Inside "Account" User-account balance information.
    """


class TradierBalanceDetails:
    """
    Trader Balance Detail:
    """


class TradierAccountTypeSettings:
    """
    Common Account Settings.
    """


class TradierAccountTypeDayTrader(TradierAccountTypeSettings):
    """
    Account Type Day Trader Settings:
    """


class TradierAccountTypeMargin(TradierAccountTypeSettings):
    """
    Account Type Margin Settings:
    """


class TradierAccountTypeCash:
    """
    Account Type Margin Settings:
    """


class TradierTimeSeriesContainer:
    """
    Container for timeseries array
    """


class TradierTimeSeries:
    """
    One bar of historical Tradier data.
    """


class TradierQuoteContainer:
    """
    Container for quotes:
    """


class TradierQuote:
    """
    Quote data from Tradier:
    """


class TradierHistoryDataContainer:
    """
    Container for deserializing history classes
    """


class TradierHistoryBar:
    """
    "Bar" for a history unit.
    """


class TradierMarketStatus:
    """
    Current market status description
    """


class TradierCalendarStatus:
    """
    Calendar status:
    """


class TradierCalendarDayContainer:
    """
    Container for the days array:
    """


class TradierCalendarDay:
    """
    Single days properties from the calendar:
    """


class TradierCalendarDayMarketHours:
    """
    Start and finish time of market hours for this market.
    """


class TradierSearchContainer:
    """
    Tradier Search Container for Deserialization:
    """


class TradierSearchResult:
    """
    One search result from API
    """


class TradierStreamSession:
    """
    Create a new stream session
    """


class TradierStreamData:
    """
    One data packet from a tradier stream:
    """


class TradierOrdersContainer:
    """
    Order parent class for deserialization
    """


class TradierOrders:
    """
    Order container class
    """


class TradierOrder:
    """
    Intraday or pending order for user
    """


class TradierOrderDetailedContainer:
    """
    Detailed order parent class
    """


class TradierOrderResponse:
    """
    Deserialization wrapper for order response:
    """


class TradierOrderResponseError:
    """
    Errors result from an order request.
    """


class TradierOrderResponseOrder:
    """
    Order response when purchasing equity.
    """


class TradierOrderDetailed(TradierOrder):
    """
    Detailed order type.
    """


class TradierOrderLeg:
    """
    Leg of a tradier order:
    """


class TradierApiRequestType(enum.Enum):
    """
    Rate limiting categorization
    """


class TradierAccountType(enum.Enum):
    """
    Tradier account type:
    """


class TradierOrderDirection(enum.Enum):
    """
    Direction of the order
    (buy, buy_to_open, buy_to_cover, buy_to_close, sell, sell_short, sell_to_open, sell_to_close)
    """


class TradierOrderStatus(enum.Enum):
    """
    Status of the tradier order.
     (filled, canceled, open, expired, rejected, pending, partially_filled, submitted)
    """


class TradierOrderDuration(enum.Enum):
    """
    Length of the order offer.
    """


class TradierOrderClass(enum.Enum):
    """
    Class of the order.
    """


class TradierAccountStatus(enum.Enum):
    """
    Account status flag.
    """


class TradierOptionStatus(enum.Enum):
    """
    Tradier options status
    """


class TradierTimeSeriesIntervals(enum.Enum):
    """
    TradeBar windows for Tradier's data histories
    """


class TradierHistoricalDataIntervals(enum.Enum):
    """
    Historical data intervals for tradier requests:
    """


class TradierOptionType(enum.Enum):
    """
    Tradier option type
    """


class TradierOptionExpirationType(enum.Enum):
    """
    Tradier options expiration
    """


class TradierAccountClassification(enum.Enum):
    """
    Account classification
    """


class TradierEventType(enum.Enum):
    """
    Tradier event type:
    """


class TradierTradeType(enum.Enum):
    """
    Market type of the trade:
    """


class TradierOrderType(enum.Enum):
    """
    Tradier order type: (market, limit, stop, stop_limit or market) //credit, debit, even
    """


class TradierFaultContainer:
    """
    Wrapper container for fault:
    """


class TradierFault:
    """
    Tradier fault object:
    {"fault":{"faultstring":"Access Token expired","detail":{"errorcode":"keymanagement.service.access_token_expired"}}}
    """


class TradierFaultDetail:
    """
    Error code associated with this fault.
    """



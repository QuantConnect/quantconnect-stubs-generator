import QuantConnect.Interfaces
import abc
import enum
import typing


JsonConverter = typing.Any


class TimeInForceJsonConverter(JsonConverter):
    """
    Provides an implementation of JsonConverter that can deserialize TimeInForce objects
    """


class InteractiveBrokersOrderProperties(OrderProperties):
    """
    Contains additional properties and settings for an order submitted to Interactive Brokers
    """


class OrderEvent:
    """
    Order Event - Messaging class signifying a change in an order state and record the change in the user's algorithm portfolio
    """


class BinanceOrderProperties(OrderProperties):
    """
    Contains additional properties and settings for an order submitted to Binance brokerage
    """


class OrderJsonConverter(JsonConverter):
    """
    Provides an implementation of JsonConverter that can deserialize Orders
    """


class LimitOrder(Order):
    """
    Limit order type definition
    """


class OrderRequest(metaclass=abc.ABCMeta):
    """
    Represents a request to submit, update, or cancel an order
    """


class Order(metaclass=abc.ABCMeta):
    """
    Order struct for placing new trade
    """


class OrderRequestType(enum.Enum):
    """
    Specifies the type of OrderRequest
    """


class OrderExtensions:
    """
    Provides extension methods for the Order class and for the OrderStatus enumeration
    """


class GDAXOrderProperties(OrderProperties):
    """
    Contains additional properties and settings for an order submitted to GDAX brokerage
    """


class OrderResponseErrorCode(enum.Enum):
    """
    Error detail code
    """


class BitfinexOrderProperties(OrderProperties):
    """
    Contains additional properties and settings for an order submitted to Bitfinex brokerage
    """


class TimeInForce(QuantConnect.Interfaces.ITimeInForceHandler, metaclass=abc.ABCMeta):
    """
    Time In Force - defines the length of time over which an order will continue working before it is canceled
    """


class OrderTicket:
    """
    Provides a single reference to an order for the algorithm to maintain. As the order gets
    updated this ticket will also get updated
    """


class OrderSubmissionData:
    """
    The purpose of this class is to store time and price information
    available at the time an order was submitted.
    """


class OrderResponse:
    """
    Represents a response to an OrderRequest. See OrderRequest.Response property for
    a specific request's response value
    """


class MarketOnCloseOrder(Order):
    """
    Market on close order type - submits a market order on exchange close
    """


class SubmitOrderRequest(OrderRequest):
    """
    Defines a request to submit a new order
    """


class StopLimitOrder(Order):
    """
    Stop Market Order Type Definition
    """


class OrderSizing:
    """
    Provides methods for computing a maximum order size.
    """


class UpdateOrderRequest(OrderRequest):
    """
    Defines a request to update an order's values
    """


class MarketOrder(Order):
    """
    Market order type definition
    """


class OrderRequestStatus(enum.Enum):
    """
    Specifies the status of a request
    """


class CancelOrderRequest(OrderRequest):
    """
    Defines a request to cancel an order
    """


class OrderProperties(QuantConnect.Interfaces.IOrderProperties):
    """
    Contains additional properties and settings for an order
    """


class OrderType(enum.Enum):
    """
    Type of the order: market, limit or stop
    """


class OrderDirection(enum.Enum):
    """
    Direction of the order
    """


class OrderStatus(enum.Enum):
    """
    Fill status of the order class.
    """


class OptionExerciseOrder(Order):
    """
    Option exercise order type definition
    """


class MarketOnOpenOrder(Order):
    """
    Market on Open order type, submits a market order when the exchange opens
    """


class StopMarketOrder(Order):
    """
    Stop Market Order Type Definition
    """


class OrderError(enum.Enum):
    """
    Specifies the possible error states during presubmission checks
    """


class OrderField(enum.Enum):
    """
    Specifies an order field that does not apply to all order types
    """


class UpdateOrderFields:
    """
    Specifies the data in an order to be updated
    """



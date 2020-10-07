import enum
import typing


System_IEquatable = typing.Any
IValidatableObject = typing.Any


class InlineResponse4002(System_IEquatable, IValidatableObject):
    """
    InlineResponse4002
    """


class Position(System_IEquatable, IValidatableObject):
    """
    The specification of a Position within an Account.
    """


class StopOrderReason(enum.Enum):
    """
    The reason that the Stop Order was initiated
    """


class InlineResponse4041(System_IEquatable, IValidatableObject):
    """
    InlineResponse4041
    """


class UnitsAvailable(System_IEquatable, IValidatableObject):
    """
    Representation of how many units of an Instrument are available to be traded by an Order depending on its postionFill option.
    """


class InlineResponse2003(System_IEquatable, IValidatableObject):
    """
    InlineResponse2003
    """


class StopLossOrderRejectTransaction(System_IEquatable, IValidatableObject):
    """
    A StopLossOrderRejectTransaction represents the rejection of the creation of a StopLoss Order.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"STOP_LOSS_ORDER_REJECT\" in a StopLossOrderRejectTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the StopLoss Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for StopLoss Orders.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Stop Loss Order was initiated
        """


    class RejectReasonEnum(enum.Enum):
        """
        The reason that the Reject Transaction was created
        """


class InlineResponse20023(System_IEquatable, IValidatableObject):
    """
    InlineResponse20023
    """


class InlineResponse20026(System_IEquatable, IValidatableObject):
    """
    InlineResponse20026
    """


class LimitOrder(System_IEquatable, IValidatableObject):
    """
    A LimitOrder is an order that is created with a price threshold, and will only be filled by a price that is equal to or better than the threshold.
    """


    class StateEnum(enum.Enum):
        """
        The current state of the Order.
        """


    class TypeEnum(enum.Enum):
        """
        The type of the Order. Always set to \"LIMIT\" for Limit Orders.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the Limit Order.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


class OrderRequest(System_IEquatable, IValidatableObject):
    """
    The base Order specification used when requesting that an Order be created. Each specific Order-type extends this definition.
    """


class MarketOrderDelayedTradeClose(System_IEquatable, IValidatableObject):
    """
    Details for the Market Order extensions specific to a Market Order placed with the intent of fully closing a specific open trade that should have already been closed but wasn&#39;t due to halted market conditions
    """


class OrderClientExtensionsModifyTransaction(System_IEquatable, IValidatableObject):
    """
    A OrderClientExtensionsModifyTransaction represents the modification of an Order&#39;s Client Extensions.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"ORDER_CLIENT_EXTENSIONS_MODIFY\" for a OrderClienteExtensionsModifyTransaction.
        """


class Order(System_IEquatable, IValidatableObject):
    """
    The base Order definition specifies the properties that are common to all Orders.
    """


    class StateEnum(enum.Enum):
        """
        The current state of the Order.
        """


class MarketOrderReason(enum.Enum):
    """
    The reason that the Market Order was created
    """


class TakeProfitOrderRejectTransaction(System_IEquatable, IValidatableObject):
    """
    A TakeProfitOrderRejectTransaction represents the rejection of the creation of a TakeProfit Order.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"TAKE_PROFIT_ORDER_REJECT\" in a TakeProfitOrderRejectTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the TakeProfit Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for TakeProfit Orders.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Take Profit Order was initiated
        """


    class RejectReasonEnum(enum.Enum):
        """
        The reason that the Reject Transaction was created
        """


class DelayedTradeClosureTransaction(System_IEquatable, IValidatableObject):
    """
    A DelayedTradeClosure Transaction is created administratively to indicate open trades that should have been closed but weren&#39;t because the open trades&#39; instruments were untradeable at the time. Open trades listed in this transaction will be closed once their respective instruments become tradeable.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"DELAYED_TRADE_CLOSURE\" for an DelayedTradeClosureTransaction.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason for the delayed trade closure
        """


class InlineResponse20025(System_IEquatable, IValidatableObject):
    """
    InlineResponse20025
    """


class TransactionHeartbeat(System_IEquatable, IValidatableObject):
    """
    A TransactionHeartbeat object is injected into the Transaction stream to ensure that the HTTP connection remains active.
    """


class TrailingStopLossOrderTransaction(System_IEquatable, IValidatableObject):
    """
    A TrailingStopLossOrderTransaction represents the creation of a TrailingStopLoss Order in the user&#39;s Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"TRAILING_STOP_LOSS_ORDER\" in a TrailingStopLossOrderTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the TrailingStopLoss Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for TrailingStopLoss Orders.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Trailing Stop Loss Order was initiated
        """


class InlineResponse400(System_IEquatable, IValidatableObject):
    """
    InlineResponse400
    """


class PositionFinancing(System_IEquatable, IValidatableObject):
    """
    OpenTradeFinancing is used to pay/collect daily financing charge for a Position within an Account
    """


class InlineResponse20017(System_IEquatable, IValidatableObject):
    """
    InlineResponse20017
    """


    class TypeEnum(enum.Enum):
        """
        A filter that can be used when fetching Transactions
        """


class InlineResponse4046(System_IEquatable, IValidatableObject):
    """
    InlineResponse4046
    """


class StopLossDetails(System_IEquatable, IValidatableObject):
    """
    StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade&#39;s dependent Stop Loss Order is modified directly through the Trade.
    """


    class TimeInForceEnum(enum.Enum):
        """
        The time in force for the created Stop Loss Order. This may only be GTC, GTD or GFD.
        """


class StopOrderTransaction(System_IEquatable, IValidatableObject):
    """
    A StopOrderTransaction represents the creation of a Stop Order in the user&#39;s Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"STOP_ORDER\" in a StopOrderTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the Stop Order.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Stop Order was initiated
        """


class ClientComment(System_IEquatable, IValidatableObject):
    """
    A client-provided comment that can contain any data and may be assigned to their Orders or Trades. Comments are typically used to provide extra context or meaning to an Order or Trade.
    """


class ClientID(System_IEquatable, IValidatableObject):
    """
    A client-provided identifier, used by clients to refer to their Orders or Trades with an identifier that they have provided.
    """


class Transaction(System_IEquatable, IValidatableObject):
    """
    The base Transaction specification. Specifies properties that are common between all Transaction.
    """


class OrderType(enum.Enum):
    """
    The type of the Order.
    """


class CandlestickGranularity(enum.Enum):
    """
    The granularity of a candlestick
    """


class OrderFillReason(enum.Enum):
    """
    The reason that an Order was filled
    """


class MarketIfTouchedOrderRequest(System_IEquatable, IValidatableObject):
    """
    A MarketIfTouchedOrderRequest specifies the parameters that may be set when creating a Market-if-Touched Order.
    """


    class TypeEnum(enum.Enum):
        """
        The type of the Order to Create. Must be set to \"MARKET_IF_TOUCHED\" when creating a Market If Touched Order.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the MarketIfTouched Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for MarketIfTouched Orders.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


class LiquidityRegenerationSchedule(System_IEquatable, IValidatableObject):
    """
    A LiquidityRegenerationSchedule indicates how liquidity that is used when filling an Order for an instrument is regenerated following the fill.  A liquidity regeneration schedule will be in effect until the timestamp of its final step, but may be replaced by a schedule created for an Order of the same instrument that is filled while it is still in effect.
    """


class OrderClientExtensionsModifyRejectTransaction(System_IEquatable, IValidatableObject):
    """
    A OrderClientExtensionsModifyRejectTransaction represents the rejection of the modification of an Order&#39;s Client Extensions.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT\" for a OrderClientExtensionsModifyRejectTransaction.
        """


    class RejectReasonEnum(enum.Enum):
        """
        The reason that the Reject Transaction was created
        """


class InlineResponse20029(System_IEquatable, IValidatableObject):
    """
    InlineResponse20029
    """


    class GranularityEnum(enum.Enum):
        """
        The granularity of the candlesticks provided.
        """


class PriceStatus(enum.Enum):
    """
    The status of the Price.
    """


class LimitOrderRequest(System_IEquatable, IValidatableObject):
    """
    A LimitOrderRequest specifies the parameters that may be set when creating a Limit Order.
    """


    class TypeEnum(enum.Enum):
        """
        The type of the Order to Create. Must be set to \"LIMIT\" when creating a Market Order.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the Limit Order.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


class OrderState(enum.Enum):
    """
    The current state of the Order.
    """


class ResetResettablePLTransaction(System_IEquatable, IValidatableObject):
    """
    A ResetResettablePLTransaction represents the resetting of the Account&#39;s resettable PL counters.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"RESET_RESETTABLE_PL\" for a ResetResettablePLTransaction.
        """


class InlineResponse20010(System_IEquatable, IValidatableObject):
    """
    InlineResponse20010
    """


class InlineResponse20021(System_IEquatable, IValidatableObject):
    """
    InlineResponse20021
    """


class Instrument(System_IEquatable, IValidatableObject):
    """
    Full specification of an Instrument.
    """


    class TypeEnum(enum.Enum):
        """
        The type of the Instrument
        """


class TrailingStopLossOrder(System_IEquatable, IValidatableObject):
    """
    A TrailingStopLossOrder is an order that is linked to an open Trade and created with a price distance. The price distance is used to calculate a trailing stop value for the order that is in the losing direction from the market price at the time of the order&#39;s creation. The trailing stop value will follow the market price as it moves in the winning direction, and the order will filled (closing the Trade) by the first price that is equal to or worse than the trailing stop value. A TrailingStopLossOrder cannot be used to open a new Position.
    """


    class StateEnum(enum.Enum):
        """
        The current state of the Order.
        """


    class TypeEnum(enum.Enum):
        """
        The type of the Order. Always set to \"TRAILING_STOP_LOSS\" for Trailing Stop Loss Orders.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the TrailingStopLoss Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for TrailingStopLoss Orders.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


class TradeSummary(System_IEquatable, IValidatableObject):
    """
    The summary of a Trade within an Account. This representation does not provide the full details of the Trade&#39;s dependent Orders.
    """


    class StateEnum(enum.Enum):
        """
        The current state of the Trade.
        """


class LimitOrderTransaction(System_IEquatable, IValidatableObject):
    """
    A LimitOrderTransaction represents the creation of a Limit Order in the user&#39;s Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"LIMIT_ORDER\" in a LimitOrderTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the Limit Order.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Limit Order was initiated
        """


class TrailingStopLossOrderReason(enum.Enum):
    """
    The reason that the Trailing Stop Loss Order was initiated
    """


class TakeProfitOrderTransaction(System_IEquatable, IValidatableObject):
    """
    A TakeProfitOrderTransaction represents the creation of a TakeProfit Order in the user&#39;s Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"TAKE_PROFIT_ORDER\" in a TakeProfitOrderTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the TakeProfit Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for TakeProfit Orders.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Take Profit Order was initiated
        """


class OrderID(System_IEquatable, IValidatableObject):
    """
    The Order&#39;s identifier, unique within the Order&#39;s Account.
    """


class SetTradeClientExtensionsBody(System_IEquatable, IValidatableObject):
    """
    SetTradeClientExtensionsBody
    """


class InlineResponse200(System_IEquatable, IValidatableObject):
    """
    InlineResponse200
    """


class ReplaceOrderBody(System_IEquatable, IValidatableObject):
    """
    ReplaceOrderBody
    """


class TransactionID(System_IEquatable, IValidatableObject):
    """
    The unique Transaction identifier within each Account.
    """


class InlineResponse4043(System_IEquatable, IValidatableObject):
    """
    InlineResponse4043
    """


class InlineResponse20012(System_IEquatable, IValidatableObject):
    """
    InlineResponse20012
    """


class InlineResponse20028(System_IEquatable, IValidatableObject):
    """
    InlineResponse20028
    """


class OpenTradeFinancing(System_IEquatable, IValidatableObject):
    """
    OpenTradeFinancing is used to pay/collect daily financing charge for an open Trade within an Account
    """


class TransactionRejectReason(enum.Enum):
    """
    The reason that a Transaction was rejected.
    """


class ClientTag(System_IEquatable, IValidatableObject):
    """
    A client-provided tag that can contain any data and may be assigned to their Orders or Trades. Tags are typically used to associate groups of Trades and/or Orders together.
    """


class TimeInForce(enum.Enum):
    """
    The time-in-force of an Order. TimeInForce describes how long an Order should remain pending before being automatically cancelled by the execution system.
    """


class CloseTransaction(System_IEquatable, IValidatableObject):
    """
    A CloseTransaction represents the closing of an Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"CLOSE\" in a CloseTransaction.
        """


class LiquidityRegenerationScheduleStep(System_IEquatable, IValidatableObject):
    """
    A liquidity regeneration schedule Step indicates the amount of bid and ask liquidity that is used by the Account at a certain time. These amounts will only change at the timestamp of the following step.
    """


class MarginCallExtendTransaction(System_IEquatable, IValidatableObject):
    """
    A MarginCallExtendTransaction is created when the margin call state for an Account has been extended.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"MARGIN_CALL_EXTEND\" for an MarginCallExtendTransaction.
        """


class DailyFinancingTransaction(System_IEquatable, IValidatableObject):
    """
    A DailyFinancingTransaction represents the daily payment/collection of financing for an Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"DAILY_FINANCING\" for a DailyFinancingTransaction.
        """


    class AccountFinancingModeEnum(enum.Enum):
        """
        The account financing mode at the time of the daily financing.
        """


class InlineResponse4044(System_IEquatable, IValidatableObject):
    """
    InlineResponse4044
    """


class CreateTransaction(System_IEquatable, IValidatableObject):
    """
    A CreateTransaction represents the creation of an Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"CREATE\" in a CreateTransaction.
        """


class AccountProperties(System_IEquatable, IValidatableObject):
    """
    Properties related to an Account.
    """


class InlineResponse20011(System_IEquatable, IValidatableObject):
    """
    InlineResponse20011
    """


class OrderSpecifier(System_IEquatable, IValidatableObject):
    """
    The specification of an Order as referred to by clients
    """


class TakeProfitOrderReason(enum.Enum):
    """
    The reason that the Take Profit Order was initiated
    """


class OrderIdentifier(System_IEquatable, IValidatableObject):
    """
    An OrderIdentifier is used to refer to an Order, and contains both the OrderID and the ClientOrderID.
    """


class InlineResponse2009(System_IEquatable, IValidatableObject):
    """
    InlineResponse2009
    """


class TransactionFilter(enum.Enum):
    """
    A filter that can be used when fetching Transactions
    """


class MarketOrderMarginCloseoutReason(enum.Enum):
    """
    The reason that the Market Order was created to perform a margin closeout
    """


class StopLossOrderTransaction(System_IEquatable, IValidatableObject):
    """
    A StopLossOrderTransaction represents the creation of a StopLoss Order in the user&#39;s Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"STOP_LOSS_ORDER\" in a StopLossOrderTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the StopLoss Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for StopLoss Orders.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Stop Loss Order was initiated
        """


class StopOrderRequest(System_IEquatable, IValidatableObject):
    """
    A StopOrderRequest specifies the parameters that may be set when creating a Stop Order.
    """


    class TypeEnum(enum.Enum):
        """
        The type of the Order to Create. Must be set to \"STOP\" when creating a Stop Order.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the Stop Order.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


class TransferFundsTransaction(System_IEquatable, IValidatableObject):
    """
    A TransferFundsTransaction represents the transfer of funds in/out of an Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"TRANSFER_FUNDS\" in a TransferFundsTransaction.
        """


    class FundingReasonEnum(enum.Enum):
        """
        The reason that an Account is being funded.
        """


class TakeProfitOrder(System_IEquatable, IValidatableObject):
    """
    A TakeProfitOrder is an order that is linked to an open Trade and created with a price threshold. The Order will be filled (closing the Trade) by the first price that is equal to or better than the threshold. A TakeProfitOrder cannot be used to open a new Position.
    """


    class StateEnum(enum.Enum):
        """
        The current state of the Order.
        """


    class TypeEnum(enum.Enum):
        """
        The type of the Order. Always set to \"TAKE_PROFIT\" for Take Profit Orders.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the TakeProfit Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for TakeProfit Orders.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


class SetOrderClientExtensionsBody(System_IEquatable, IValidatableObject):
    """
    SetOrderClientExtensionsBody
    """


class InlineResponse20013(System_IEquatable, IValidatableObject):
    """
    InlineResponse20013
    """


class OrderCancelReason(enum.Enum):
    """
    The reason that an Order was cancelled.
    """


class ClientConfigureRejectTransaction(System_IEquatable, IValidatableObject):
    """
    A ClientConfigureRejectTransaction represents the reject of configuration of an Account by a client.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"CLIENT_CONFIGURE_REJECT\" in a ClientConfigureRejectTransaction.
        """


    class RejectReasonEnum(enum.Enum):
        """
        The reason that the Reject Transaction was created
        """


class InlineResponse4001(System_IEquatable, IValidatableObject):
    """
    InlineResponse4001
    """


class LimitOrderReason(enum.Enum):
    """
    The reason that the Limit Order was initiated
    """


class UserInfoExternal(System_IEquatable, IValidatableObject):
    """
    A representation of user information, as available to external (3rd party) clients.
    """


class InlineResponse20019(System_IEquatable, IValidatableObject):
    """
    InlineResponse20019
    """


class CreateOrderBody(System_IEquatable, IValidatableObject):
    """
    CreateOrderBody
    """


class MarketIfTouchedOrderTransaction(System_IEquatable, IValidatableObject):
    """
    A MarketIfTouchedOrderTransaction represents the creation of a MarketIfTouched Order in the user&#39;s Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"MARKET_IF_TOUCHED_ORDER\" in a MarketIfTouchedOrderTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the MarketIfTouched Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for MarketIfTouched Orders.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Market-if-touched Order was initiated
        """


class FundingReason(enum.Enum):
    """
    The reason that an Account is being funded.
    """


class TakeProfitDetails(System_IEquatable, IValidatableObject):
    """
    TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade&#39;s dependent Take Profit Order is modified directly through the Trade.
    """


    class TimeInForceEnum(enum.Enum):
        """
        The time in force for the created Take Profit Order. This may only be GTC, GTD or GFD.
        """


class PriceBucket(System_IEquatable, IValidatableObject):
    """
    A Price Bucket represents a price available for an amount of liquidity
    """


class TradeClientExtensionsModifyTransaction(System_IEquatable, IValidatableObject):
    """
    A TradeClientExtensionsModifyTransaction represents the modification of a Trade&#39;s Client Extensions.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"TRADE_CLIENT_EXTENSIONS_MODIFY\" for a TradeClientExtensionsModifyTransaction.
        """


class TradeState(enum.Enum):
    """
    The current state of the Trade.
    """


class MarketOrder(System_IEquatable, IValidatableObject):
    """
    A MarketOrder is an order that is filled immediately upon creation using the current market price.
    """


    class StateEnum(enum.Enum):
        """
        The current state of the Order.
        """


    class TypeEnum(enum.Enum):
        """
        The type of the Order. Always set to \"MARKET\" for Market Orders.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the Market Order. Restricted to FOK or IOC for a MarketOrder.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


class AccountID(System_IEquatable, IValidatableObject):
    """
    The string representation of an Account Identifier.
    """


class MarginCallExitTransaction(System_IEquatable, IValidatableObject):
    """
    A MarginCallExitnterTransaction is created when an Account leaves the margin call state.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"MARGIN_CALL_EXIT\" for an MarginCallExitTransaction.
        """


class AccountChanges(System_IEquatable, IValidatableObject):
    """
    An AccountChanges Object is used to represent the changes to an Account&#39;s Orders, Trades and Positions since a specified Account TransactionID in the past.
    """


class InlineResponse4042(System_IEquatable, IValidatableObject):
    """
    InlineResponse4042
    """


class CalculatedPositionState(System_IEquatable, IValidatableObject):
    """
    The dynamic (calculated) state of a Position
    """


class PositionSide(System_IEquatable, IValidatableObject):
    """
    The representation of a Position for a single direction (long or short).
    """


class AccountSummary(System_IEquatable, IValidatableObject):
    """
    A summary representation of a client&#39;s Account. The AccountSummary does not provide to full specification of pending Orders, open Trades and Positions.
    """


class TradeOpen(System_IEquatable, IValidatableObject):
    """
    A TradeOpen object represents a Trade for an instrument that was opened in an Account. It is found embedded in Transactions that affect the position of an instrument in the Account, specifically the OrderFill Transaction.
    """


class InlineResponse20016(System_IEquatable, IValidatableObject):
    """
    InlineResponse20016
    """


class ClosePositionBody(System_IEquatable, IValidatableObject):
    """
    ClosePositionBody
    """


class MarketOrderPositionCloseout(System_IEquatable, IValidatableObject):
    """
    A MarketOrderPositionCloseout specifies the extensions to a Market Order when it has been created to closeout a specific Position.
    """


class DateTime(System_IEquatable, IValidatableObject):
    """
    A date and time value using either RFC3339 or UNIX time representation.
    """


class UserSpecifier(System_IEquatable, IValidatableObject):
    """
    The specifier that refers to a User
    """


class OrderCancelTransaction(System_IEquatable, IValidatableObject):
    """
    An OrderCancelTransaction represents the cancellation of an Order in the client&#39;s Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"ORDER_CANCEL\" for an OrderCancelTransaction.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Order was cancelled.
        """


class InlineResponse20015(System_IEquatable, IValidatableObject):
    """
    InlineResponse20015
    """


class StopLossOrder(System_IEquatable, IValidatableObject):
    """
    A StopLossOrder is an order that is linked to an open Trade and created with a price threshold. The Order will be filled (closing the Trade) by the first price that is equal to or worse than the threshold. A StopLossOrder cannot be used to open a new Position.
    """


    class StateEnum(enum.Enum):
        """
        The current state of the Order.
        """


    class TypeEnum(enum.Enum):
        """
        The type of the Order. Always set to \"STOP_LOSS\" for Stop Loss Orders.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the StopLoss Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for StopLoss Orders.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


class TradeClientExtensionsModifyRejectTransaction(System_IEquatable, IValidatableObject):
    """
    A TradeClientExtensionsModifyRejectTransaction represents the rejection of the modification of a Trade&#39;s Client Extensions.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT\" for a TradeClientExtensionsModifyRejectTransaction.
        """


    class RejectReasonEnum(enum.Enum):
        """
        The reason that the Reject Transaction was created
        """


class TradeReduce(System_IEquatable, IValidatableObject):
    """
    A TradeReduce object represents a Trade for an instrument that was reduced (either partially or fully) in an Account. It is found embedded in Transactions that affect the position of an instrument in the account, specifically the OrderFill Transaction.
    """


class MarginCallEnterTransaction(System_IEquatable, IValidatableObject):
    """
    A MarginCallEnterTransaction is created when an Account enters the margin call state.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"MARGIN_CALL_ENTER\" for an MarginCallEnterTransaction.
        """


class MarketOrderTradeClose(System_IEquatable, IValidatableObject):
    """
    A MarketOrderTradeClose specifies the extensions to a Market Order that has been created specifically to close a Trade.
    """


class MarketIfTouchedOrderReason(enum.Enum):
    """
    The reason that the Market-if-touched Order was initiated
    """


class AcceptDatetimeFormat(enum.Enum):
    """
    DateTime header
    """


class InlineResponse2005(System_IEquatable, IValidatableObject):
    """
    InlineResponse2005
    """


class InlineResponse2004(System_IEquatable, IValidatableObject):
    """
    InlineResponse2004
    """


class AccountFinancingMode(enum.Enum):
    """
    The financing mode of an Account
    """


class MarketOrderRequest(System_IEquatable, IValidatableObject):
    """
    A MarketOrderRequest specifies the parameters that may be set when creating a Market Order.
    """


    class TypeEnum(enum.Enum):
        """
        The type of the Order to Create. Must be set to \"MARKET\" when creating a Market Order.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the Market Order. Restricted to FOK or IOC for a MarketOrder.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


class MarketOrderRejectTransaction(System_IEquatable, IValidatableObject):
    """
    A MarketOrderRejectTransaction represents the rejection of the creation of a Market Order.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"MARKET_ORDER_REJECT\" in a MarketOrderRejectTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the Market Order. Restricted to FOK or IOC for a MarketOrder.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Market Order was created
        """


    class RejectReasonEnum(enum.Enum):
        """
        The reason that the Reject Transaction was created
        """


class InlineResponse20014(System_IEquatable, IValidatableObject):
    """
    InlineResponse20014
    """


class ReopenTransaction(System_IEquatable, IValidatableObject):
    """
    A ReopenTransaction represents the re-opening of a closed Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"REOPEN\" in a ReopenTransaction.
        """


class StopLossOrderRequest(System_IEquatable, IValidatableObject):
    """
    A StopLossOrderRequest specifies the parameters that may be set when creating a Stop Loss Order.
    """


    class TypeEnum(enum.Enum):
        """
        The type of the Order to Create. Must be set to \"STOP_LOSS\" when creating a Stop Loss Order.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the StopLoss Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for StopLoss Orders.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


class StopOrderRejectTransaction(System_IEquatable, IValidatableObject):
    """
    A StopOrderRejectTransaction represents the rejection of the creation of a Stop Order.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"STOP_ORDER_REJECT\" in a StopOrderRejectTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the Stop Order.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Stop Order was initiated
        """


    class RejectReasonEnum(enum.Enum):
        """
        The reason that the Reject Transaction was created
        """


class InlineResponse20020(System_IEquatable, IValidatableObject):
    """
    The response body for the Transaction Stream uses chunked transfer encoding.  Each chunk contains Transaction and/or TransactionHeartbeat objects encoded as JSON.  Each JSON object is serialized into a single line of text, and multiple objects found in the same chunk are separated by newlines. TransactionHeartbeats are sent every 5 seconds.
    """


class InlineResponse201(System_IEquatable, IValidatableObject):
    """
    InlineResponse201
    """


class InlineResponse2001(System_IEquatable, IValidatableObject):
    """
    InlineResponse2001
    """


class DecimalNumber(System_IEquatable, IValidatableObject):
    """
    The string representation of a decimal number.
    """


class TradeID(System_IEquatable, IValidatableObject):
    """
    The Trade&#39;s identifier, unique within the Trade&#39;s Account.
    """


class TradeSpecifier(System_IEquatable, IValidatableObject):
    """
    The identification of a Trade as referred to by clients
    """


class MarketIfTouchedOrderRejectTransaction(System_IEquatable, IValidatableObject):
    """
    A MarketIfTouchedOrderRejectTransaction represents the rejection of the creation of a MarketIfTouched Order.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"MARKET_IF_TOUCHED_ORDER_REJECT\" in a MarketIfTouchedOrderRejectTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the MarketIfTouched Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for MarketIfTouched Orders.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Market-if-touched Order was initiated
        """


    class RejectReasonEnum(enum.Enum):
        """
        The reason that the Reject Transaction was created
        """


class InlineResponse20024(System_IEquatable, IValidatableObject):
    """
    InlineResponse20024
    """


class InlineResponse2002(System_IEquatable, IValidatableObject):
    """
    InlineResponse2002
    """


class ConfigureAccountBody(System_IEquatable, IValidatableObject):
    """
    ConfigureAccountBody
    """


class InlineResponse4003(System_IEquatable, IValidatableObject):
    """
    InlineResponse4003
    """


class TakeProfitOrderRequest(System_IEquatable, IValidatableObject):
    """
    A TakeProfitOrderRequest specifies the parameters that may be set when creating a Take Profit Order.
    """


    class TypeEnum(enum.Enum):
        """
        The type of the Order to Create. Must be set to \"TAKE_PROFIT\" when creating a Take Profit Order.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the TakeProfit Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for TakeProfit Orders.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


class InlineResponse2007(System_IEquatable, IValidatableObject):
    """
    InlineResponse2007
    """


class OrderPositionFill(enum.Enum):
    """
    Specification of how Positions in the Account are modified when the Order is filled.
    """


class StopOrder(System_IEquatable, IValidatableObject):
    """
    A StopOrder is an order that is created with a price threshold, and will only be filled by a price that is equal to or worse than the threshold.
    """


    class StateEnum(enum.Enum):
        """
        The current state of the Order.
        """


    class TypeEnum(enum.Enum):
        """
        The type of the Order. Always set to \"STOP\" for Stop Orders.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the Stop Order.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


class InstrumentType(enum.Enum):
    """
    The type of an Instrument.
    """


class LimitOrderRejectTransaction(System_IEquatable, IValidatableObject):
    """
    A LimitOrderRejectTransaction represents the rejection of the creation of a Limit Order.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"LIMIT_ORDER_REJECT\" in a LimitOrderRejectTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the Limit Order.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Limit Order was initiated
        """


    class RejectReasonEnum(enum.Enum):
        """
        The reason that the Reject Transaction was created
        """


class ClientConfigureTransaction(System_IEquatable, IValidatableObject):
    """
    A ClientConfigureTransaction represents the configuration of an Account by a client.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"CLIENT_CONFIGURE\" in a ClientConfigureTransaction.
        """


class InlineResponse4004(System_IEquatable, IValidatableObject):
    """
    InlineResponse4004
    """


class TrailingStopLossOrderRequest(System_IEquatable, IValidatableObject):
    """
    A TrailingStopLossOrderRequest specifies the parameters that may be set when creating a Trailing Stop Loss Order.
    """


    class TypeEnum(enum.Enum):
        """
        The type of the Order to Create. Must be set to \"TRAILING_STOP_LOSS\" when creating a Trailng Stop Loss Order.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the TrailingStopLoss Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for TrailingStopLoss Orders.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


class SetTradeDependentOrdersBody(System_IEquatable, IValidatableObject):
    """
    SetTradeDependentOrdersBody
    """


class AccountUnits(System_IEquatable, IValidatableObject):
    """
    The string representation of a quantity of an Account&#39;s home currency.
    """


class InstrumentName(System_IEquatable, IValidatableObject):
    """
    Instrument name identifier. Used by clients to refer to an Instrument.
    """


class InlineResponse2011(System_IEquatable, IValidatableObject):
    """
    InlineResponse2011
    """


class Trade(System_IEquatable, IValidatableObject):
    """
    The specification of a Trade within an Account. This includes the full representation of the Trade&#39;s dependent Orders in addition to the IDs of those Orders.
    """


    class StateEnum(enum.Enum):
        """
        The current state of the Trade.
        """


class UserInfo(System_IEquatable, IValidatableObject):
    """
    A representation of user information, as provided to the user themself.
    """


class Currency(System_IEquatable, IValidatableObject):
    """
    Currency name identifier. Used by clients to refer to currencies.
    """


class MarketOrderTransaction(System_IEquatable, IValidatableObject):
    """
    A MarketOrderTransaction represents the creation of a Market Order in the user&#39;s account. A Market Order is an Order that is filled immediately at the current market price. Market Orders can be specialized when they are created to accomplish a specific task: to close a Trade, to closeout a Position or to particiate in in a Margin closeout.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"MARKET_ORDER\" in a MarketOrderTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the Market Order. Restricted to FOK or IOC for a MarketOrder.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Market Order was created
        """


class MarketIfTouchedOrder(System_IEquatable, IValidatableObject):
    """
    A MarketIfTouchedOrder is an order that is created with a price threshold, and will only be filled by a market price that is touches or crosses the threshold.
    """


    class StateEnum(enum.Enum):
        """
        The current state of the Order.
        """


    class TypeEnum(enum.Enum):
        """
        The type of the Order. Always set to \"MARKET_IF_TOUCHED\" for Market If Touched Orders.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the MarketIfTouched Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for MarketIfTouched Orders.
        """


    class PositionFillEnum(enum.Enum):
        """
        Specification of how Positions in the Account are modified when the Order is filled.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


class InlineResponse4006(System_IEquatable, IValidatableObject):
    """
    InlineResponse4006
    """


class InlineResponse2006(System_IEquatable, IValidatableObject):
    """
    InlineResponse2006
    """


class AccountChangesState(System_IEquatable, IValidatableObject):
    """
    An AccountState Object is used to represent an Account&#39;s current price-dependent state. Price-dependent Account state is dependent on OANDA&#39;s current Prices, and includes things like unrealized PL, NAV and Trailing Stop Loss Order state.
    """


class WeeklyAlignment(enum.Enum):
    """
    The day of the week to use for candlestick granularities with weekly alignment.
    """


class Candlestick(System_IEquatable, IValidatableObject):
    """
    The Candlestick representation
    """


class PositionAggregationMode(enum.Enum):
    """
    The way that position values for an Account are calculated and aggregated.
    """


class InlineResponse2008(System_IEquatable, IValidatableObject):
    """
    InlineResponse2008
    """


class Price(System_IEquatable, IValidatableObject):
    """
    The specification of an Account-specific Price.
    """


    class StatusEnum(enum.Enum):
        """
        The status of the Price.
        """


class RequestID(System_IEquatable, IValidatableObject):
    """
    The request identifier.
    """


class PriceValue(System_IEquatable, IValidatableObject):
    """
    The string representation of a Price for an Instrument.
    """


class PricingHeartbeat(System_IEquatable, IValidatableObject):
    """
    A PricingHeartbeat object is injected into the Pricing stream to ensure that the HTTP connection remains active.
    """


class TrailingStopLossOrderRejectTransaction(System_IEquatable, IValidatableObject):
    """
    A TrailingStopLossOrderRejectTransaction represents the rejection of the creation of a TrailingStopLoss Order.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"TRAILING_STOP_LOSS_ORDER_REJECT\" in a TrailingStopLossOrderRejectTransaction.
        """


    class TimeInForceEnum(enum.Enum):
        """
        The time-in-force requested for the TrailingStopLoss Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for TrailingStopLoss Orders.
        """


    class TriggerConditionEnum(enum.Enum):
        """
        Specification of what component of a price should be used for comparison when determining if the Order should be filled.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Trailing Stop Loss Order was initiated
        """


    class RejectReasonEnum(enum.Enum):
        """
        The reason that the Reject Transaction was created
        """


class OrderTriggerCondition(enum.Enum):
    """
    Specification of what component of a price should be used for comparison when determining if the Order should be filled.
    """


class InlineResponse20022(System_IEquatable, IValidatableObject):
    """
    The response body for the Pricing Stream uses chunked transfer encoding.  Each chunk contains Price and/or PricingHeartbeat objects encoded as JSON.  Each JSON object is serialized into a single line of text, and multiple objects found in the same chunk are separated by newlines. Heartbeats are sent every 5 seconds.
    """


class InlineResponse4045(System_IEquatable, IValidatableObject):
    """
    InlineResponse4045
    """


class InlineResponse401(System_IEquatable, IValidatableObject):
    """
    InlineResponse401
    """


class QuoteHomeConversionFactors(System_IEquatable, IValidatableObject):
    """
    QuoteHomeConversionFactors represents the factors that can be used used to convert quantities of a Price&#39;s Instrument&#39;s quote currency into the Account&#39;s home currency.
    """


class DynamicOrderState(System_IEquatable, IValidatableObject):
    """
    The dynamic state of an Order. This is only relevant to TrailingStopLoss Orders, as no other Order type has dynamic state.
    """


class ClientExtensions(System_IEquatable, IValidatableObject):
    """
    A ClientExtensions object allows a client to attach a clientID, tag and comment to Orders and Trades in their Account.  Do not set, modify, or delete this field if your account is associated with MT4.
    """


class OrderCancelRejectTransaction(System_IEquatable, IValidatableObject):
    """
    An OrderCancelRejectTransaction represents the rejection of the cancellation of an Order in the client&#39;s Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"ORDER_CANCEL_REJECT\" for an OrderCancelRejectTransaction.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that the Order was to be cancelled.
        """


    class RejectReasonEnum(enum.Enum):
        """
        The reason that the Reject Transaction was created
        """


class Account(System_IEquatable, IValidatableObject):
    """
    The full details of a client&#39;s Account. This includes full open Trade, open Position and pending Order representation.
    """


class OrderFillTransaction(System_IEquatable, IValidatableObject):
    """
    An OrderFillTransaction represents the filling of an Order in the client&#39;s Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"ORDER_FILL\" for an OrderFillTransaction.
        """


    class ReasonEnum(enum.Enum):
        """
        The reason that an Order was filled
        """


class UnitsAvailableDetails(System_IEquatable, IValidatableObject):
    """
    Representation of many units of an Instrument are available to be traded for both long and short Orders.
    """


class TrailingStopLossDetails(System_IEquatable, IValidatableObject):
    """
    TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade&#39;s dependent Trailing Stop Loss Order is modified directly through the Trade.
    """


    class TimeInForceEnum(enum.Enum):
        """
        The time in force for the created Trailing Stop Loss Order. This may only be GTC, GTD or GFD.
        """


class CloseTradeBody(System_IEquatable, IValidatableObject):
    """
    CloseTradeBody
    """


class InlineResponse4005(System_IEquatable, IValidatableObject):
    """
    InlineResponse4005
    """


class TransferFundsRejectTransaction(System_IEquatable, IValidatableObject):
    """
    A TransferFundsRejectTransaction represents the rejection of the transfer of funds in/out of an Account.
    """


    class TypeEnum(enum.Enum):
        """
        The Type of the Transaction. Always set to \"TRANSFER_FUNDS_REJECT\" in a TransferFundsRejectTransaction.
        """


    class FundingReasonEnum(enum.Enum):
        """
        The reason that an Account is being funded.
        """


    class RejectReasonEnum(enum.Enum):
        """
        The reason that the Reject Transaction was created
        """


class TransactionType(enum.Enum):
    """
    The possible types of a Transaction
    """


class CalculatedTradeState(System_IEquatable, IValidatableObject):
    """
    The dynamic (calculated) state of an open Trade
    """


class VWAPReceipt(System_IEquatable, IValidatableObject):
    """
    A VWAP Receipt provides a record of how the price for an Order fill is constructed. If the Order is filled with multiple buckets in a depth of market, each bucket will be represented with a VWAP Receipt.
    """


class InlineResponse20018(System_IEquatable, IValidatableObject):
    """
    InlineResponse20018
    """


class InlineResponse20027(System_IEquatable, IValidatableObject):
    """
    InlineResponse20027
    """


class MarketOrderMarginCloseout(System_IEquatable, IValidatableObject):
    """
    Details for the Market Order extensions specific to a Market Order placed that is part of a Market Order Margin Closeout in a client&#39;s account
    """


    class ReasonEnum(enum.Enum):
        """
        The reason the Market Order was created to perform a margin closeout
        """


class InlineResponse404(System_IEquatable, IValidatableObject):
    """
    InlineResponse404
    """


class CandlestickData(System_IEquatable, IValidatableObject):
    """
    The price data (open, high, low, close) for the Candlestick representation.
    """


class InlineResponse4007(System_IEquatable, IValidatableObject):
    """
    InlineResponse4007
    """


class StopLossOrderReason(enum.Enum):
    """
    The reason that the Stop Loss Order was initiated
    """



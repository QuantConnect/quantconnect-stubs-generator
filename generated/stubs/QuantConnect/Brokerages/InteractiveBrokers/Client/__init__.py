import abc
import typing


System_EventArgs = typing.Any
DefaultEWrapper = typing.Any
System_IDisposable = typing.Any


class NextValidIdEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.NextValidId event
    """


class SecurityType:
    """
    Contract Security Types
    """


class OrderType:
    """
    Order Type string constants
    """


class ErrorEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.Error event
    """


class TimeInForce:
    """
    Order Time in Force Values
    """


class UpdatePortfolioEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.UpdatePortfolio event
    """


class HistoricalDataEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.HistoricalData event
    """


class OrderStatus:
    """
    Order Status constants.
    """


class BarSize:
    """
    Historical Bar Size Requests
    """


class TickPriceEventArgs(TickEventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.TickPrice event
    """


class ContractDetailsEventArgs(System_EventArgs):
    """
    Event arguments class for the following events:
    InteractiveBrokersClient.ContractDetailsInteractiveBrokersClient.BondContractDetails
    """


class TickSizeEventArgs(TickEventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.TickSize event
    """


class AgentDescription:
    """
    Used for Rule 80A describes the type of trader.
    """


class ReceiveFaEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.ReceiveFa event
    """


class OpenOrderEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.OpenOrder event
    """


class UpdateAccountValueEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.UpdateAccountValue event
    """


class ActionSide:
    """
    Order Action Side. Specifies whether securities should be bought or sold.
    """


class CommissionReportEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.CommissionReport event
    """


class InteractiveBrokersClient(DefaultEWrapper, System_IDisposable):
    """
    Event based implementation of Interactive Brokers EWrapper interface
    """


class RequestEndEventArgs(System_EventArgs):
    """
    Event arguments class for the following events:
    InteractiveBrokersClient.AccountSummaryEndInteractiveBrokersClient.ContractDetailsEndInteractiveBrokersClient.ExecutionDetailsEnd
    """


class RightType:
    """
    Option Right Type (Put or Call)
    """


class AccountDownloadEndEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.AccountDownloadEnd event
    """


class HistoricalDataEndEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.HistoricalDataEnd event
    """


class ExecutionDetailsEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.ExecutionDetails event
    """


class CurrentTimeUtcEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.CurrentTimeUtc event
    """


class TickEventArgs(System_EventArgs, metaclass=abc.ABCMeta):
    """
    Base event arguments class for Tick events
    """


class OrderStatusEventArgs(System_EventArgs):
    """
    Event arguments class for the InteractiveBrokersClient.OrderStatus event
    """



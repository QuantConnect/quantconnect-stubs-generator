import QuantConnect.Securities
import abc


class BacktestingTransactionHandler(BrokerageTransactionHandler):
    """
    This transaction handler is used for processing transactions during backtests
    """


class BrokerageTransactionHandler(ITransactionHandler):
    """
    Transaction handler for all brokerages
    """


class ITransactionHandler(QuantConnect.Securities.IOrderProcessor, QuantConnect.Securities.IOrderEventProvider, metaclass=abc.ABCMeta):
    """
    Transaction handlers define how the transactions are processed and set the order fill information.
    The pass this information back to the algorithm portfolio and ensure the cash and portfolio are synchronized.
    """


class CancelPendingOrders:
    """
    Class used to keep track of CancelPending orders and their original or updated status
    """



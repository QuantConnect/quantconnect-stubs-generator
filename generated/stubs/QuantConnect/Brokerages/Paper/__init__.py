import QuantConnect.Brokerages
import QuantConnect.Brokerages.Backtesting


class PaperBrokerage(QuantConnect.Brokerages.Backtesting.BacktestingBrokerage):
    """
    Paper Trading Brokerage
    """


class PaperBrokerageFactory(QuantConnect.Brokerages.BrokerageFactory):
    """
    The factory type for the PaperBrokerage
    """



import QuantConnect.Brokerages
import abc


class BasicOptionAssignmentSimulation(IBacktestingMarketSimulation):
    """
    This market conditions simulator emulates exercising of short option positions in the portfolio.
    Simulator implements basic no-arb argument: when time value of the option contract is close to zero
    it assigns short legs getting profit close to expiration dates in deep ITM positions. User algorithm then receives
    assignment event from LEAN. Simulator randomly scans for arbitrage opportunities every two hours or so.
    """


class BacktestingBrokerage(QuantConnect.Brokerages.Brokerage):
    """
    Represents a brokerage to be used during backtesting. This is intended to be only be used with the BacktestingTransactionHandler
    """


class BacktestingBrokerageFactory(QuantConnect.Brokerages.BrokerageFactory):
    """
    Factory type for the BacktestingBrokerage
    """


class IBacktestingMarketSimulation(metaclass=abc.ABCMeta):
    """
    Backtesting Market Simulation interface, that must be implemented by all simulators of market conditions run during backtest
    """



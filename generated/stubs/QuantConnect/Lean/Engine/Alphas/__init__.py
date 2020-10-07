import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Lean.Engine.Alpha
import typing


System_IDisposable = typing.Any


class StatisticsInsightManagerExtension(QuantConnect.Algorithm.Framework.Alphas.IInsightManagerExtension):
    """
    Manages alpha statistics responsbilities
    """


class ChartingInsightManagerExtension(QuantConnect.Algorithm.Framework.Alphas.IInsightManagerExtension):
    """
    Manages alpha charting responsibilities.
    """


class DefaultAlphaHandler(QuantConnect.Lean.Engine.Alpha.IAlphaHandler):
    """
    Default alpha handler that supports sending insights to the messaging handler, analyzing insights online
    """


    class AlphaResultPacketSender(QuantConnect.Algorithm.Framework.Alphas.IInsightManagerExtension, System_IDisposable):
        """
        This class is protected.
        
        Encapsulates routing finalized insights to the messaging handler
        """



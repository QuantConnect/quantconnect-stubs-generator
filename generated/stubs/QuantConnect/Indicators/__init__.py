import QuantConnect.Data
import QuantConnect.Data.Market
import abc
import enum
import typing


System_IEquatable = typing.Any
System_IComparable = typing.Any


QuantConnect_Indicators_IndicatorBase_T = typing.TypeVar('QuantConnect_Indicators_IndicatorBase_T')
QuantConnect_Indicators_ConstantIndicator_T = typing.TypeVar('QuantConnect_Indicators_ConstantIndicator_T')
QuantConnect_Indicators_FunctionalIndicator_T = typing.TypeVar('QuantConnect_Indicators_FunctionalIndicator_T')
QuantConnect_Indicators_CompositeIndicator_T = typing.TypeVar('QuantConnect_Indicators_CompositeIndicator_T')
QuantConnect_Indicators_WindowIndicator_T = typing.TypeVar('QuantConnect_Indicators_WindowIndicator_T')
QuantConnect_Indicators_IIndicator_T = typing.TypeVar('QuantConnect_Indicators_IIndicator_T')
QuantConnect_Indicators_IReadOnlyWindow_T = typing.TypeVar('QuantConnect_Indicators_IReadOnlyWindow_T')
QuantConnect_Indicators_RollingWindow_T = typing.TypeVar('QuantConnect_Indicators_RollingWindow_T')


class ArnaudLegouxMovingAverage(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    Smooth and high sensitive moving Average. This moving average reduce lag of the information
    but still being smooth to reduce noises.
    Is a weighted moving average, which weights have a Normal shape;
    the parameters Sigma and Offset affect the kurtosis and skewness of the weights respectively.
    Source: http://www.arnaudlegoux.com/index.html
    """


class ExponentialMovingAverage(Indicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional exponential moving average indicator (EMA)
    """


class IntradayVwap(IndicatorBase[QuantConnect.Data.BaseData]):
    """
    Defines the canonical intraday VWAP indicator
    """


class AccumulationDistribution(TradeBarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Accumulation/Distribution (AD)
    The Accumulation/Distribution is calculated using the following formula:
    AD = AD + ((Close - Low) - (High - Close)) / (High - Low) * Volume
    """


class AbsolutePriceOscillator(MovingAverageConvergenceDivergence):
    """
    This indicator computes the Absolute Price Oscillator (APO)
    The Absolute Price Oscillator is calculated using the following formula:
    APO[i] = FastMA[i] - SlowMA[i]
    """


class MovingAverageType(enum.Enum):
    """
    Defines the different types of moving averages
    """


class WilderMovingAverage(Indicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents the moving average indicator defined by Welles Wilder in his book:
    New Concepts in Technical Trading Systems.
    """


class UltimateOscillator(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Ultimate Oscillator (ULTOSC)
    The Ultimate Oscillator is calculated as explained here:
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:ultimate_oscillator
    """


class CoppockCurve(IndicatorBase[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    A momentum indicator developed by Edwin “Sedge” Coppock in October 1965.
    The goal of this indicator is to identify long-term buying opportunities in the S&amp;P500 and Dow Industrials.
    Source: http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:coppock_curve
    """


class LogReturn(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    Represents the LogReturn indicator (LOGR)
    - log returns are useful for identifying price convergence/divergence in a given period
    - logr = log (current price / last price in period)
    """


class AdvanceDeclineRatio(AdvanceDeclineIndicator):
    """
    The advance-decline ratio (ADR) compares the number of stocks
    that closed higher against the number of stocks
    that closed lower than their previous day's closing prices.
    """


class IndicatorBase(typing.Generic[QuantConnect_Indicators_IndicatorBase_T], IIndicator[QuantConnect_Indicators_IndicatorBase_T], metaclass=abc.ABCMeta):
    """
    This class has no documentation.
    """


class HeikinAshi(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Heikin-Ashi bar (HA)
    The Heikin-Ashi bar is calculated using the following formulas:
    HA_Close[0] = (Open[0] + High[0] + Low[0] + Close[0]) / 4
    HA_Open[0] = (HA_Open[1] + HA_Close[1]) / 2
    HA_High[0] = MAX(High[0], HA_Open[0], HA_Close[0])
    HA_Low[0] = MIN(Low[0], HA_Open[0], HA_Close[0])
    """


class NormalizedAverageTrueRange(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Normalized Average True Range (NATR).
    The Normalized Average True Range is calculated with the following formula:
    NATR = (ATR(period) / Close) * 100
    """


class WindowIdentity(WindowIndicator[IndicatorDataPoint]):
    """
    Represents an indicator that is a ready after ingesting enough samples (# samples > period)
    and always returns the same value as it is given.
    """


class ConstantIndicator(typing.Generic[QuantConnect_Indicators_ConstantIndicator_T], IndicatorBase[QuantConnect_Indicators_ConstantIndicator_T]):
    """
    An indicator that will always return the same value.
    """


class Maximum(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    Represents an indicator capable of tracking the maximum value and how many periods ago it occurred
    """


class FunctionalIndicator(typing.Generic[QuantConnect_Indicators_FunctionalIndicator_T], IndicatorBase[QuantConnect_Indicators_FunctionalIndicator_T]):
    """
    The functional indicator is used to lift any function into an indicator. This can be very useful
    when trying to combine output of several indicators, or for expression a mathematical equation
    """


class FisherTransform(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Fisher transform is a mathematical process which is used to convert any data set to a modified
    data set whose Probability Distribution Function is approximately Gaussian. Once the Fisher transform
    is computed, the transformed data can then be analyzed in terms of it's deviation from the mean.
    
    The equation is y = .5 * ln [ 1 + x / 1 - x ] where
    x is the input
    y is the output
    ln is the natural logarithm
    
    The Fisher transform has much sharper turning points than other indicators such as MACD
    
    For more info, read chapter 1 of Cybernetic Analysis for Stocks and Futures by John F. Ehlers
    
    We are implementing the latest version of this indicator found at Fig. 4 of
    http://www.mesasoftware.com/papers/UsingTheFisherTransform.pdf
    """


class StandardDeviation(Variance):
    """
    This indicator computes the n-period population standard deviation.
    """


class RateOfChangeRatio(RateOfChange):
    """
    This indicator computes the Rate Of Change Ratio (ROCR).
    The Rate Of Change Ratio is calculated with the following formula:
    ROCR = price / prevPrice
    """


class LeastSquaresMovingAverage(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    The Least Squares Moving Average (LSMA) first calculates a least squares regression line
    over the preceding time periods, and then projects it forward to the current period. In
    essence, it calculates what the value would be if the regression line continued.
    Source: https://rtmath.net/helpFinAnalysis/html/b3fab79c-f4b2-40fb-8709-fdba43cdb363.htm
    """


class SchaffTrendCycle(Indicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator creates the Schaff Trend Cycle
    """


class KaufmanAdaptiveMovingAverage(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Kaufman Adaptive Moving Average (KAMA).
    The Kaufman Adaptive Moving Average is calculated as explained here:
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:kaufman_s_adaptive_moving_average
    """


class Variance(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period population variance.
    """


class CompositeIndicator(typing.Generic[QuantConnect_Indicators_CompositeIndicator_T], IndicatorBase[IndicatorDataPoint]):
    """
    This indicator is capable of wiring up two separate indicators into a single indicator
    such that the output of each will be sent to a user specified function.
    """


class MassIndex(TradeBarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Mass Index uses the high-low range to identify trend reversals based on range expansions.
    In this sense, the Mass Index is a volatility indicator that does not have a directional
    bias. Instead, the Mass Index identifies range bulges that can foreshadow a reversal of the
    current trend. Developed by Donald Dorsey.
    """


class Momentum(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period change in a value using the following:
    value_0 - value_n
    """


class Trix(Indicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the TRIX (1-period ROC of a Triple EMA)
    The TRIX is calculated as explained here:
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:trix
    """


class BollingerBands(Indicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator creates a moving average (middle band) with an upper band and lower band
    fixed at k standard deviations above and below the moving average.
    """


class Identity(Indicator):
    """
    Represents an indicator that is a ready after ingesting a single sample and
        always returns the same value as it is given.
    """


class RateOfChangePercent(RateOfChange):
    """
    This indicator computes the n-period percentage rate of change in a value using the following:
    100 * (value_0 - value_n) / value_n
    """


class AverageTrueRange(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The AverageTrueRange indicator is a measure of volatility introduced by Welles Wilder in his
    book: New Concepts in Technical Trading Systems. This indicator computes the TrueRange and then
    smoothes the TrueRange over a given period.
    
    TrueRange is defined as the maximum of the following:
      High - Low
      ABS(High - PreviousClose)
      ABS(Low - PreviousClose)
    """


class BalanceOfPower(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Balance Of Power (BOP).
    The Balance Of Power is calculated with the following formula:
    BOP = (Close - Open) / (High - Low)
    """


class VolumeWeightedAveragePriceIndicator(TradeBarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Volume Weighted Average Price (VWAP) Indicator:
    It is calculated by adding up the dollars traded for every transaction (price multiplied
    by number of shares traded) and then dividing by the total shares traded for the day.
    """


class AroonOscillator(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Aroon Oscillator is the difference between AroonUp and AroonDown. The value of this
    indicator fluctuates between -100 and +100. An upward trend bias is present when the oscillator
    is positive, and a negative trend bias is present when the oscillator is negative. AroonUp/Down
    values over 75 identify strong trends in their respective direction.
    """


class HullMovingAverage(IndicatorBase[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    Produces a Hull Moving Average as explained at http://www.alanhull.com/hull-moving-average/
    and derived from the instructions for the Excel VBA code at http://finance4traders.blogspot.com/2009/06/how-to-calculate-hull-moving-average.html
    """


class IndicatorExtensions:
    """
    Provides extension methods for Indicator
    """


class MovingAverageConvergenceDivergence(Indicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator creates two moving averages defined on a base indicator and produces the difference
    between the fast and slow averages.
    """


class SwissArmyKnifeTool(enum.Enum):
    """
    The tools of the Swiss Army Knife. Some of the tools lend well to chaining with the "Of" Method, others may be treated as moving averages
    """


class SwissArmyKnife(Indicator, IIndicatorWarmUpPeriodProvider):
    """
    Swiss Army Knife indicator by John Ehlers
    """


class MeanAbsoluteDeviation(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period mean absolute deviation.
    """


class Indicator(IndicatorBase[IndicatorDataPoint], metaclass=abc.ABCMeta):
    """
    Represents a type capable of ingesting a piece of data and producing a new piece of data.
    Indicators can be used to filter and transform data into a new, more informative form.
    """


class TrueRange(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the True Range (TR).
    The True Range is the greatest of the following values:
    value1 = distance from today's high to today's low.
    value2 = distance from yesterday's close to today's high.
    value3 = distance from yesterday's close to today's low.
    """


class MidPrice(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the MidPrice (MIDPRICE).
    The MidPrice is calculated using the following formula:
    MIDPRICE = (Highest High + Lowest Low) / 2
    """


class TradeBarIndicator(IndicatorBase[QuantConnect.Data.Market.TradeBar], metaclass=abc.ABCMeta):
    """
    The TradeBarIndicator is an indicator that accepts TradeBar data as its input.
    
    This type is more of a shim/typedef to reduce the need to refer to things as IndicatorBase&lt;TradeBar&gt;
    """


class IndicatorResult:
    """
    Represents the result of an indicator's calculations
    """


class AverageDirectionalIndex(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes Average Directional Index which measures trend strength without regard to trend direction.
    Firstly, it calculates the Directional Movement and the True Range value, and then the values are accumulated and smoothed
    using a custom smoothing method proposed by Wilder. For an n period smoothing, 1/n of each period's value is added to the total period.
    From these accumulated values we are therefore able to derived the 'Positive Directional Index' (+DI) and 'Negative Directional Index' (-DI)
    which is used to calculate the Average Directional Index.
    Computation source:
    https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_directional_index_adx
    """


class DetrendedPriceOscillator(IndicatorBase[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    The Detrended Price Oscillator is an indicator designed to remove trend from price
    and make it easier to identify cycles.
    DPO does not extend to the last date because it is based on a displaced moving average.
    Is estimated as Price {X/2 + 1} periods ago less the X-period simple moving average.
    E.g.DPO(20) equals price 11 days ago less the 20-day SMA.
    """


class T3MovingAverage(IndicatorBase[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the T3 Moving Average (T3).
    The T3 Moving Average is calculated with the following formula:
    EMA1(x, Period) = EMA(x, Period)
    EMA2(x, Period) = EMA(EMA1(x, Period),Period)
    GD(x, Period, volumeFactor) = (EMA1(x, Period)*(1+volumeFactor)) - (EMA2(x, Period)* volumeFactor)
    T3 = GD(GD(GD(t, Period, volumeFactor), Period, volumeFactor), Period, volumeFactor);
    """


class TriangularMovingAverage(Indicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Triangular Moving Average (TRIMA).
    The Triangular Moving Average is calculated with the following formula:
    (1) When the period is even, TRIMA(x,period)=SMA(SMA(x,period/2),(period/2)+1)
    (2) When the period is odd,  TRIMA(x,period)=SMA(SMA(x,(period+1)/2),(period+1)/2)
    """


class AverageDirectionalMovementIndexRating(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Average Directional Movement Index Rating (ADXR).
    The Average Directional Movement Index Rating is calculated with the following formula:
    ADXR[i] = (ADX[i] + ADX[i - period + 1]) / 2
    """


class LinearWeightedMovingAverage(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional Weighted Moving Average indicator. The weight are linearly
    distributed according to the number of periods in the indicator.
    
    For example, a 4 period indicator will have a numerator of (4 * window[0]) + (3 * window[1]) + (2 * window[2]) + window[3]
    and a denominator of 4 + 3 + 2 + 1 = 10
    
    During the warm up period, IsReady will return false, but the LWMA will still be computed correctly because
    the denominator will be the minimum of Samples factorial or Size factorial and
    the computation iterates over that minimum value.
    
    The RollingWindow of inputs is created when the indicator is created.
    A RollingWindow of LWMAs is not saved.  That is up to the caller.
    """


class WilliamsPercentR(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Williams %R, or just %R, is the current closing price in relation to the high and low of
    the past N days (for a given N). The value of this indicator fluctuates between -100 and 0.
    The symbol is said to be oversold when the oscillator is below -80%,
    and overbought when the oscillator is above -20%.
    """


class ArmsIndex(TradeBarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Arms Index, also called the Short-Term Trading Index (TRIN)
    is a technical analysis indicator that compares the number of advancing
    and declining stocks (AD Ratio) to advancing and declining volume (AD volume).
    """


class DoubleExponentialMovingAverage(IndicatorBase[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Double Exponential Moving Average (DEMA).
    The Double Exponential Moving Average is calculated with the following formula:
    EMA2 = EMA(EMA(t,period),period)
    DEMA = 2 * EMA(t,period) - EMA2
    The Generalized DEMA (GD) is calculated with the following formula:
    GD = (volumeFactor+1) * EMA(t,period) - volumeFactor * EMA2
    """


class DonchianChannel(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the upper and lower band of the Donchian Channel.
    The upper band is computed by finding the highest high over the given period.
    The lower band is computed by finding the lowest low over the given period.
    The primary output value of the indicator is the mean of the upper and lower band for
    the given timeframe.
    """


class KeltnerChannels(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator creates a moving average (middle band) with an upper band and lower band
    fixed at k average true range multiples away from the middle band.
    """


class AdvanceDeclineVolumeRatio(AdvanceDeclineIndicator):
    """
    The Advance Decline Volume Ratio is a Breadth indicator calculated as ratio of
    summary volume of advancing stocks to summary volume of declining stocks.
    AD Volume Ratio is used in technical analysis to see where the main trading activity is focused.
    """


class MovingAverageTypeExtensions:
    """
    Provides extension methods for the MovingAverageType enumeration
    """


class IchimokuKinkoHyo(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Ichimoku Kinko Hyo indicator. It consists of the following main indicators:
    Tenkan-sen: (Highest High + Lowest Low) / 2 for the specific period (normally 9)
    Kijun-sen: (Highest High + Lowest Low) / 2 for the specific period (normally 26)
    Senkou A Span: (Tenkan-sen + Kijun-sen )/ 2 from a specific number of periods ago (normally 26)
    Senkou B Span: (Highest High + Lowest Low) / 2 for the specific period (normally 52), from a specific number of periods ago (normally 26)
    """


class PythonIndicator(IndicatorBase[QuantConnect.Data.IBaseData]):
    """
    Provides a wrapper for IndicatorBase{IBaseData} implementations written in python
    """


class Stochastic(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Slow Stochastics %K and %D. The Fast Stochastics %K is is computed by
    (Current Close Price - Lowest Price of given Period) / (Highest Price of given Period - Lowest Price of given Period)
    multiplied by 100. Once the Fast Stochastics %K is calculated the Slow Stochastic %K is calculated by the average/smoothed price of
    of the Fast %K with the given period. The Slow Stochastics %D is then derived from the Slow Stochastics %K with the given period.
    """


class MoneyFlowIndex(TradeBarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Money Flow Index (MFI) is an oscillator that uses both price and volume to
    measure buying and selling pressure
    
    Typical Price = (High + Low + Close)/3
    Money Flow = Typical Price x Volume
    Positive Money Flow = Sum of the money flows of all days where the typical
        price is greater than the previous day's typical price
    Negative Money Flow = Sum of the money flows of all days where the typical
        price is less than the previous day's typical price
    Money Flow Ratio = (14-period Positive Money Flow)/(14-period Negative Money Flow)
    
    Money Flow Index = 100 x  Positive Money Flow / ( Positive Money Flow + Negative Money Flow)
    """


class CommodityChannelIndex(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional commodity channel index (CCI)
    
    CCI = (Typical Price - 20-period SMA of TP) / (.015 * Mean Deviation)
    Typical Price (TP) = (High + Low + Close)/3
    Constant = 0.015
    
    There are four steps to calculating the Mean Deviation, first, subtract
    the most recent 20-period average of the typical price from each period's
    typical price. Second, take the absolute values of these numbers. Third,
    sum the absolute values. Fourth, divide by the total number of periods (20).
    """


class MomentumPercent(RateOfChangePercent):
    """
    This indicator computes the n-period percentage rate of change in a value using the following:
    100 * (value_0 - value_n) / value_n
    
    This indicator yields the same results of RateOfChangePercent
    """


class MomersionIndicator(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    Oscillator indicator that measures momentum and mean-reversion over a specified
    period n.
    Source: Harris, Michael. "Momersion Indicator." Price Action Lab.,
                13 Aug. 2015. Web. http://www.priceactionlab.com/Blog/2015/08/momersion-indicator/.
    """


class WindowIndicator(typing.Generic[QuantConnect_Indicators_WindowIndicator_T], IndicatorBase[QuantConnect_Indicators_WindowIndicator_T], metaclass=abc.ABCMeta):
    """
    Represents an indicator that acts on a rolling window of data
    """


class RelativeStrengthIndex(Indicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents the  Relative Strength Index (RSI) developed by K. Welles Wilder.
    You can optionally specified a different moving average type to be used in the computation
    """


class FilteredIdentity(IndicatorBase[QuantConnect.Data.IBaseData]):
    """
    Represents an indicator that is a ready after ingesting a single sample and
    always returns the same value as it is given if it passes a filter condition
    """


class BarIndicator(IndicatorBase[QuantConnect.Data.Market.IBaseDataBar], metaclass=abc.ABCMeta):
    """
    The BarIndicator is an indicator that accepts IBaseDataBar data as its input.
    
    This type is more of a shim/typedef to reduce the need to refer to things as IndicatorBase&lt;IBaseDataBar&gt;
    """


class SimpleMovingAverage(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional simple moving average indicator (SMA)
    """


class RegressionChannel(Indicator, IIndicatorWarmUpPeriodProvider):
    """
    The Regression Channel indicator extends the LeastSquaresMovingAverage
    with the inclusion of two (upper and lower) channel lines that are distanced from
    the linear regression line by a user defined number of standard deviations.
    Reference: http://www.onlinetradingconcepts.com/TechnicalAnalysis/LinRegChannel.html
    """


class AccelerationBands(IndicatorBase[QuantConnect.Data.Market.IBaseDataBar], IIndicatorWarmUpPeriodProvider):
    """
    The Acceleration Bands created by Price Headley plots upper and lower envelope bands around a moving average.
    """


class ParabolicStopAndReverse(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Parabolic SAR Indicator
    Based on TA-Lib implementation
    """


class PercentagePriceOscillator(AbsolutePriceOscillator):
    """
    This indicator computes the Percentage Price Oscillator (PPO)
    The Percentage Price Oscillator is calculated using the following formula:
    PPO[i] = 100 * (FastMA[i] - SlowMA[i]) / SlowMA[i]
    """


class Delay(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    An indicator that delays its input for a certain period
    """


class IndicatorStatus(enum.Enum):
    """
    The possible states returned by IndicatorBase{T}.ComputeNextValue
    """


class ChandeMomentumOscillator(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Chande Momentum Oscillator (CMO).
    CMO calculation is mostly identical to RSI.
    The only difference is in the last step of calculation:
    RSI = gain / (gain+loss)
    CMO = (gain-loss) / (gain+loss)
    """


class FractalAdaptiveMovingAverage(BarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Fractal Adaptive Moving Average (FRAMA) by John Ehlers
    """


class TripleExponentialMovingAverage(IndicatorBase[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Triple Exponential Moving Average (TEMA).
    The Triple Exponential Moving Average is calculated with the following formula:
    EMA1 = EMA(t,period)
    EMA2 = EMA(EMA(t,period),period)
    EMA3 = EMA(EMA(EMA(t,period),period),period)
    TEMA = 3 * EMA1 - 3 * EMA2 + EMA3
    """


class MidPoint(IndicatorBase[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the MidPoint (MIDPOINT)
    The MidPoint is calculated using the following formula:
    MIDPOINT = (Highest Value + Lowest Value) / 2
    """


class RateOfChange(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period rate of change in a value using the following:
    (value_0 - value_n) / value_n
    """


class EaseOfMovementValue(TradeBarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period Ease of Movement Value using the following:
    MID = (high_1 + low_1)/2 - (high_0 + low_0)/2
    RATIO = (currentVolume/10000) / (high_1 - low_1)
    EMV = MID/RATIO
    _SMA = n-period of EMV
    Returns _SMA
    Source: https://www.investopedia.com/terms/e/easeofmovement.asp
    """


class Minimum(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    Represents an indicator capable of tracking the minimum value and how many periods ago it occurred
    """


class AdvanceDeclineIndicator(TradeBarIndicator, IIndicatorWarmUpPeriodProvider, metaclass=abc.ABCMeta):
    """
    The advance-decline indicator compares the number of stocks
    that closed higher against the number of stocks
    that closed lower than their previous day's closing prices.
    """


class OnBalanceVolume(TradeBarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the On Balance Volume (OBV).
    The On Balance Volume is calculated by determining the price of the current close price and previous close price.
    If the current close price is equivalent to the previous price the OBV remains the same,
    If the current close price is higher the volume of that day is added to the OBV, while a lower close price will
    result in negative value.
    """


class Sum(WindowIndicator[IndicatorDataPoint], IIndicatorWarmUpPeriodProvider):
    """
    Represents an indicator capable of tracking the sum for the given period
    """


class AccumulationDistributionOscillator(TradeBarIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Accumulation/Distribution Oscillator (ADOSC)
    The Accumulation/Distribution Oscillator is calculated using the following formula:
    ADOSC = EMA(fast,AD) - EMA(slow,AD)
    """


class IndicatorDataPoint(QuantConnect.Data.BaseData, System_IEquatable, System_IComparable, System_IComparable):
    """
    Represents a piece of data at a specific time
    """


class IIndicatorWarmUpPeriodProvider(metaclass=abc.ABCMeta):
    """
    Represents an indicator with a warm up period provider.
    """


class IIndicator(typing.Generic[QuantConnect_Indicators_IIndicator_T], System_IComparable, System_IComparable, IIndicator, metaclass=abc.ABCMeta):
    """
    KEEPING THIS INTERFACE FOR BACKWARDS COMPATIBILITY.
    Represents an indicator that can receive data updates and emit events when the value of
    the indicator has changed.
    """


class IReadOnlyWindow(typing.Generic[QuantConnect_Indicators_IReadOnlyWindow_T], typing.List[QuantConnect_Indicators_IReadOnlyWindow_T], metaclass=abc.ABCMeta):
    """
    Interface type used to pass windows around without worry of external modification
    """


class RollingWindow(typing.Generic[QuantConnect_Indicators_RollingWindow_T], IReadOnlyWindow[QuantConnect_Indicators_RollingWindow_T]):
    """
    This is a window that allows for list access semantics,
        where this[0] refers to the most recent item in the
        window and this[Count-1] refers to the last item in the window
    """



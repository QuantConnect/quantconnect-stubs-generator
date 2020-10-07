import QuantConnect.Data.Market
import QuantConnect.Indicators
import abc
import enum


class SeparatingLines(CandlestickPattern):
    """
    Separating Lines candlestick pattern indicator
    """


class Breakaway(CandlestickPattern):
    """
    Breakaway candlestick pattern indicator
    """


class DarkCloudCover(CandlestickPattern):
    """
    Dark Cloud Cover candlestick pattern
    """


class Engulfing(CandlestickPattern):
    """
    Engulfing candlestick pattern
    """


class ShootingStar(CandlestickPattern):
    """
    Shooting Star candlestick pattern
    """


class ThreeInside(CandlestickPattern):
    """
    Three Inside Up/Down candlestick pattern
    """


class UpDownGapThreeMethods(CandlestickPattern):
    """
    Up/Down Gap Three Methods candlestick pattern
    """


class HikkakeModified(CandlestickPattern):
    """
    Hikkake Modified candlestick pattern
    """


class ShortLineCandle(CandlestickPattern):
    """
    Short Line Candle candlestick pattern indicator
    """


class KickingByLength(CandlestickPattern):
    """
    Kicking (bull/bear determined by the longer marubozu) candlestick pattern
    """


class ClosingMarubozu(CandlestickPattern):
    """
    Closing Marubozu candlestick pattern indicator
    """


class IdenticalThreeCrows(CandlestickPattern):
    """
    Identical Three Crows candlestick pattern
    """


class CandlestickPattern(QuantConnect.Indicators.WindowIndicator[QuantConnect.Data.Market.IBaseDataBar], metaclass=abc.ABCMeta):
    """
    Abstract base class for a candlestick pattern indicator
    """


class HangingMan(CandlestickPattern):
    """
    Hanging Man candlestick pattern indicator
    """


class HomingPigeon(CandlestickPattern):
    """
    Homing Pigeon candlestick pattern indicator
    """


class Takuri(CandlestickPattern):
    """
    Takuri (Dragonfly Doji with very long lower shadow) candlestick pattern indicator
    """


class ThreeWhiteSoldiers(CandlestickPattern):
    """
    Three Advancing White Soldiers candlestick pattern
    """


class Counterattack(CandlestickPattern):
    """
    Counterattack candlestick pattern
    """


class UniqueThreeRiver(CandlestickPattern):
    """
    Unique Three River candlestick pattern
    """


class MatHold(CandlestickPattern):
    """
    Mat Hold candlestick pattern
    """


class StickSandwich(CandlestickPattern):
    """
    Stick Sandwich candlestick pattern indicator
    """


class Hikkake(CandlestickPattern):
    """
    Hikkake candlestick pattern
    """


class LadderBottom(CandlestickPattern):
    """
    Ladder Bottom candlestick pattern indicator
    """


class Doji(CandlestickPattern):
    """
    Doji candlestick pattern indicator
    """


class GapSideBySideWhite(CandlestickPattern):
    """
    Up/Down-gap side-by-side white lines candlestick pattern
    """


class DragonflyDoji(CandlestickPattern):
    """
    Dragonfly Doji candlestick pattern indicator
    """


class Thrusting(CandlestickPattern):
    """
    Thrusting candlestick pattern indicator
    """


class Marubozu(CandlestickPattern):
    """
    Marubozu candlestick pattern indicator
    """


class EveningStar(CandlestickPattern):
    """
    Evening Star candlestick pattern
    """


class EveningDojiStar(CandlestickPattern):
    """
    Evening Doji Star candlestick pattern
    """


class InvertedHammer(CandlestickPattern):
    """
    Inverted Hammer candlestick pattern indicator
    """


class ThreeBlackCrows(CandlestickPattern):
    """
    Three Black Crows candlestick pattern
    """


class RiseFallThreeMethods(CandlestickPattern):
    """
    Rising/Falling Three Methods candlestick pattern
    """


class UpsideGapTwoCrows(CandlestickPattern):
    """
    Upside Gap Two Crows candlestick pattern
    """


class ConcealedBabySwallow(CandlestickPattern):
    """
    Concealed Baby Swallow candlestick pattern
    """


class InNeck(CandlestickPattern):
    """
    In-Neck candlestick pattern indicator
    """


class DojiStar(CandlestickPattern):
    """
    Doji Star candlestick pattern indicator
    """


class MatchingLow(CandlestickPattern):
    """
    Matching Low candlestick pattern indicator
    """


class ThreeLineStrike(CandlestickPattern):
    """
    Three Line Strike candlestick pattern
    """


class HaramiCross(CandlestickPattern):
    """
    Harami Cross candlestick pattern indicator
    """


class AbandonedBaby(CandlestickPattern):
    """
    Abandoned Baby candlestick pattern
    """


class AdvanceBlock(CandlestickPattern):
    """
    Advance Block candlestick pattern
    """


class OnNeck(CandlestickPattern):
    """
    On-Neck candlestick pattern indicator
    """


class MorningDojiStar(CandlestickPattern):
    """
    Morning Doji Star candlestick pattern
    """


class GravestoneDoji(CandlestickPattern):
    """
    Gravestone Doji candlestick pattern indicator
    """


class StalledPattern(CandlestickPattern):
    """
    Stalled Pattern candlestick pattern
    """


class Piercing(CandlestickPattern):
    """
    Piercing candlestick pattern
    """


class TasukiGap(CandlestickPattern):
    """
    Tasuki Gap candlestick pattern indicator
    """


class CandleSettingType(enum.Enum):
    """
    Types of candlestick settings
    """


class CandleRangeType(enum.Enum):
    """
    Types of candlestick ranges
    """


class CandleColor(enum.Enum):
    """
    Colors of a candle
    """


class LongLeggedDoji(CandlestickPattern):
    """
    Long Legged Doji candlestick pattern indicator
    """


class BeltHold(CandlestickPattern):
    """
    Belt-hold candlestick pattern indicator
    """


class Kicking(CandlestickPattern):
    """
    Kicking candlestick pattern
    """


class Hammer(CandlestickPattern):
    """
    Hammer candlestick pattern indicator
    """


class ThreeOutside(CandlestickPattern):
    """
    Three Outside Up/Down candlestick pattern
    """


class ThreeStarsInSouth(CandlestickPattern):
    """
    Three Stars In The South candlestick pattern
    """


class HighWaveCandle(CandlestickPattern):
    """
    High-Wave Candle candlestick pattern indicator
    """


class TwoCrows(CandlestickPattern):
    """
    Two Crows candlestick pattern indicator
    """


class LongLineCandle(CandlestickPattern):
    """
    Long Line Candle candlestick pattern indicator
    """


class CandleSettings:
    """
    Candle settings for all candlestick patterns
    """


class CandleSetting:
    """
    Represents a candle setting
    """


class Harami(CandlestickPattern):
    """
    Harami candlestick pattern indicator
    """


class MorningStar(CandlestickPattern):
    """
    Morning Star candlestick pattern
    """


class SpinningTop(CandlestickPattern):
    """
    Spinning Top candlestick pattern indicator
    """


class Tristar(CandlestickPattern):
    """
    Tristar candlestick pattern indicator
    """


class RickshawMan(CandlestickPattern):
    """
    Rickshaw Man candlestick pattern
    """



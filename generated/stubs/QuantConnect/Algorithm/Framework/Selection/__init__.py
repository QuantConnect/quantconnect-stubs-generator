import QuantConnect
import QuantConnect.Data.UniverseSelection
import abc
import typing


class TechnologyETFUniverse(InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following Technology ETFs at their inception date
    1998-12-22   XLK    Technology Select Sector SPDR Fund
    1999-03-10   QQQ    Invesco QQQ
    2001-07-13   SOXX   iShares PHLX Semiconductor ETF
    2001-07-13   IGV    iShares Expanded Tech-Software Sector ETF
    2004-01-30   VGT    Vanguard Information Technology ETF
    2006-04-25   QTEC   First Trust NASDAQ 100 Technology
    2006-06-23   FDN    First Trust Dow Jones Internet Index
    2007-05-10   FXL    First Trust Technology AlphaDEX Fund
    2008-12-17   TECL   Direxion Daily Technology Bull 3X Shares
    2008-12-17   TECS   Direxion Daily Technology Bear 3X Shares
    2010-03-11   SOXL   Direxion Daily Semiconductor Bull 3x Shares
    2010-03-11   SOXS   Direxion Daily Semiconductor Bear 3x Shares
    2011-07-06   SKYY   First Trust ISE Cloud Computing Index Fund
    2011-12-21   SMH    VanEck Vectors Semiconductor ETF
    2013-08-01   KWEB   KraneShares CSI China Internet ETF
    2013-10-24   FTEC   Fidelity MSCI Information Technology Index ETF
    """


class MetalsETFUniverse(InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following Metals ETFs at their inception date
    2004-11-18   GLD    SPDR Gold Trust
    2005-01-28   IAU    iShares Gold Trust
    2006-04-28   SLV    iShares Silver Trust
    2006-05-22   GDX    VanEck Vectors Gold Miners ETF
    2008-12-04   AGQ    ProShares Ultra Silver
    2009-11-11   GDXJ   VanEck Vectors Junior Gold Miners ETF
    2010-01-08   PPLT   Aberdeen Standard Platinum Shares ETF
    2010-12-08   NUGT   Direxion Daily Gold Miners Bull 3X Shares
    2010-12-08   DUST   Direxion Daily Gold Miners Bear 3X Shares
    2011-10-17   USLV   VelocityShares 3x Long Silver ETN
    2011-10-17   UGLD   VelocityShares 3x Long Gold ETN
    2013-10-03   JNUG   Direxion Daily Junior Gold Miners Index Bull 3x Shares
    2013-10-03   JDST   Direxion Daily Junior Gold Miners Index Bear 3X Shares
    """


class LiquidETFUniverse(InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following ETFs at their inception date
    """


    class Grouping(typing.List[QuantConnect.Symbol]):
        """
        Represent a collection of ETF symbols that is grouped according to a given criteria
        """


class USTreasuriesETFUniverse(InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following US Treasuries ETFs at their inception date
    2002-07-26   IEF    iShares 7-10 Year Treasury Bond ETF
    2002-07-26   SHY    iShares 1-3 Year Treasury Bond ETF
    2002-07-26   TLT    iShares 20+ Year Treasury Bond ETF
    2007-01-11   SHV    iShares Short Treasury Bond ETF
    2007-01-11   IEI    iShares 3-7 Year Treasury Bond ETF
    2007-01-11   TLH    iShares 10-20 Year Treasury Bond ETF
    2007-12-10   EDV    Vanguard Ext Duration Treasury ETF
    2007-05-30   BIL    SPDR Barclays 1-3 Month T-Bill ETF
    2007-05-30   SPTL   SPDR Portfolio Long Term Treasury ETF
    2008-05-01   TBT    UltraShort Barclays 20+ Year Treasury
    2009-04-16   TMF    Direxion Daily 20-Year Treasury Bull 3X
    2009-04-16   TMV    Direxion Daily 20-Year Treasury Bear 3X
    2009-08-20   TBF    ProShares Short 20+ Year Treasury
    2009-11-23   VGSH   Vanguard Short-Term Treasury ETF
    2009-11-23   VGIT   Vanguard Intermediate-Term Treasury ETF
    2009-11-24   VGLT   Vanguard Long-Term Treasury ETF
    2010-08-06   SCHO   Schwab Short-Term U.S. Treasury ETF
    2010-08-06   SCHR   Schwab Intermediate-Term U.S. Treasury ETF
    2011-12-01   SPTS   SPDR Portfolio Short Term Treasury ETF
    2012-02-24   GOVT   iShares U.S. Treasury Bond ETF
    """


class OpenInterestFutureUniverseSelectionModel(FutureUniverseSelectionModel):
    """
    Selects contracts in a futures universe, sorted by open interest.  This allows the selection to identifiy current
        active contract.
    """


class CoarseFundamentalUniverseSelectionModel(FundamentalUniverseSelectionModel):
    """
    Portfolio selection model that uses coarse selectors. For US equities only.
    """


class QC500UniverseSelectionModel(FundamentalUniverseSelectionModel):
    """
    Defines the QC500 universe as a universe selection model for framework algorithm
    For details: https://github.com/QuantConnect/Lean/pull/1663
    """


class EnergyETFUniverse(InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following Energy ETFs at their inception date
    1998-12-22   XLE    Energy Select Sector SPDR Fund
    2000-06-16   IYE    iShares U.S. Energy ETF
    2004-09-29   VDE    Vanguard Energy ETF
    2006-04-10   USO    United States Oil Fund
    2006-06-22   XES    SPDR S&P Oil & Gas Equipment & Services ETF
    2006-06-22   XOP    SPDR S&P Oil & Gas Exploration & Production ETF
    2007-04-18   UNG    United States Natural Gas Fund
    2008-06-25   ICLN   iShares Global Clean Energy ETF
    2008-11-06   ERX    Direxion Daily Energy Bull 3X Shares
    2008-11-06   ERY    Direxion Daily Energy Bear 3x Shares
    2008-11-25   SCO    ProShares UltraShort Bloomberg Crude Oil
    2008-11-25   UCO    ProShares Ultra Bloomberg Crude Oil
    2009-06-02   AMJ    JPMorgan Alerian MLP Index ETN
    2010-06-02   BNO    United States Brent Oil Fund
    2010-08-25   AMLP   Alerian MLP ETF
    2011-12-21   OIH    VanEck Vectors Oil Services ETF
    2012-02-08   DGAZ   VelocityShares 3x Inverse Natural Gas
    2012-02-08   UGAZ   VelocityShares 3x Long Natural Gas
    2012-02-15   TAN    Invesco Solar ETF
    """


class SP500SectorsETFUniverse(InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following SP500 Sectors ETFs at their inception date
    1998-12-22   XLB   Materials Select Sector SPDR ETF
    1998-12-22   XLE   Energy Select Sector SPDR Fund
    1998-12-22   XLF   Financial Select Sector SPDR Fund
    1998-12-22   XLI   Industrial Select Sector SPDR Fund
    1998-12-22   XLK   Technology Select Sector SPDR Fund
    1998-12-22   XLP   Consumer Staples Select Sector SPDR Fund
    1998-12-22   XLU   Utilities Select Sector SPDR Fund
    1998-12-22   XLV   Health Care Select Sector SPDR Fund
    1998-12-22   XLY   Consumer Discretionary Select Sector SPDR Fund
    """


class VolatilityETFUniverse(InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following Volatility ETFs at their inception date
    2010-02-11   SQQQ   ProShares UltraPro ShortQQQ
    2010-02-11   TQQQ   ProShares UltraProQQQ
    2010-11-30   TVIX   VelocityShares Daily 2x VIX Short Term ETN
    2011-01-04   VIXY   ProShares VIX Short-Term Futures ETF
    2011-05-05   SPLV   Invesco S&P 500® Low Volatility ETF
    2011-10-04   SVXY   ProShares Short VIX Short-Term Futures
    2011-10-04   UVXY   ProShares Ultra VIX Short-Term Futures
    2011-10-20   EEMV   iShares Edge MSCI Min Vol Emerging Markets ETF
    2011-10-20   EFAV   iShares Edge MSCI Min Vol EAFE ETF
    2011-10-20   USMV   iShares Edge MSCI Min Vol USA ETF
    """


class InceptionDateUniverseSelectionModel(CustomUniverseSelectionModel):
    """
    Inception Date Universe that accepts a Dictionary of DateTime keyed by String that represent
    the Inception date for each ticker
    """


class FineFundamentalUniverseSelectionModel(FundamentalUniverseSelectionModel):
    """
    Portfolio selection model that uses coarse/fine selectors. For US equities only.
    """


class FutureUniverseSelectionModel(UniverseSelectionModel):
    """
    Provides an implementation of IUniverseSelectionModel that subscribes to future chains
    """


class FundamentalUniverseSelectionModel(UniverseSelectionModel, metaclass=abc.ABCMeta):
    """
    Provides a base class for defining equity coarse/fine fundamental selection models
    """


class OptionUniverseSelectionModel(UniverseSelectionModel):
    """
    Provides an implementation of IUniverseSelectionModel that subscribes to option chains
    """


class ScheduledUniverseSelectionModel(UniverseSelectionModel):
    """
    Defines a universe selection model that invokes a selector function on a specific scheduled given by an IDateRule and an ITimeRule
    """


class EmaCrossUniverseSelectionModel(FundamentalUniverseSelectionModel):
    """
    Provides an implementation of FundamentalUniverseSelectionModel that subscribes
    to symbols with the larger delta by percentage between the two exponential moving average
    """


class NullUniverseSelectionModel(UniverseSelectionModel):
    """
    Provides a null implementation of IUniverseSelectionModel
    """


class CustomUniverse(QuantConnect.Data.UniverseSelection.UserDefinedUniverse):
    """
    Defines a universe as a set of dynamically set symbols.
    """


class ManualUniverse(QuantConnect.Data.UniverseSelection.UserDefinedUniverse):
    """
    Defines a universe as a set of manually set symbols. This differs from UserDefinedUniverse
    in that these securities were not added via AddSecurity.
    """


class IUniverseSelectionModel(metaclass=abc.ABCMeta):
    """
    Algorithm framework model that defines the universes to be used by an algorithm
    """


class ManualUniverseSelectionModel(UniverseSelectionModel):
    """
    Provides an implementation of IUniverseSelectionModel that simply
    subscribes to the specified set of symbols
    """


class UniverseSelectionModel(IUniverseSelectionModel):
    """
    Provides a base class for universe selection models.
    """


class UniverseSelectionModelPythonWrapper(UniverseSelectionModel):
    """
    Provides an implementation of IUniverseSelectionModel that wraps a PyObject object
    """


class CompositeUniverseSelectionModel(UniverseSelectionModel):
    """
    Provides an implementation of IUniverseSelectionModel that combines multiple universe
    selection models into a single model.
    """


class CustomUniverseSelectionModel(UniverseSelectionModel):
    """
    Provides an implementation of IUniverseSelectionModel that simply
    subscribes to the specified set of symbols
    """



import QuantConnect.Data


class Fred(QuantConnect.Data.BaseData):
    """
    This class has no documentation.
    """


    class CBOE:
        """
        This class has no documentation.
        """


    class OECDRecessionIndicators:
        """
        These time series is an interpretation of Organisation of Economic Development (OECD) Composite Leading Indicators: Reference Turning Points and Component Series data, which can be found at http://www.oecd.org/std/leading-indicators/oecdcompositeleadingindicatorsreferenceturningpointsandcomponentseries.htm. The OECD identifies months of turning points without designating a date within the month that turning points occurred. The dummy variable adopts an arbitrary convention that the turning point occurred at a specific date within the month. The arbitrary convention does not reflect any judgment on this issue by the OECD. Our time series is composed of dummy variables that represent periods of expansion and recession. A value of 1 is a recessionary period, while a value of 0 is an expansionary period. For this time series, the recession begins on the 15th day of the month of the peak and ends on the 15th day of the month of the trough. This time series is a disaggregation of the monthly series. For more options on recession shading, see the note and links below.
        The recession shading data that we provide initially comes from the source as a list of dates that are either an economic peak or trough. We interpret dates into recession shading data using one of three arbitrary methods. All of our recession shading data is available using all three interpretations. The period between a peak and trough is always shaded as a recession. The peak and trough are collectively extrema. Depending on the application, the extrema, both individually and collectively, may be included in the recession period in whole or in part. In situations where a portion of a period is included in the recession, the whole period is deemed to be included in the recession period.
        The first interpretation, known as the midpoint method, is to show a recession from the midpoint of the peak through the midpoint of the trough for monthly and quarterly data. For daily data, the recession begins on the 15th of the month of the peak and ends on the 15th of the month of the trough. Daily data is a disaggregation of monthly data. For monthly and quarterly data, the entire peak and trough periods are included in the recession shading. This method shows the maximum number of periods as a recession for monthly and quarterly data. The Federal Reserve Bank of St. Louis uses this method in its own publications. The midpoint method is used for this series.
        The second interpretation, known as the trough method, is to show a recession from the period following the peak through the trough (i.e. the peak is not included in the recession shading, but the trough is). For daily data, the recession begins on the first day of the first month following the peak and ends on the last day of the month of the trough. Daily data is a disaggregation of monthly data. The trough method is used when displaying data on FRED graphs. A version of this time series represented using the trough method can be found at:
        The third interpretation, known as the peak method, is to show a recession from the period of the peak to the trough (i.e. the peak is included in the recession shading, but the trough is not). For daily data, the recession begins on the first day of the month of the peak and ends on the last day of the month preceding the trough. Daily data is a disaggregation of monthly data. A version of this time series represented using the peak method can be found at:
        The OECD CLI system is based on the "growth cycle" approach, where business cycles and turning points are measured and identified in the deviation-from-trend series. The main reference series used in the OECD CLI system for the majority of countries is industrial production (IIP) covering all industry sectors excluding construction. This series is used because of its cyclical sensitivity and monthly availability, while the broad based Gross Domestic Product (GDP) is used to supplement the IIP series for identification of the final reference turning points in the growth cycle.
        Zones aggregates of the CLIs and the reference series are calculated as weighted averages of the corresponding zone member series (i.e. CLIs and IIPs).
        Up to December 2008 the turning points chronologies shown for regional/zone area aggregates or individual countries are determined by the rules established by the National Bureau of Economic Research (NBER) in the United States, which have been formalized and incorporated in a computer routine (Bry and Boschan) and included in the Phase-Average Trend (PAT) de-trending procedure. Starting from December 2008 the turning point detection algorithm is decoupled from the de-trending procedure, and is a simplified version of the original Bry and Boschan routine. (The routine parses local minima and maxima in the cycle series and applies censor rules to guarantee alternating peaks and troughs, as well as phase and cycle length constraints.)
        The components of the CLI are time series which exhibit leading relationship with the reference series (IIP) at turning points. Country CLIs are compiled by combining de-trended smoothed and normalized components. The component series for each country are selected based on various criteria such as economic significance; cyclical behavior; data quality; timeliness and availability.
        OECD data should be cited as follows: OECD Composite Leading Indicators, "Composite Leading Indicators: Reference Turning Points and Component Series", http://www.oecd.org/std/leading-indicators/oecdcompositeleadingindicatorsreferenceturningpointsandcomponentseries.htm
        """


    class ICEBofAML:
        """
        This class has no documentation.
        """


    class Wilshire:
        """
        Wilshire Indexes help clients, investment professionals and researchers accurately measure and better understand the market. The Wilshire Index family leverages more than 40 years of Wilshire performance measurement expertise and employs unbiased construction rules.
        """


    class CentralBankInterventions:
        """
        This class has no documentation.
        """


    class LIBOR:
        """
        This class has no documentation.
        """


    class TradeWeightedIndexes:
        """
        This class has no documentation.
        """


    class CommercialPaper:
        """
        Commercial paper (CP) consists of short-term, promissory notes issued primarily by corporations. Maturities range up to 270 days but average about 30 days. Many companies use CP to raise cash needed for current transactions, and many find it to be a lower-cost alternative to bank loans.
        The Federal Reserve Board disseminates information on CP primarily through its World Wide Web site. In addition, the Board publishes one-, two-, and three-month rates on AA nonfinancial and AA financial CP weekly in its H.15 Statistical Release.
        The Federal Reserve Board's CP release is derived from data supplied by The Depository Trust & Clearing Corporation (DTCC), a national clearinghouse for the settlement of securities trades and a custodian for securities. DTCC performs these functions for almost all activity in the domestic CP market. The Federal Reserve Board only considers maturities of 270 days or less. CP is exempt from SEC registration if its maturity does not exceed 270 days.
        Data on CP issuance rates and volumes typically are updated daily and typically posted with a one-day lag. Data on CP outstanding usually are available as of the close of business each Wednesday and as of the last business day of the month; these data are also posted with a one-day lag. The daily CP release will usually be available at 9:45 a.m. EST. However, the Federal Reserve Board makes no guarantee regarding the timing of the daily CP release. This policy is subject to change at any time without notice.
        """


class Observation:
    """
    This class has no documentation.
    """


class FredApi(QuantConnect.Data.BaseData):
    """
    This class has no documentation.
    """



import QuantConnect.Data


class FxcmVolume(QuantConnect.Data.BaseData):
    """
    FXCM Real FOREX Volume and Transaction data from its clients base, available for the following pairs:
        - EURUSD, USDJPY, GBPUSD, USDCHF, EURCHF, AUDUSD, USDCAD,
          NZDUSD, EURGBP, EURJPY, GBPJPY, EURAUD, EURCAD, AUDJPY
        FXCM only provides support for FX symbols which produced over 110 million average daily volume (ADV) during 2013.
        This limit is imposed to ensure we do not highlight low volume/low ticket symbols in addition to other financial
        reporting concerns.
    """


class Quandl(QuantConnect.Data.DynamicData):
    """
    Quandl Data Type - Import generic data from quandl, without needing to define Reader methods.
    This reads the headers of the data imported, and dynamically creates properties for the imported data.
    """


class NullData(QuantConnect.Data.BaseData):
    """
    Represents a custom data type that works as a heartbeat of data in live mode
    """


class USEnergyAPI(QuantConnect.Data.BaseData):
    """
    US Energy Information Administration provides extensive data on energy usage, import, export,
    and forecasting across all US energy sectors.
    https://www.eia.gov/opendata/
    """



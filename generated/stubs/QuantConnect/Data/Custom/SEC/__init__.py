import QuantConnect.Data
import abc
import typing


IsoDateTimeConverter = typing.Any


class SECReportFormerCompany:
    """
    This class has no documentation.
    """


class SECReportMailAddress:
    """
    This class has no documentation.
    """


class SECReportFactory:
    """
    This class has no documentation.
    """


class SECReportFiler:
    """
    This class has no documentation.
    """


class SECReportDateTimeConverter(IsoDateTimeConverter):
    """
    Specifies format for parsing DateTime values from SEC data
    """


class SECReportSubmission:
    """
    This class has no documentation.
    """


class SECReportCompanyData:
    """
    This class has no documentation.
    """


class SECReport10Q(QuantConnect.Data.BaseData, ISECReport):
    """
    SEC 10-Q report (quarterly earnings) BaseData implementation.
    Using this class, you can retrieve SEC report data for a security if it exists.
    If the ticker you want no longer trades, you can also use the CIK of the company
    you want data for as well except for currently traded stocks. This may change in the future.
    """


class SECReportBusinessAddress:
    """
    This class has no documentation.
    """


class SECReportDocument:
    """
    This class has no documentation.
    """


class ISECReport(QuantConnect.Data.IBaseData, metaclass=abc.ABCMeta):
    """
    Base interface for all SEC report types.
    Using an interface, we can retrieve all report types with a single
    call to Slice.Get{T}()
    """


class SECReportIndexFile:
    """
    This class has no documentation.
    """


class SECReportIndexDirectory:
    """
    This class has no documentation.
    """


class SECReportIndexItem:
    """
    This class has no documentation.
    """


class SECReport8K(QuantConnect.Data.BaseData, ISECReport):
    """
    SEC 8-K report (important investor notices) BaseData implementation.
    Using this class, you can retrieve SEC report data for a security if it exists.
    If the ticker you want no longer trades, you can also use the CIK of the company
    you want data for as well except for currently traded stocks. This may change in the future.
    """


class SECReportFilingValues:
    """
    This class has no documentation.
    """


class SECReport10K(QuantConnect.Data.BaseData, ISECReport):
    """
    SEC 10-K report (annual earnings) BaseData implementation.
    Using this class, you can retrieve SEC report data for a security if it exists.
    If the ticker you want no longer trades, you can also use the CIK of the company
    you want data for as well except for currently traded stocks. This may change in the future.
    """



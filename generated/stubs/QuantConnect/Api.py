import QuantConnect.Interfaces
import enum


class Api(QuantConnect.Interfaces.IApi, QuantConnect.Interfaces.IDownloadProvider):
    """
    QuantConnect.com Interaction Via API.
    """


class ApiConnection:
    """
    API Connection and Hash Manager
    """


class RestResponse:
    """
    Base API response class for the QuantConnect API.
    """


class Project(RestResponse):
    """
    Response from reading a project by id.
    """


class ProjectResponse(RestResponse):
    """
    Project list response
    """


class Compile(RestResponse):
    """
    Response from the compiler on a build event
    """


class Backtest(RestResponse):
    """
    Backtest response packet from the QuantConnect.com API.
    """


class BacktestList(RestResponse):
    """
    Collection container for a list of backtests for a project
    """


class BacktestReport(RestResponse):
    """
    Backtest Report Response wrapper
    """


class ProjectFile:
    """
    File for a project
    """


class ProjectFilesResponse(RestResponse):
    """
    Response received when reading all files of a project
    """


class Link(RestResponse):
    """
    Response from reading purchased data
    """


class CompileState(enum.Enum):
    """
    State of the compilation request
    """


class AuthenticationResponse(RestResponse):
    """
    Verify if the credentials are OK.
    """



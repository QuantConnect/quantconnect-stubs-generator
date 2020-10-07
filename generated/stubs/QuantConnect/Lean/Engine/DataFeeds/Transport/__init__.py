import QuantConnect.Interfaces


class LocalFileSubscriptionStreamReader(QuantConnect.Interfaces.IStreamReader):
    """
    Represents a stream reader capable of reading lines from disk
    """


class RestSubscriptionStreamReader(QuantConnect.Interfaces.IStreamReader):
    """
    Represents a stream reader capable of polling a rest client
    """


class RemoteFileSubscriptionStreamReader(QuantConnect.Interfaces.IStreamReader):
    """
    Represents a stream reader capabable of downloading a remote file and then
    reading it from disk
    """



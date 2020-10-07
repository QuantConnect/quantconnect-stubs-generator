import QuantConnect.Interfaces


class LiveDataQueue(QuantConnect.Interfaces.IDataQueueHandler):
    """
    Live Data Queue is the cut out implementation of how to bind a custom live data source
    """


class FakeDataQueue(QuantConnect.Interfaces.IDataQueueHandler):
    """
    This is an implementation of IDataQueueHandler used for testing
    """



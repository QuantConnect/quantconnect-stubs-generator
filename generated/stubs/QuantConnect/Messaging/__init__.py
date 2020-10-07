import QuantConnect.Interfaces


class EventMessagingHandler(QuantConnect.Interfaces.IMessagingHandler):
    """
    Desktop implementation of messaging system for Lean Engine
    """


class Messaging(QuantConnect.Interfaces.IMessagingHandler):
    """
    Local/desktop implementation of messaging system for Lean Engine.
    """


class StreamingMessageHandler(QuantConnect.Interfaces.IMessagingHandler):
    """
    Message handler that sends messages over tcp using NetMQ.
    """



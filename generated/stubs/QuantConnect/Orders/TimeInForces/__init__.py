import QuantConnect.Orders


class DayTimeInForce(QuantConnect.Orders.TimeInForce):
    """
    Day Time In Force - order expires at market close
    """


class GoodTilCanceledTimeInForce(QuantConnect.Orders.TimeInForce):
    """
    Good Til Canceled Time In Force - order does never expires
    """


class GoodTilDateTimeInForce(QuantConnect.Orders.TimeInForce):
    """
    Good Til Date Time In Force - order expires and will be cancelled on a fixed date/time
    """



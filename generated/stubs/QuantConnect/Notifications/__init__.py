import abc


class NotificationManager:
    """
    Local/desktop implementation of messaging system for Lean Engine.
    """


class Notification(metaclass=abc.ABCMeta):
    """
    Local/desktop implementation of messaging system for Lean Engine.
    """


class NotificationWeb(Notification):
    """
    Web Notification Class
    """


class NotificationSms(Notification):
    """
    Sms Notification Class
    """


class NotificationEmail(Notification):
    """
    Email notification data.
    """



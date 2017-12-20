from notifications import Notification
from tools import jsonManager as jsonM


def get_notifications():
    notifications = list()
    data = jsonM.get_from_url('https://api.picarto.tv/v1/user/notifications')

    for notification in data:
        notifications.append(Notification(notification))

    return notifications

def filter_notifications_by_type(notifications, type):
    new_notifications = list()

    for notification in notifications:
        if notification.get_type() == type:
            new_notifications.append(notification)

    return new_notifications
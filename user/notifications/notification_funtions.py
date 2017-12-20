from notifications import Notification
import jsonManager as jsonM

def get_notifications():
    notifications = list(Notification)
    data = jsonM.get_from_url('https://api.picarto.tv/v1/user/notifications')

    for notification in data:
        notifications.append(Notification(notification))

    return notifications
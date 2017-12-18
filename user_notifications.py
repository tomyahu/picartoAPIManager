import jsonManager as jsonM

class Notification():

    def __init__(self, notification):
        self.channel = notification['channel']
        self.type = notification['type']
        self.read = not notification['unread']
        self.url = notification['uri']


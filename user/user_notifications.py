import jsonManager as jsonM

class Notification():

    def __init__(self, notification):
        self.channel = notification['channel']
        self.type = notification['type']
        self.read = not notification['unread']
        self.url = notification['uri']

    def get_channel(self):
        return self.channel

    def get_type(self):
        return self.type

    def get_url(self):
        return self.url

    def is_read(self):
        return self.read

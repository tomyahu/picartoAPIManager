class Notification:

    def __init__(self, data):
        """
        Creates a new instance of the type Notification
        :param data: The data of the Notification
        """
        # type: dict -> None
        self.channel = data['channel']
        self.type = data['type']
        self.read = not data['unread']
        self.url = data['uri']
        self.icon = data['has_icon']

    def get_channel(self):
        return self.channel

    def get_type(self):
        return self.type

    def get_url(self):
        return self.url

    def is_read(self):
        return self.read

    def has_icon(self):
        return self.icon
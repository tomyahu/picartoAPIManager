import abc


class AbstractUser(abc.ABCMeta):

    def __init__(self, data):
        self.id = data['user_id']
        self.name = data['name']
        self.online = data['online']

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def is_online(self):
        return self.online


class RegularUser(AbstractUser):

    def __init__(self, data):
        AbstractUser.__init__(data)
        self.avatar_url = data['avatar']

    def get_avatar_url(self):
        return self.avatar_url


class MultistreamUser(AbstractUser):

    def __init__(self, user):
        AbstractUser.__init__(data)
        self.adult = user['adult']

    def is_adult(self):
        return self.adult

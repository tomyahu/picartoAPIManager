class MultistreamUser():

    def __init__(self, user):
        self.id = user['user_id']
        self.name = user['name']
        self.online = user['online']
        self.adult = user['adult']

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def is_online(self):
        return self.online

    def is_adult(self):
        return self.adult
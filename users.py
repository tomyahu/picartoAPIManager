

class MultistreamUser():

    def __init__(self, user):
        self.id = user['user_id']
        self.name = user['name']
        self.online = user['online']
        self.adult = user['adult']
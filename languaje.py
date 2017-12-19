

class Languaje():

    def __init__(self, languaje):
        self.id = languaje['id']
        self.country = languaje['name']

    def get_id(self):
        return self.id

    def get_country(self):
        return self.country
import jsonManager as jsonM
from .components.descriptionPanel import Description_Panel
from .components.languaje import Languaje
from .components.thumbnails import Thumbnails

preurl = 'https://api.picarto.tv/v1/'

class Channel():

    def __init__(self, name):
        data = jsonM.get_from_url(preurl + '/channel/name/' + name)
        self.set_data(data)

    def __init__(self, id):
        data = jsonM.get_from_url(preurl + '/channel/id/' + id)
        self.set_data(data)

    def __init__(self, data):
        self.set_data(data)

    def set_data(self, data):
        self.name = data['name']
        self.user_id = data['user_id']
        self.avatar = data['avatar']
        self.online = data['online']
        self.viewers = data['viewers']
        self.total_views = data['viewers_total']
        self.thumbnails = Thumbnails(data['thumbnails'])

        self.followers = data['followers']
        self.subscribers = data['subscribers']
        self.adult = data['adult']
        self.category = data['category']
        self.account_type = data['account_type']
        self.commissions = data['commissions']
        self.title = data['title']
        self.description_panels = []

        for panel in data['description_panels']:
            self.description_panels += [Description_Panel(panel)]

        self.private = data['private']
        self.gaming = data['gaming']
        self.guest_chat = data['guest_chat']
        self.last_live = data['last_live']
        self.tags = []

        for tag in data['tags']:
            self.tags += [tag]

        self.multistream = []

        for user in data['multistream']:
            self.multistream += [user]

        self.languajes = []

        for languaje in data['languajes']:
            self.languajes += [Languaje(data['languajes'])]

    #Getters
    def get_name(self):
        return self.name

    def get_id(self):
        return self.user_id

    def get_viewer_amount(self):
        return self.viewers

    def get_total_views(self):
        return self.total_views

    def follower_number(self):
        return self.followers

    def get_subscribers(self):
        return self.subscribers

    def get_title(self):
        return self.title

    def get_category(self):
        return self.category

    def get_tags(self):
        return self.tags

    def get_languajes(self):
        return self.languajes

    def get_account_type(self):
        return self.account_type

    def get_description_panels(self):
        return self.description_panels

    def get_multistream_users(self):
        return self.multistream

    def is_online(self):
        return self.online

    def is_adult(self):
        return self.adult

    def is_acepting_commissions(self):
        return self.commissions

    def is_private(self):
        return self.private

    def is_gaming(self):
        return self.gaming

    def can_guests_chat(self):
        return self.guest_chat





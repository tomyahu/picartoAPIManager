import jsonManager as jsonM

preurl = 'https://api.picarto.tv/v1/'

class Thumbnails():

    def __init__(self, thumbnail_list):
        self.web = thumbnail_list['web']
        self.web_large = thumbnail_list['web_large']
        self.mobile = thumbnail_list['mobile']
        self.tablet = thumbnail_list['tablet']


class Description_Panel():

    def __init__(self, descrption_panel):
        self.title = descrption_panel['title']
        self.body = descrption_panel['body']
        self.image = descrption_panel['image']
        self.image_link = descrption_panel['image_link']
        self.button_text = descrption_panel['button_text']
        self.button_link = descrption_panel['button_link']
        self.position = descrption_panel['position']


class Languaje():

    def __init__(self, languaje):
        self.id = languaje['id']
        self.country = languaje['name']


class Channel():

    def __init__(self, name):
        data = jsonM.get_from_url(preurl + '/channel/name/' + name)
        self.set_data(data)

    def __init__(self, id):
        data = jsonM.get_from_url(preurl + '/channel/id/' + id)
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
        self.account_type = data['free']
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

        self.multistream = data['multistream']
        self.languajes = []

        for languaje in data['languajes']:
            self.languajes += [Languaje(data['languajes'])]

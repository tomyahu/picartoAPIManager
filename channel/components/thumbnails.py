class Thumbnails():

    def __init__(self, thumbnail_list):
        self.web = thumbnail_list['web']
        self.web_large = thumbnail_list['web_large']
        self.mobile = thumbnail_list['mobile']
        self.tablet = thumbnail_list['tablet']

    def get_web_url(self):
        return self.web

    def get_web_large_url(self):
        return self.web_large

    def get_mobile_url(self):
        return self.mobile

    def get_tablet_url(self):
        return self.tablet


class Description_Panel():

    def __init__(self, descrption_panel):
        self.title = descrption_panel['title']
        self.body = descrption_panel['body']
        self.image = descrption_panel['image']
        self.image_link = descrption_panel['image_link']
        self.button_text = descrption_panel['button_text']
        self.button_link = descrption_panel['button_link']
        self.position = descrption_panel['position']

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_image_url(self):
        return self.image

    def get_image_link(self):
        return self.image_link

    def get_button_text(self):
        return self.button_text

    def get_button_link(self):
        return self.button_link

    def get_position(self):
        return self.position
class UtilsMixin:

    def set_image_urls(self, media):
        if media['config_width'] == 640:
            self.image_thumbnail_url = media['src']
        elif media['config_width'] == 750:
            self.image_low_resolution_url = media['src']
        elif media['config_width'] == 1080:
            self.image_standard_resolution_url = media['src']

from .mixins import UtilsMixin


class CarouselMedia(UtilsMixin):

    def __init__(self):
        self.type = ''
        self.image_thumbnail_url = ''
        self.image_low_resolution_url = ''
        self.image_standard_resolution_url = ''
        self.image_high_resolution_url = ''
        self.video_thumbnail_url = ''
        self.video_low_resolution_url = ''
        self.video_standard_resolution_url = ''
        self.video_high_resolution_url = ''

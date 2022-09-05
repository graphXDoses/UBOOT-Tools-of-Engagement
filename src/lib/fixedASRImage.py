from kivy.uix.image import Image

class FixedASRImage(Image):

    def __init__(self, source):
        super(FixedASRImage, self).__init__(source=source)
        self.allow_stretch = True
        self.keep_ratio    = True

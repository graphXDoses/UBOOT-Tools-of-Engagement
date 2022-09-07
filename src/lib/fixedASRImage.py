########################################################
# fixedASRImage.py
# Xristos Dosis
# August 6, 2022
#
# Derivative of Kivy Image class, with fixed aspect
# ratio.
########################################################

from kivy.uix.image import Image

class FixedASRImage(Image):

    def __init__(self, source):
        super(FixedASRImage, self).__init__(source=source)
        self.allow_stretch = True
        self.keep_ratio    = True

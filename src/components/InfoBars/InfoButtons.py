########################################################
# InfoButtons.py
# Xristos Dosis
# August 6, 2022
#
# UI Layout for info bar displaying active button
# and part name.
########################################################

from src.constants.EventNames import EVENTS
from src.components.Layouts.InfoLayout import InfoLayout

class InfoButtons(InfoLayout):

    def __init__(self):
        super().__init__(EVENTS.CHANGE_FOCUS)

    def updateLabelCallback(self, object):
        if isinstance(object.attachment, list):
            self.InfoLabel.text = object.attachment[0]
        else:
            self.InfoLabel.text = object.attachment

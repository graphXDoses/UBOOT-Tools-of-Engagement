########################################################
# InfoContext.py
# Xristos Dosis
# August 6, 2022
#
# UI Layout for info bar displaying current context.
########################################################

from src.constants.EventNames import EVENTS
from src.components.Layouts.InfoLayout import InfoLayout

class InfoContext(InfoLayout):

    def __init__(self):
        super().__init__(EVENTS.CHANGE_CONTEXT)

    def updateLabelCallback(self, context):
        self.InfoLabel.text = context

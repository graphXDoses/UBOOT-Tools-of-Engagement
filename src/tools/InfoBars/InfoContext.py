from src.constants.EventNames import EVENTS
from src.tools.Layouts.InfoLayout import InfoLayout

class InfoContext(InfoLayout):

    def __init__(self):
        super().__init__(EVENTS.CHANGE_CONTEXT)

    def updateLabelCallback(self, context):
        self.InfoLabel.text = context

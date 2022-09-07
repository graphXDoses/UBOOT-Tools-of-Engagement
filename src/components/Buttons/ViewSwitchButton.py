########################################################
# ViewSwitchButton.py
# Xristos Dosis
# August 6, 2022
#
# Derivative class of Button, dedicated to triggering
# 'CHANGE_VIEW' events.
########################################################

from src.constants.EventNames import EVENTS
from src.constants.UI import VIEWS_POOL
from src.lib.EventBus import EventBus
from src.components.Buttons.ButtonModel import Button

class ViewSwitchButton(Button):

    def __init__(self, source, text="Switch", portalTo=VIEWS_POOL.SETTINGSVIEW):
        if source is None:
            super(ViewSwitchButton, self).__init__(source, useShaders=False)
            self.text = text
        else:
            super(ViewSwitchButton, self).__init__(source)
        self.portalTo = portalTo

        self.bind(on_press=self.keyDown)
        self.bind(on_release=self.__viewSwitchCallback)

    @staticmethod
    def __viewSwitchCallback(i=None):
        if not i.currentImage is None:
            i.canvas["hasFocus"] = 0.0
        EventBus.trigger(EVENTS.CHANGE_VIEW, i.portalTo)

    @staticmethod
    def keyDown(i=None):
        if not i.currentImage is None:
            i.canvas["hasFocus"] = 1.0

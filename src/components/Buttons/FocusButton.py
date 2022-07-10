from kivy.graphics import Color, Rectangle
from src.constants.Colors import (
    BUTTON_NORMAL_BACKGROUND_COLOR,
    BUTTON_ILLUMINATION_BACKGROUND_COLOR,
    ICON_NORMAL_BACKGROUND_COLOR,
    ICON_ILLUMINATION_BACKGROUND_COLOR
)
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus
from src.components.Buttons.ButtonModel import Button

class FocusButton(Button):

    def __init__(self, source, attachment, context):
        super(FocusButton, self).__init__(source)
        self.context = context
        self.attachment = [attachment]

        self.bind(on_press=self.setFocus)
        EventBus.on(EVENTS.CHANGE_FOCUS, self.__focusChangeCallback)

    @staticmethod
    def setFocus(i=None):
        i.canvas["hasFocus"] = 1.0
        EventBus.trigger(EVENTS.CHANGE_FOCUS, i)

    def __focusChangeCallback(self, button):
        if not button is self:
            self.canvas["hasFocus"] = 0.0

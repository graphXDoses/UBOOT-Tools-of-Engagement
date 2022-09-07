########################################################
# ResetButton.py
# Xristos Dosis
# August 6, 2022
#
# Derivative class of Button, dedicated to triggering
# 'RESET' events.
########################################################

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

class ResetButton(Button):

    def __init__(self, source, context):
        super().__init__(source)
        self.context = context

        self.bind(on_press=self.keyDown)
        self.bind(on_release=self.__resetCallback)

    @staticmethod
    def __resetCallback(i=None):
        i.canvas["hasFocus"] = 0.0
        EventBus.trigger(EVENTS.RESET, i.context)

    @staticmethod
    def keyDown(i=None):
        i.canvas["hasFocus"] = 1.0

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

class LinkFocusButton(Button):

    def __init__(self, source, attachment, context):
        super(LinkFocusButton, self).__init__(source)
        # self.link = source[1]
        self.context = context
        self.attachment = [attachment]
        self.pressed_counter = self.__pressCounter()

        self.bind(on_press=self.setFocus)
        EventBus.on(EVENTS.CHANGE_FOCUS, self.__focusChangeCallback)
        # EventBus.on(EVENTS.ENTER_LINK, self.__addLink)
        # EventBus.on(EVENTS.BREAK_LINK, self.__removeLink)
        EventBus.on(EVENTS.RESET, self.__reset)

    def __pressCounter(self):
        n = 1
        while 1:
            n += 1
            yield n

    # def __addLink(self):
    #     self.currentImage = self.link
    #
    # def __removeLink(self):
    #     self.currentImage = self.source

    def __reset(self, context):
        if context == self.context:
            EventBus.trigger(EVENTS.BREAK_LINK)
            self.pressed_counter = self.__pressCounter()
            self.nextDraw()

    @staticmethod
    def setFocus(i=None):
        if i.canvas["hasFocus"] == 1.0:
            pressCounter = next(i.pressed_counter)

            if pressCounter % 2 == 0 and pressCounter > 0:
                EventBus.trigger(EVENTS.ENTER_LINK)
            elif pressCounter % 2 == 1:
                EventBus.trigger(EVENTS.BREAK_LINK)

        i.canvas["hasFocus"] = 1.0
        EventBus.trigger(EVENTS.CHANGE_FOCUS, i)

    def __focusChangeCallback(self, button):
        if not button is self:
            self.canvas["hasFocus"] = 0.0

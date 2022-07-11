from kivy.uix.floatlayout import FloatLayout
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus
from src.lib.AppConfig import AppConfig

class PartModel(FloatLayout):

    def __init__(self, context):
        super().__init__()
        self.__target = None
        self.context = context
        EventBus.on(EVENTS.CHANGE_FOCUS, self.__focus)
        EventBus.on(EVENTS.CHANGE_CONTEXT, self.__aquireContext)

    def __focus(self, button):
        self.__target = list(filter(lambda item: item.name in button.attachment, self.children))

    def __aquireContext(self, context):
        if self.context == context:
            for child in self.children:
                if not child.isFixed:
                    initAngle = AppConfig.getInitAngle(child.name)
                    if initAngle != child.getAngle:
                        child.rotateBy(initAngle)
                        child.updateAngle()

    def rotate(self, value):
        for target in self.__target:
            target.rotateBy(value)

    def updateAngle(self):
        for target in self.__target:
            target.updateAngle()

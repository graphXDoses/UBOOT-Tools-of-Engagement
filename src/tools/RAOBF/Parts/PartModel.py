from kivy.uix.floatlayout import FloatLayout
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus

class PartModel(FloatLayout):

    def __init__(self):
        super().__init__()
        self.__target = None
        EventBus.on(EVENTS.CHANGE_FOCUS, self.__focus)

    def __focus(self, button):
        self.__target = list(filter(lambda item: item.name in button.attachment, self.children))

    def rotate(self, value):
        for target in self.__target:
            target.rotateBy(value)

    def updateAngle(self):
        for target in self.__target:
            target.updateAngle()

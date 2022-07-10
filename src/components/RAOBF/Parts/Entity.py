from kivy.graphics import Rotate, PushMatrix, PopMatrix
from src.constants.EventNames import EVENTS
from src.lib.fixedASRImage import FixedASRImage
from src.lib.EventBus import EventBus
from src.lib.AppConfig import AppConfig

class Entity(FixedASRImage):

    def __init__(self, img, name, context, isFixed=False):
        super().__init__(source=img)
        self.name = name
        self.context = context
        self.isFixed = isFixed
        self.__rotation = Rotate(origin=self.center, angle=0)
        self.__rectAngle = self.__rotation.angle

        if not self.isFixed:
            initAngle = AppConfig.getInitAngle(self.name)
            EventBus.on(EVENTS.RESET, self.__resetCallback)
        # with self.canvas:
        if not self.isFixed:
            if initAngle != 0:
                self.rotateBy(initAngle)
                self.updateAngle()
        self.bind(center=self.redraw)
        self.canvas.ask_update()

    def redraw(self, *args):
        self.center = self.parent.center
        self.__rotation.origin = self.center

    def rotateBy(self, value):
        if not self.isFixed:
            if value >= 360: value  -= 360
            if value <= -360: value += 360
            self.canvas.clear()
            with self.canvas:
                PushMatrix()
                self.__rotation = Rotate(origin=self.center, angle=self.__rectAngle+value)
                super().__init__(source=self.source)
                PopMatrix()

    def updateAngle(self):
        if not self.isFixed:
            self.__rectAngle = self.__rotation.angle
            EventBus.trigger(EVENTS.CHANGE_VALUE, self.name, self.__rectAngle)

    def __resetCallback(self, context):
        if context == self.context:
            self.canvas.clear()
            self.__rotation.angle = 0
            AppConfig.reset(self.name)
            self.__rectAngle = self.__rotation.angle
            with self.canvas:
                PushMatrix()
                self.__rotation = Rotate(origin=self.center, angle=0)
                super().__init__(source=self.source)
                PopMatrix()

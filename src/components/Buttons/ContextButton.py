from kivy.clock import mainthread
from kivy.graphics import Color, Rectangle
from src.constants.UI import CONTEXT_POOL, default_context
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus
from src.components.Buttons.ButtonModel import Button

class ContextButton(Button):

    def __init__(self, source):
        super(ContextButton, self).__init__(source, useShaders=False)
        self.frontSide      = source[0]
        self.backSide       = source[1]
        self.context        = self.flip()
        self.currentContext = default_context
        self.currentImage   = self.backSide

        self.bind(on_release=self.changeContext)
        EventBus.on(EVENTS.CHANGE_CONTEXT, self.__changeContextCallback)

        self.nextDraw()

    def flip(self):
        n = 0
        pool = [CONTEXT_POOL.ATTACK_DISC, CONTEXT_POOL.SLIDE_RULE_DISC]
        while 1:
            n += 1
            yield pool[n % 2]

    @staticmethod
    def changeContext(i=None):
        EventBus.trigger(EVENTS.CHANGE_CONTEXT, next(i.context))

    def __changeContextCallback(self, context):
        if context == CONTEXT_POOL.ATTACK_DISC:
            self.currentImage = self.backSide
        elif context == CONTEXT_POOL.SLIDE_RULE_DISC:
            self.currentImage = self.frontSide

        self.canvas.clear()
        with self.canvas:
            self.bg = Rectangle(pos=self.pos, size=self.size, texture=self.currentImage)

    @mainthread
    def nextDraw(self):
        self.canvas.clear()
        with self.canvas:
            self.bg = Rectangle(pos=self.pos, size=self.size, texture=self.currentImage)
        self.bind(pos=self.syncValues, size=self.syncValues)

    def syncValues(self, *args):
        self.bg.pos  = self.pos
        self.bg.size = self.size

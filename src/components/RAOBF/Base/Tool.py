########################################################
# Tool.py
# Xristos Dosis
# August 6, 2022
#
# Extends the Kivy FloatLayout class. Works as basis for
# all tool objects.
########################################################

from kivy.uix.floatlayout import FloatLayout
from src.components.RAOBF.Base.Part import Part
from src.constants.RaobfNames import *
from src.constants.Images import IMAGES
from src.constants.UI import CONTEXT_POOL
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus
from src.lib.AppConfig import AppConfig

class Tool(FloatLayout):

    def __init__(self, context):
        super().__init__()
        self.__target = None
        self.context = context
        self._widgetSetup()
        EventBus.on(EVENTS.CHANGE_FOCUS, self.__focus)
        EventBus.on(EVENTS.CHANGE_CONTEXT, self.__aquireContext)

    def _widgetSetup(self):
        rContext = CONTEXT_POOL.findByVal(self.context)
        rImgs = IMAGES.__dict__[rContext].__dict__

        for alias, img in rImgs.items():
            Name = next( ( v for k,v in globals().items() if k == alias ) )
            if not alias in ('RB', 'AOB'):
                part = Part(
                    img,
                    name = repr(Name),
                    context = self.context
                )
            else:
                part = Part(
                    img,
                    name = repr(Name),
                    context = self.context,
                    isFixed = True
                )
            self.add_widget(part)
            setattr(
                self,
                '_{}'.format(alias),
                part
            )

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

    def getAngle(self):
        return self.__target[-1].getAngle

    def rotate(self, value):
        for target in self.__target:
            target.rotateBy(value)

    def updateAngle(self):
        for target in self.__target:
            target.updateAngle()

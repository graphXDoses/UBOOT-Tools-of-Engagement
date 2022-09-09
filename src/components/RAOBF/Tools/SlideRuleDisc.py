########################################################
# SlideRuleDisc.py
# Xristos Dosis
# August 6, 2022
#
# Extends the Tool class. Instantiates all relevant parts
# and appends them to the layout. Manipulates children
# parts with own callback functions for focus and
# rotation difference.
########################################################

from src.components.RAOBF.Base.Tool import Tool
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus


class SlideRuleDisc(Tool):

    def __init__(self, context):
        super().__init__(context)
        self.__target = self._DS
        EventBus.on(EVENTS.CHANGE_FOCUS, self.__focus)

    def __focus(self, button):
        self.__target = list(filter(lambda item: item.name in button.attachment, self.children))

    def rotate(self, value):
        for target in self.__target:
            target.rotateBy(value)

    def updateAngle(self):
        for target in self.__target:
            target.updateAngle()

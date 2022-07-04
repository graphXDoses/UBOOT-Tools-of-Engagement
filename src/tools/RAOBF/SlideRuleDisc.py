from src.tools.RAOBF.Parts.Entity import Entity
from src.tools.RAOBF.Parts.PartModel import PartModel
from src.constants.RaobfNames import AOB, DS, TM
from src.constants.Images import IMAGES
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus


class SlideRuleDisc(PartModel):

    def __init__(self, context):
        super().__init__()
        self.context = context

        self._AOB   = Entity(
            IMAGES.SLIDE_RULE_DISC.AOB,
            name = AOB,
            context = self.context,
            isFixed = True
        )
        self._DS   = Entity(
            IMAGES.SLIDE_RULE_DISC.DS,
            name = DS,
            context = self.context
        )
        self._TM   = Entity(
            IMAGES.SLIDE_RULE_DISC.TM,
            name = TM,
            context = self.context
        )

        for ent in [
            self._AOB,
            self._DS,
            self._TM
        ]:
            self.add_widget(ent)

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

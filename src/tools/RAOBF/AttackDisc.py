from src.tools.RAOBF.Parts.Entity import Entity
from src.tools.RAOBF.Parts.PartModel import PartModel
from src.constants.RaobfNames import RB, CR, TD, BALA, ACP
from src.constants.Images import IMAGES
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus


class AttackDisc(PartModel):

    def __init__(self, context):
        super().__init__()
        self.context = context

        self._RB   = Entity(
            IMAGES.ATTACK_DISC.RB,
            name = RB,
            context = self.context,
            isFixed = True
        )
        self._CR   = Entity(
            IMAGES.ATTACK_DISC.CR,
            name = CR,
            context = self.context
        )
        self._TD   = Entity(
            IMAGES.ATTACK_DISC.TD,
            name = TD,
            context = self.context
        )
        self._BALA = Entity(
            IMAGES.ATTACK_DISC.BALA,
            name = BALA,
            context = self.context
        )
        self._ACP  = Entity(
            IMAGES.ATTACK_DISC.ACP,
            name = ACP,
            context = self.context
        )

        for ent in [
            self._RB,
            self._CR,
            self._TD,
            self._BALA,
            self._ACP
        ]:
            self.add_widget(ent)

        self.__target = self._CR
        EventBus.on(EVENTS.CHANGE_FOCUS, self.__focus)


    def __focus(self, button):
        self.__target = list(filter(lambda item: item.name in button.attachment, self.children))

    def rotate(self, value):
        for target in self.__target:
            target.rotateBy(value)

    def updateAngle(self):
        for target in self.__target:
            target.updateAngle()

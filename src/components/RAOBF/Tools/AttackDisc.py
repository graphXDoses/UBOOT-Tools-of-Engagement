########################################################
# AttackDisc.py
# Xristos Dosis
# August 6, 2022
#
# Extends the Tool class. Instantiates all relevant parts
# and appends them to the layout. Manipulates children
# parts with own callback functions for focus and
# rotation difference.
########################################################

from src.components.RAOBF.Base.Part import Part
from src.components.RAOBF.Base.Tool import Tool
from src.constants.RaobfNames import RB, CR, TG, BALA, ACP
from src.constants.Images import IMAGES
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus


class AttackDisc(Tool):

    def __init__(self, context):
        super().__init__(context)

        self._RB   = Part(
            IMAGES.ATTACK_DISC.RB,
            name = RB,
            context = self.context,
            isFixed = True
        )
        self._CR   = Part(
            IMAGES.ATTACK_DISC.CR,
            name = CR,
            context = self.context
        )
        self._TG   = Part(
            IMAGES.ATTACK_DISC.TG,
            name = TG,
            context = self.context
        )
        self._BALA = Part(
            IMAGES.ATTACK_DISC.BALA,
            name = BALA,
            context = self.context
        )
        self._ACP  = Part(
            IMAGES.ATTACK_DISC.ACP,
            name = ACP,
            context = self.context
        )

        for ent in [
            self._RB,
            self._CR,
            self._TG,
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

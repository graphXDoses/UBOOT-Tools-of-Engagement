from kivy.vector import Vector
from kivy.uix.boxlayout import BoxLayout
from src.constants.RaobfNames import *
from src.constants.UI import not_assigned, default_context, CONTEXT_POOL
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus
from src.components.RAOBF.Tools.AttackDisc import AttackDisc
from src.components.RAOBF.Tools.SlideRuleDisc import SlideRuleDisc

class ToolsAreaWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(ToolsAreaWidget, self).__init__(orientation="vertical")
        # self.hasSnapOn      = None
        self.cardinalVector = Vector((0, 1))
        self.attackDisc     = AttackDisc(CONTEXT_POOL.ATTACK_DISC)
        self.slideRuleDisc  = SlideRuleDisc(CONTEXT_POOL.SLIDE_RULE_DISC)
        self.activeSide     = None
        self.rootVector     = self.attackDisc.center

        EventBus.on(EVENTS.CHANGE_CONTEXT, self.__changeContext)

    def __changeContext(self, context):
        if context == CONTEXT_POOL.ATTACK_DISC:
            self.clear_widgets()
            self.add_widget(self.attackDisc)
            self.hasSnapOn  = True
            self.activeSide = self.attackDisc

        elif context == CONTEXT_POOL.SLIDE_RULE_DISC:
            self.clear_widgets()
            self.add_widget(self.slideRuleDisc)
            self.hasSnapOn  = False
            self.activeSide = self.slideRuleDisc

    def on_touch_down(self, touch):
        self.cardinalVector = Vector(touch.x, touch.y) - self.rootVector

    def on_touch_move(self, touch):
        v = Vector(touch.x, touch.y) - self.rootVector
        angle = -self.cardinalVector.angle(v)
        if self.hasSnapOn:
            self.activeSide.rotate(round(angle))
        else:
            self.activeSide.rotate(angle)

    def on_touch_up(self, touch):
        self.activeSide.updateAngle()

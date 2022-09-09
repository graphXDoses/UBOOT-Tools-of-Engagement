########################################################
# ToolsAreaWidget.py
# Xristos Dosis
# August 6, 2022
#
# UI layout for tools. Instanciates both AttackDisc and
# SlideRuleDisc with the corresponding context. Also
# handles the recieved touch input and communicates
# the rotation difference with respect to a cardinal up
# vector, to active tool.
########################################################

from kivy.vector import Vector
from kivy.uix.boxlayout import BoxLayout
from src.constants.UI import not_assigned, default_context, CONTEXT_POOL
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus
from src.components.RAOBF.Tools.AttackDisc import AttackDisc
from src.components.RAOBF.Tools.SlideRuleDisc import SlideRuleDisc

class ToolsAreaWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(ToolsAreaWidget, self).__init__(orientation="vertical")
        self.cardinalVector = Vector((0, 1))
        self.attackDisc     = AttackDisc(CONTEXT_POOL.ATTACK_DISC)
        self.slideRuleDisc  = SlideRuleDisc(CONTEXT_POOL.SLIDE_RULE_DISC)
        self.activeSide     = None
        self.rootVector     = self.attackDisc.center
        self.regTouch       = None

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
        if self.regTouch is None:
            self.cardinalVector = Vector(touch.x, touch.y) - self.rootVector
            self.regTouch = touch

    def on_touch_move(self, touch):
        if not self.regTouch is None:
            v = Vector(self.regTouch.x, self.regTouch.y) - self.rootVector
            angle = -self.cardinalVector.angle(v)
            if self.hasSnapOn:
                self.activeSide.rotate(round(angle))
            else:
                self.activeSide.rotate(angle)

    def on_touch_up(self, touch):
        self.regTouch = None
        self.activeSide.updateAngle()

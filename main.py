from src.lib.AppConfig import AppConfig
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import mainthread
from kivy.uix.boxlayout import BoxLayout
from kivy.vector import Vector
from src.tools.RAOBF.AttackDisc import AttackDisc
from src.tools.RAOBF.SlideRuleDisc import SlideRuleDisc
from src.tools.Layouts.ToolbarLayout import ToolbarLayout
from src.tools.InfoBars.InfoButtons import InfoButtons
from src.tools.InfoBars.InfoContext import InfoContext
from src.constants.RaobfNames import *
from src.constants.UI import not_assigned, default_context, CONTEXT_POOL
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus
from src.lib.AppConfig import AppConfig

class MainWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(orientation="vertical")
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

class AttackDiscApplication(App):

    def build(self):
        self.root = BoxLayout(orientation="vertical")

        controlsArea  = ToolbarLayout(hostFor="controls")
        helpContextConfigArea  = ToolbarLayout(hostFor="help-context-config")
        infoContext   = InfoContext()
        mainWidget    = MainWidget()
        infoButtons   = InfoButtons()

        EventBus.trigger(EVENTS.CHANGE_CONTEXT, default_context)
        helpContextConfigArea.children[0].children[0].flip()

        # activeButton = AppConfig.getInitActiveButton()
        # if activeButton == not_assigned:
        #     controlsArea.children[0].children[-1].setFocus(controlsArea.children[0].children[-1])
        # else:
        #     from tools.Buttons.FocusButton import FocusButton
        #     from tools.Buttons.LinkFocusButton import LinkFocusButton
        #     target = next(filter(lambda i: isinstance(i, (FocusButton, LinkFocusButton)) and i.attachment[0] == activeButton, controlsArea.children[0].children))
        #
        #     target.setFocus(target)
        #     del FocusButton, LinkFocusButton

        self.root.add_widget(infoContext)
        self.root.add_widget(helpContextConfigArea)
        self.root.add_widget(mainWidget, canvas="before")
        self.root.add_widget(controlsArea)
        self.root.add_widget(infoButtons)

        return self.root

if __name__ == '__main__':
    AttackDiscApplication().run()

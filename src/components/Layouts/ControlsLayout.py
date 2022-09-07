########################################################
# ControlsLayout.py
# Xristos Dosis
# August 6, 2022
#
# Extends the Kivy BoxLayout class. Ensures the proper
# spacing between children buttons.
########################################################

from kivy.clock import mainthread
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line
from kivy.vector import Vector
from src.constants.UI import CONTEXT_POOL
from src.constants.EventNames import EVENTS
from src.constants.Colors import BUTTON_ILLUMINATION_BACKGROUND_COLOR
from src.lib.EventBus import EventBus
from src.components.Buttons.ButtonFactory import ButtonFactory


class ControlsLayout(BoxLayout):

    def __init__(self, button_size=100): #85
        super(ControlsLayout, self).__init__(orientation='horizontal', size_hint=(None, None), height=button_size, pos_hint={"center_x":0.5, "center_y":0.5})
        padding_value = 30

        self.button_size = button_size
        self.hasLink     = False
        self.restoreLink = False

        self.spacing = padding_value
        self.padding = [0, 0, 0, padding_value]
        self.height += sum((self.padding[1], self.padding[3]))

        EventBus.on(EVENTS.CHANGE_CONTEXT, self.__changeContext)
        EventBus.on(EVENTS.ENTER_LINK, self.__addLink)
        EventBus.on(EVENTS.BREAK_LINK, self.__removeLink)

    def __changeContext(self, context):
        self.clear_widgets()
        for button in ButtonFactory().controls(context):
            self.add_widget(button)

        if self.hasLink:
            self.restoreLink = True
            EventBus.trigger(EVENTS.BREAK_LINK)
        else:
            if self.restoreLink and context == CONTEXT_POOL.ATTACK_DISC:
                EventBus.trigger(EVENTS.ENTER_LINK)

        self.width = self.spacing*(len(self.children) - 1) + len(self.children)*self.button_size

    @mainthread
    def __addLink(self):
        self.hasLink = True
        self.restoreLink = False
        with self.canvas.before:
            Color(*BUTTON_ILLUMINATION_BACKGROUND_COLOR)
            pts = list()
            for btn in [self.children[-2], self.children[-1]]:
                p = Vector(*btn.pos) + Vector(*btn.size)/2
                pts.append(p.x)
                pts.append(p.y)

            Line(points=pts, width=2)

    def __removeLink(self):
        self.hasLink = False
        self.canvas.before.clear()

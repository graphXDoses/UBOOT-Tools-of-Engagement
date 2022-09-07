########################################################
# InfoLayout.py
# Xristos Dosis
# August 6, 2022
#
# Extends the Kivy BoxLayout class.
########################################################

from kivy.clock import mainthread
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from src.constants.Colors import TOOLBAR_BACKGROUND
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus


class InfoLayout(BoxLayout):

    def __init__(self, triggerEvent, default_height=75):
        super(InfoLayout, self).__init__(orientation='horizontal', size_hint=(1, None), height=default_height)

        self.InfoLabel = Label()
        self.add_widget(self.InfoLabel)
        EventBus.on(triggerEvent, self.updateLabelCallback)
        self.nextDraw()

    @mainthread
    def nextDraw(self):
        with self.canvas.before:
            Color(*TOOLBAR_BACKGROUND)
            self.bg = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.redraw, size=self.redraw)

    def redraw(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def updateLabelCallback(self, object):
        return

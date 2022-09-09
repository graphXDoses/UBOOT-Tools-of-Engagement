########################################################
# ToolbarLayout.py
# Xristos Dosis
# August 6, 2022
#
# Generic toolbar layout, extending Kivy BoxLayout class.
########################################################

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from src.constants.Colors import TOOLBAR_BACKGROUND
from src.components.Layouts.ControlsLayout import ControlsLayout
from src.components.Layouts.HelpAndContextLayout import HelpAndContextLayout


class ToolbarLayout(BoxLayout):

    def __init__(self, hostFor="mv-controls", size=75):
        super(ToolbarLayout, self).__init__(orientation='vertical', size_hint=(1, None), pos_hint={"center_x":0.5})

        if hostFor == "mv-controls":
            self.add_widget(ControlsLayout())
        elif hostFor == "mv-help-context-config":
            self.add_widget(HelpAndContextLayout())
        self.height = self.children[0].height

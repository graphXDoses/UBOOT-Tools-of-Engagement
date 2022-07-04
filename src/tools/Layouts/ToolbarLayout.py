from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from src.constants.RaobfNames import CR, TD, BALA, ACP
from src.constants.Colors import TOOLBAR_BACKGROUND
from src.tools.Layouts.ControlsLayout import ControlsLayout
from src.tools.Layouts.HelpAndContextLayout import HelpAndContextLayout


class ToolbarLayout(BoxLayout):

    def __init__(self, hostFor="controls", size=75):
        super(ToolbarLayout, self).__init__(orientation='vertical', size_hint=(1, None), pos_hint={"center_x":0.5})

        if hostFor == "controls":
            self.add_widget(ControlsLayout())
        elif hostFor == "help-context-config":
            self.add_widget(HelpAndContextLayout())
            # pass
        self.height = self.children[0].height
        # with self.canvas.before:
        #     Color(*TOOLBAR_BACKGROUND)
        #     self.bg = Rectangle(pos=self.pos, size=self.size)
    #     self.bind(pos=self.redraw, size=self.redraw)
    #
    # def redraw(self, *args):
    #     self.bg.pos = self.pos
    #     self.bg.size = self.size

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line
from kivy.vector import Vector
from src.constants.EventNames import EVENTS
from src.constants.Colors import BUTTON_ILLUMINATION_BACKGROUND_COLOR
from src.lib.EventBus import EventBus
from src.components.Buttons.ButtonFactory import ButtonFactory


class HelpAndContextLayout(BoxLayout):

    def __init__(self, button_size=100): #85
        super(HelpAndContextLayout, self).__init__(orientation='horizontal', size_hint=(1, None), height=button_size, pos_hint={"center_x":0.5, "center_y":0.5})

        padding_value = 30

        self.button_size = button_size

        for button in ButtonFactory().helpContext():
            self.add_widget(button)

        self.spacing = padding_value
        self.padding = [padding_value, padding_value, padding_value, 0]
        self.height += sum((self.padding[1], self.padding[3]))
        self.bind(width=self.updateValues)

    def updateValues(self, *args):
        self.spacing = self.width - ((self.button_size * len(self.children)) + sum((self.padding[0], self.padding[2])))

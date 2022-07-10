from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

class SettingsView(Screen):

    def __init__(self, name=None):
        if not name is None:
            super().__init__(name=name)
        else:
            super().__init__()

        rootWidget = BoxLayout(orientation="vertical")

        self.add_widget(rootWidget)

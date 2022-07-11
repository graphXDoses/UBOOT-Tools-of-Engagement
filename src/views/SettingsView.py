from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from src.constants.UI import VIEWS_POOL
from src.components.Buttons.ViewSwitchButton import ViewSwitchButton

class SettingsView(Screen):

    def __init__(self, name=None):
        if not name is None:
            super().__init__(name=name)
        else:
            super().__init__()

        rootWidget = BoxLayout(orientation="vertical")
        rootWidget.add_widget(ViewSwitchButton(None, text="Get Back", portalTo=VIEWS_POOL.MAINVIEW))

        self.add_widget(rootWidget)

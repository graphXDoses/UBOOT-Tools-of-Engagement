from kivy.uix.screenmanager import ScreenManager
from src.constants.UI import VIEWS_POOL, default_view
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus
from src.lib.Utils import Cycler
from src.views.MainView import MainView
from src.views.SettingsView import SettingsView

class ViewManager(ScreenManager):

    def __init__(self):
        super().__init__()

        self.getNextDir = Cycler(["down", "up"])
        self.transition.direction = self.getNextDir()
        EventBus.on(EVENTS.CHANGE_VIEW, self.__changeView)

        self.add_widget(MainView(name=VIEWS_POOL.MAINVIEW))
        self.add_widget(SettingsView(name=VIEWS_POOL.SETTINGSVIEW))

        EventBus.trigger(EVENTS.CHANGE_VIEW, default_view)

    def __changeView(self, view):
        if self.has_screen(view) and self.current != view:
            self.current = view
            self.transition.direction = self.getNextDir()

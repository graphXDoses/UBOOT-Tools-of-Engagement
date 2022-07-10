from src.lib.AppConfig import AppConfig
from kivy.app import App
from kivy.core.window import Window
from src.views.ViewManager import ViewManager

class ToolsOfEngagement(App):

    def build(self):
        self.viewManager = ViewManager()
        return self.viewManager

if __name__ == '__main__':
    ToolsOfEngagement().run()

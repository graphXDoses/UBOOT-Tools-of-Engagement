########################################################
# main.py
# Xristos Dosis
# August 6, 2022
#
# Main entry point of application.
########################################################

### FPS DEBUG ###
# from kivy.config import Config
# Config.set('modules', 'monitor', '')

from kivy.app import App
from kivy.core.window import Window
from src.views.ViewManager import ViewManager

class ToolsOfEngagement(App):

    def build(self):
        self.ViewManager = ViewManager()
        return self.ViewManager

if __name__ == '__main__':
    ToolsOfEngagement().run()

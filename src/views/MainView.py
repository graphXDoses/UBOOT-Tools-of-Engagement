from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from src.components.Layouts.ToolbarLayout import ToolbarLayout
from src.components.InfoBars.InfoButtons import InfoButtons
from src.components.InfoBars.InfoContext import InfoContext
from src.components.RAOBF.ToolsAreaWidget import ToolsAreaWidget
from src.constants.RaobfNames import *
from src.constants.UI import not_assigned, default_context, CONTEXT_POOL
from src.constants.EventNames import EVENTS
from src.lib.EventBus import EventBus

class MainView(Screen):

    def __init__(self, name=None):
        if not name is None:
            super().__init__(name=name)
        else:
            super().__init__()
        rootWidget = BoxLayout(orientation="vertical")

        controlsArea  = ToolbarLayout(hostFor="mv-controls")
        helpContextConfigArea  = ToolbarLayout(hostFor="mv-help-context-config")
        infoContext   = InfoContext()
        toolsWidget   = ToolsAreaWidget()
        infoButtons   = InfoButtons()

        EventBus.trigger(EVENTS.CHANGE_CONTEXT, default_context)
        helpContextConfigArea.children[0].children[0].flip()

        rootWidget.add_widget(infoContext)
        rootWidget.add_widget(helpContextConfigArea)
        rootWidget.add_widget(toolsWidget, canvas="before")
        rootWidget.add_widget(controlsArea)
        rootWidget.add_widget(infoButtons)

        self.add_widget(rootWidget)

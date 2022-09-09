########################################################
# AppConfig.py
# Xristos Dosis
# August 6, 2022
#
# Application configuration class. Reads and writes
# from/to app.ini and stores data related to the
# application.
########################################################

from configparser import ConfigParser
from src.constants.EventNames import EVENTS
from src.constants.UI import active_button, not_assigned, default_context, CONTEXT_POOL
from src.lib.EventBus import EventBus

class AppConfig(ConfigParser):

    def __init__(self):
        super().__init__()
        self.read('app.ini')
        self.context = "_".join(map(lambda i: i.upper(), default_context.split()))
        EventBus.on(EVENTS.CHANGE_VALUE, self.__valueChangeCallback)
        EventBus.on(EVENTS.CHANGE_FOCUS, self.__focusChangeCallback)
        EventBus.on(EVENTS.CHANGE_CONTEXT, self.__changeContext)

    def getInitAngle(self, ref):
        return self.getfloat(self.context, ref, fallback=0.0)

    def getInitActiveButton(self):
        return self.get(self.context, active_button, fallback=not_assigned)

    def reset(self, ref):
        self.__valueChangeCallback(ref, 0.0)

    def __changeContext(self, context):
        self.context = "_".join(map(lambda i: i.upper(), context.split()))

    def __focusChangeCallback(self, button):
        self.__valueChangeCallback(active_button, button.attachment[0])

    def __valueChangeCallback(self, ref, value):
        self.set(self.context, ref, str(value))
        with open('app.ini', 'w') as configfile:
            self.write(configfile)



_ = AppConfig()
del AppConfig
AppConfig = _

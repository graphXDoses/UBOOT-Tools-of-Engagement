from src.lib.EventModel import EventModel

class EventBus:

    def __init__(self)->None:
        self._events = dict()

    def has(self, eventName:str)->bool:
        return eventName in self._events

    def on(self, eventName:str, callback)->None:
        if self.has(eventName):
            self._events[eventName].addObserver(callback)
            return

        self._events[eventName] = EventModel(eventName)
        self.on(eventName, callback)

    def off(self, eventName:str, callback)->None:
        if not self.has(eventName): return

        self._removeObserver(eventName, callback)

        if len(self._events) < 1: self._removeEventKey(eventName)

    def trigger(self, eventName:str, *args)->None:
        if not self.has(eventName): return

        observers = self._events[eventName]._observers

        for observer in observers:
            observer(*args)

    def _removeObserver(self, eventName:str, callback)->None:
        self._events[eventName].removeObserver(callback)

    def _removeEventKey(self, eventName:str)->None:
        del self._events[eventName]


_ = EventBus()
del EventBus
EventBus = _

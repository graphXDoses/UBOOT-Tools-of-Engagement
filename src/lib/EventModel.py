class EventModel:

    def __init__(self, name:str='')->None:
        self._name = name
        self._observers = []

    def hasObserver(self, observer:str)->bool:
        return observer in self._observers

    def addObserver(self, observer:str)->None:
        if self.hasObserver(observer):
            return
        self._observers.append(observer)

    def removeObserver(self, observer:str)->None:
        if not self.hasObserver(observer):
            return
        self._observers.pop(observer)

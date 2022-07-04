class JSDictionary:
    """docstring for JSDictionary."""

    def __init__(self, target:dict):
        for k, v in zip(target.keys(), target.values()):
            if isinstance(v, dict):
                if not k in self.__dict__:
                    setattr(self, k, JSDictionary(v))
            else:
                if not k in self.__dict__:
                    setattr(self, k, v)

    def __iter__(self):
        for key in self.__dict__:
            yield getattr(self, key)

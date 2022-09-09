########################################################
# jsDictionary.py
# Xristos Dosis
# August 6, 2022
#
# Javasript style dictionary.
########################################################

class JSDictionary:

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

    def findByVal(self, value):
        if not isinstance(value, str): raise ValueError('String expected.')
        try: key, *_ = filter( lambda v: v[1] == value, self.__dict__.items() )
        except ValueError: return None
        return key[0]

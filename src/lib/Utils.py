########################################################
# Utils.py
# Xristos Dosis
# August 6, 2022
#
# All application utillities.
########################################################

def hex2RGB(string)->tuple:
    n = int(string, base=16)
    return (
        (n >> 16)/255.,
        ((n >> 8) & 255)/255.,
        (n & 255) / 255.
    )

def rgb2hex(col)->int:
    r, g, b = col
    r, g, b = int(r*255.) << 16, (int(g*255.) << 8), int(b*255.)
    return hex(sum((r, g, b)))

########################################################
# Cycler class:
# Creates a generator that cycles through a collection
# of iterables indefinatelly and returns the next
# iterable upon calling.
########################################################
class Cycler:

    def __init__(self, options, start=0):
        self.__idx = start
        self.__options = options
        self.__iterable = self.__gen()

    @property
    def getIDX(self):
        return self.__idx

    def __gen(self):
        while 1:
            self.__idx += 1
            yield self.__options[ self.__idx % len(self.__options) ]

    def __call__(self):
        return next(self.__iterable)


class Label:
    def __init__(self, extended, compact):
        self._extended = extended
        self._compact = compact

    def __repr__(self):
        return self._extended

    def __str__(self):
        return self._compact

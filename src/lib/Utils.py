########################################################
# Utils.py
# Xristos Dosis
# August 6, 2022
#
# All application utillities.
########################################################

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

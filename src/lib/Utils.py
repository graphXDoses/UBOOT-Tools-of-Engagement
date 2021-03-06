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

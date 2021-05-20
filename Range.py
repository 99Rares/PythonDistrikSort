# noinspection SpellCheckingInspection


class range:
    """
     Klasse fur den Objekt Range.
     Attributes:
        start (float), stop (float)
    """

    def __init__(self, start, stop):
        self.__start = float(start)
        self.__stop = float(stop)

    @property
    def start(self):
        return self.__start

    @property
    def stop(self):
        return self.__stop

    @start.setter
    def start(self, new_start):
        self.__start = new_start

    @stop.setter
    def stop(self, new_stop):
        self.__stop = new_stop

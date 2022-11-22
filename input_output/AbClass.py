import abc


class MyAbstract(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def input(self):
        pass

    @abc.abstractmethod
    def output(self):
        pass

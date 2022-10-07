from abc import ABC, abstractmethod

from pubsub import pub


class EventListener(ABC):
    @abstractmethod
    def listen(self):
        pass


class AlgorithmFinishedEvent:
    EVENT_NAME = "algorithm-finished"

    def __init__(self, value1, value2):
        self.__value1 = value1
        self.__value2 = value2

    @property
    def value1(self):
        return self.__value1

    @property
    def value2(self):
        return self.__value2

    def publish(self):
        pub.sendMessage(self.EVENT_NAME, event=self)

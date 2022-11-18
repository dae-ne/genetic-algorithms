from abc import ABC, abstractmethod


class EventListener(ABC):
    @abstractmethod
    def listen(self):
        pass


class AlgorithmFinishedEvent:
    def __init__(self, generations, execution_time, time_finished, options):
        self.__generations = generations
        self.__execution_time = execution_time
        self.__time_finished = time_finished
        self.__options = options

    @property
    def generations(self):
        return self.__generations

    @property
    def execution_time(self):
        return self.__execution_time

    @property
    def time_finished(self):
        return self.__time_finished

    @property
    def options(self):
        return self.__options

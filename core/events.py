from abc import ABC, abstractmethod


class EventListener(ABC):
    @abstractmethod
    def listen(self):
        pass


class AlgorithmFinishedEvent:
    def __init__(self, generations, execution_time, options):
        self.__generations = generations
        self.__execution_time = execution_time
        self.__options = options

    @property
    def generations(self):
        return self.__generations

    @property
    def execution_time(self):
        return self.__execution_time

    @property
    def options(self):
        return self.__options


class DataSavedEvent:
    def __init__(self, directory, file_name):
        self.__directory = directory
        self.__file_name = file_name

    @property
    def directory(self):
        return self.__directory

    @property
    def file_name(self):
        return self.__file_name

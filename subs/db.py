from pubsub import pub

from core.events import EventListener, AlgorithmFinishedEvent


class DbEventListener(EventListener):
    def listen(self):
        pub.subscribe(self.__handle, AlgorithmFinishedEvent.__name__)

    @staticmethod
    def __handle(event: AlgorithmFinishedEvent):
        print("db listener:", event.value1, event.value2)

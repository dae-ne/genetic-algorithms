from pubsub import pub

from core.events import EventListener, AlgorithmFinishedEvent


class PlotEventListener(EventListener):
    def listen(self):
        pub.subscribe(self.__handle, AlgorithmFinishedEvent.__name__)

    @staticmethod
    def __handle(event: AlgorithmFinishedEvent):
        print("plot listener:", event.value1, event.value2)

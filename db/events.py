import time

from pubsub import pub

from core.events import AlgorithmFinishedEvent, EventListener


class AlgorithmFinishedDbEventListener(EventListener):
    def listen(self):
        pub.subscribe(self.__handler, AlgorithmFinishedEvent.EVENT_NAME)

    @staticmethod
    def __handler(event: AlgorithmFinishedEvent):
        print("wait...")
        time.sleep(1)
        print("db listener data:", event.value1, event.value2)

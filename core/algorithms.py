import time
from threading import Thread

from pubsub import pub

from core.events import AlgorithmFinishedEvent


class AsyncGeneticAlgorithm(Thread):
    def __init__(self, population_size, selection_method):
        super().__init__()

        self.population_size = population_size
        self.selection_method = selection_method

    def run(self):
        print("wait...")
        time.sleep(1)
        print("Data:", self.population_size, self.selection_method)

        event = AlgorithmFinishedEvent("value1", "value2")
        pub.sendMessage(AlgorithmFinishedEvent.__name__, event=event)

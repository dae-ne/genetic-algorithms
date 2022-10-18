import time
from threading import Thread

from pubsub import pub

from core.events import AlgorithmFinishedEvent
from core.fitness_function import TestFunction
from core.models import AlgorithmOptions
from core.population import Generator
from core.selection import SelectionMethodFactory


class AsyncGeneticAlgorithm(Thread):
    def __init__(self, options: AlgorithmOptions):
        super().__init__()
        self.options = options

    def run(self):
        selection_method = SelectionMethodFactory.create(self.options)

        print("wait...")
        time.sleep(1)
        print(self.options.__dict__)

        population = Generator.generate_random_population(self.options.population_size,
                                                          self.options.range_from,
                                                          self.options.range_to,
                                                          self.options.precision,
                                                          TestFunction())
        print(population)
        print("Best candidate: {}".format(population.get_best_candidate(self.options.maximization)))
        print("Average score: {}".format(population.get_average_score()))
        print("Standard deviation: {}".format(population.get_standard_deviation()))

        event = AlgorithmFinishedEvent("value1", "value2")
        pub.sendMessage(AlgorithmFinishedEvent.__name__, event=event)

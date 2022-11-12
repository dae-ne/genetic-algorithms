import random
import time
from threading import Thread

from pubsub import pub

from core.crossover import CrossoverMethodFactory
from core.events import AlgorithmFinishedEvent
from core.fitness_function import TestFunction
from core.models import AlgorithmOptions
from core.mutation import MutationMethodFactory
from core.population import Generator, Population
from core.selection import SelectionMethodFactory


class AsyncGeneticAlgorithm(Thread):
    def __init__(self, options: AlgorithmOptions):
        super().__init__()
        self.options = options

    def run(self):
        print("wait...")
        time.sleep(1)
        print(self.options.__dict__)

        population = Generator.generate_random_population(self.options.population_size,
                                                          self.options.range_from,
                                                          self.options.range_to,
                                                          self.options.precision,
                                                          TestFunction())
        self.print_stats(population, with_candidates=False)

        for epoch in range(self.options.epochs_amount):
            population = self.create_next_generation(population)

        print('after')
        self.print_stats(population, with_candidates=False)

        event = AlgorithmFinishedEvent("value1", "value2")
        pub.sendMessage(AlgorithmFinishedEvent.__name__, event=event)

    def create_next_generation(self, population):
        selection_method = SelectionMethodFactory.create(self.options)
        crossover_method = CrossoverMethodFactory.create(self.options)
        mutation_method = MutationMethodFactory.create(self.options)
        # inversion_method

        new_population = Population()
        elite = population.get_n_best_candidates(self.options.elite_strategy_amount, self.options.maximization)
        for candidate in elite:
            new_population.add_candidate(candidate)

        selected_candidates = selection_method.calculate(population)
        if len(selected_candidates) < 2:
            raise Exception("Less than 2 candidates were selected")

        while new_population.size < population.size:
            parents = random.sample(selected_candidates, 2)
            children = crossover_method.cross(*parents)
            for child in children:
                if new_population.size >= population.size:
                    break

                mutation_method.mutate(child)
                # inversion
                new_population.add_candidate(child)

        return new_population

    def print_stats(self, population, with_candidates=False):
        if with_candidates:
            print("All candidates:")
            print(population)
        print("Best candidate: {}".format(population.get_n_best_candidates(1, self.options.maximization)[0]))
        print("Average score: {}".format(population.get_average_score()))
        print("Standard deviation: {}".format(population.get_standard_deviation()))

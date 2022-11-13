import random
import time
from threading import Thread

from pubsub import pub

from core.crossover import CrossoverMethodFactory
from core.events import AlgorithmFinishedEvent
from core.fitness_function import TestFunction
from core.inversion import InversionMethod
from core.models import AlgorithmOptions
from core.mutation import MutationMethodFactory
from core.population import Generator, Population
from core.selection import SelectionMethodFactory


class AsyncGeneticAlgorithm(Thread):
    def __init__(self, options: AlgorithmOptions):
        super().__init__()
        self.options = options

    def run(self):
        selection_method = SelectionMethodFactory.create(self.options)
        crossover_method = CrossoverMethodFactory.create(self.options)
        mutation_method = MutationMethodFactory.create(self.options)
        inversion_method = InversionMethod(self.options.inversion_probability)

        execution_time = time.time()
        generations = [Generator.generate_random_population(self.options.population_size,
                                                            self.options.range_from,
                                                            self.options.range_to,
                                                            self.options.precision,
                                                            TestFunction())]
        self.print_stats(generations[0], with_candidates=False)

        for epoch in range(self.options.epochs_amount):
            generations.append(self.create_next_generation(generations[-1], selection_method, crossover_method,
                                                           mutation_method, inversion_method))

        print("after")
        self.print_stats(generations[-1], with_candidates=False)
        execution_time = time.time() - execution_time

        event = AlgorithmFinishedEvent(generations, execution_time, self.options)
        pub.sendMessage(AlgorithmFinishedEvent.__name__, event=event)

    def create_next_generation(self, population, selection, crossover, mutation, inversion):
        new_population = Population()
        elite = population.get_n_best_candidates(self.options.elite_strategy_amount, self.options.maximization)
        for candidate in elite:
            new_population.add_candidate(candidate)

        selected_candidates = selection.calculate(population)
        if len(selected_candidates) < 2:
            raise Exception("Less than 2 candidates were selected")

        while new_population.size < population.size:
            parents = random.sample(selected_candidates, 2)
            children = crossover.cross(*parents)
            for child in children:
                if new_population.size >= population.size:
                    break

                mutation.mutate(child)
                inversion.inverse(child)
                new_population.add_candidate(child)

        return new_population

    def print_stats(self, population, with_candidates=False):
        if with_candidates:
            print("All candidates:")
            print(population)
        print("Best candidate: {}".format(population.get_best_candidate(self.options.maximization)))
        print("Average score: {}".format(population.get_average_score()))
        print("Standard deviation: {}".format(population.get_standard_deviation()))

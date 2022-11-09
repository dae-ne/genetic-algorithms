import copy
import random
from abc import ABC, abstractmethod

from core.models import AlgorithmOptions, CrossoverMethod
from core.population import Candidate


class CrossoverMethodAlgorithm(ABC):
    def __init__(self, probability):
        self.probability = probability / 100

    def shouldCross(self):
        return random.random() < self.probability

    @abstractmethod
    def cross(self, parent1, parent2):
        pass


class CrossoverMethodFactory:
    @staticmethod
    def create(options: AlgorithmOptions) -> CrossoverMethodAlgorithm:
        match options.crossover_method:
            case CrossoverMethod.ONE_POINT:
                return CrossoverOnePointMethod(options.crossover_probability)
            case CrossoverMethod.TWO_POINTS:
                return CrossoverTwoPointsMethod(options.crossover_probability)
            case CrossoverMethod.THREE_POINTS:
                return CrossoverThreePointsMethod(options.crossover_probability)
            case CrossoverMethod.HOMO:
                return CrossoverHomoMethod(options.crossover_probability)
            case _:
                raise Exception("")


class CrossoverOnePointMethod(CrossoverMethodAlgorithm):
    def cross(self, parent1: Candidate, parent2: Candidate):
        if not self.shouldCross():
            return []

        child1, child2 = copy.deepcopy(parent1), copy.deepcopy(parent2)
        for chromosome1, chromosome2 in zip(child1.chromosomes, child2.chromosomes):
            gen_list1, gen_list2 = chromosome1.gen_list, chromosome2.gen_list
            if len(gen_list1) != len(gen_list2):
                raise Exception("Chromosomes should have the same number of gens.")

            crossing_point = random.randint(1, len(gen_list1)-1)
            gen_list1, gen_list2 = gen_list1[:crossing_point] + gen_list2[crossing_point:], gen_list2[:crossing_point] + gen_list1[crossing_point:]
            chromosome1.gen_list = gen_list1
            chromosome2.gen_list = gen_list2
        return child1, child2


class CrossoverTwoPointsMethod(CrossoverMethodAlgorithm):
    def cross(self, parent1, parent2):
        pass


class CrossoverThreePointsMethod(CrossoverMethodAlgorithm):
    def cross(self, parent1, parent2):
        pass


class CrossoverHomoMethod(CrossoverMethodAlgorithm):
    def cross(self, parent1, parent2):
        pass

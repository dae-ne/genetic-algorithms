import random
from abc import ABC, abstractmethod

from core.models import AlgorithmOptions, MutationMethod
from core.population import Candidate


class MutationMethodAlgorithm(ABC):
    def __init__(self, probability):
        self.probability = probability / 100

    def shouldMutate(self):
        return random.random() < self.probability

    @abstractmethod
    def mutate(self, candidate):
        pass


class MutationMethodFactory:
    @staticmethod
    def create(options: AlgorithmOptions) -> MutationMethodAlgorithm:
        match options.mutation_method:
            case MutationMethod.ONE_POINT:
                return MutationOnePointMethod(options.mutation_probability)
            case MutationMethod.TWO_POINTS:
                return MutationTwoPointsMethod(options.mutation_probability)
            case _:
                raise Exception("")


class MutationOnePointMethod(MutationMethodAlgorithm):
    def mutate(self, candidate: Candidate):
        if not self.shouldMutate():
            return candidate

        for chromosome in candidate.chromosomes:
            num_of_bit = random.randint(0, len(chromosome.gen_list) - 1)
            chromosome.gen_list[num_of_bit] = 1 - chromosome.gen_list[num_of_bit]

        return candidate


class MutationTwoPointsMethod(MutationMethodAlgorithm):
    def mutate(self, candidate):
        if not self.shouldMutate():
            return candidate

        for chromosome in candidate.chromosomes:
            num_of_bits = [random.randint(0, len(chromosome.gen_list) - 1) for _ in range(2)]
            for num_of_bit in num_of_bits:
                chromosome.gen_list[num_of_bit] = 1 - chromosome.gen_list[num_of_bit]

        return candidate

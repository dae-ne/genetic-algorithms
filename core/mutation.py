from abc import ABC, abstractmethod

from core.models import AlgorithmOptions, MutationMethod


class MutationMethodAlgorithm(ABC):
    def __init__(self, probability):
        self.probability = probability

    @abstractmethod
    def mutate(self, candidate):
        pass


class MutationMethodFactory:
    @staticmethod
    def create(options: AlgorithmOptions) -> MutationMethodAlgorithm:
        match options.crossover_method:
            case MutationMethod.ONE_POINT:
                return MutationOnePointMethod(options.mutation_probability)
            case MutationMethod.TWO_POINTS:
                return MutationTwoPointsMethod(options.mutation_probability)
            case _:
                raise Exception("")


class MutationOnePointMethod(MutationMethodAlgorithm):
    def mutate(self, candidate):
        pass


class MutationTwoPointsMethod(MutationMethodAlgorithm):
    def mutate(self, candidate):
        pass

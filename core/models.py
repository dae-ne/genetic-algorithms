from strenum import StrEnum
from enum import auto


class SelectionMethod(StrEnum):
    BEST = auto()
    TOURNAMENT = auto()
    ROULETTE = auto()


class CrossoverMethod(StrEnum):
    ONE_POINT = auto()
    TWO_POINTS = auto()
    THREE_POINTS = auto()
    HOMO = auto()


class MutationMethod(StrEnum):
    ONE_POINT = auto()
    TWO_POINTS = auto()


class AlgorithmOptions:
    def __init__(self,
                 range_from: int,
                 range_to: int,
                 population_size: int,
                 precision: int,
                 epochs_amount: int,
                 elite_strategy_amount: int,
                 crossover_probability: int,
                 mutation_probability: int,
                 inversion_probability: int,
                 selection_method: SelectionMethod,
                 selection_param: int,
                 crossover_method: CrossoverMethod,
                 mutation_method: MutationMethod,
                 maximization: bool):
        self.range_from = range_from
        self.range_to = range_to
        self.population_size = population_size
        self.precision = precision
        self.epochs_amount = epochs_amount
        self.elite_strategy_amount = elite_strategy_amount
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.inversion_probability = inversion_probability
        self.selection_method = selection_method
        self.selection_param = selection_param
        self.crossover_method = crossover_method
        self.mutation_method = mutation_method
        self.maximization = maximization

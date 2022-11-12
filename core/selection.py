import random
from abc import ABC, abstractmethod

from core.models import AlgorithmOptions, SelectionMethod


class SelectionMethodAlgorithm(ABC):
    def __init__(self, maximization=False):
        self.maximization = maximization

    @abstractmethod
    def calculate(self, population):
        pass


class SelectionMethodFactory:
    @staticmethod
    def create(options: AlgorithmOptions) -> SelectionMethodAlgorithm:
        match options.selection_method:
            case SelectionMethod.BEST:
                return SelectionBestMethod(options.selection_param, options.maximization)
            case SelectionMethod.ROULETTE:
                return SelectionRouletteMethod(options.maximization)
            case SelectionMethod.TOURNAMENT:
                return SelectionTournamentMethod(options.selection_param, options.maximization)
            case _:
                raise Exception("")


class SelectionBestMethod(SelectionMethodAlgorithm):
    def __init__(self, percent=60, maximization=False):
        super().__init__(maximization)
        self.percent = percent

    def calculate(self, population):
        candidates = sorted(population.candidates, key=lambda candidate: candidate.score, reverse=self.maximization)
        return candidates[:int(population.size * self.percent / 100)]


class SelectionRouletteMethod(SelectionMethodAlgorithm):
    def calculate(self, population):
        pass


class SelectionTournamentMethod(SelectionMethodAlgorithm):
    def __init__(self, group_size=3, maximization=False):
        super().__init__(maximization)
        self.group_size = group_size

    def calculate(self, population):
        random.shuffle(population.candidates)
        candidates = []
        for i in range(0, population.size, self.group_size):
            group = population.candidates[i:i+self.group_size]
            candidates.append(self.select_best_from_group(group))

        return candidates

    def select_best_from_group(self, group):
        sorted_group = sorted(group, key=lambda candidate: candidate.score, reverse=self.maximization)
        return sorted_group[0]

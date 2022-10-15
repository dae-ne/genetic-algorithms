from abc import ABC, abstractmethod

from core.models import AlgorithmOptions, SelectionMethod


class SelectionMethodAlgorithm(ABC):
    @abstractmethod
    def calculate(self):
        pass


class SelectionMethodFactory:
    @staticmethod
    def create(options: AlgorithmOptions) -> SelectionMethodAlgorithm:
        match options.selection_method:
            case SelectionMethod.BEST:
                return SelectionBestMethod()
            case SelectionMethod.ROULETTE:
                return SelectionRouletteMethod()
            case SelectionMethod.TOURNAMENT:
                return SelectionTournamentMethod()
            case _:
                raise Exception("")


class SelectionBestMethod(SelectionMethodAlgorithm):
    def calculate(self):
        pass


class SelectionRouletteMethod(SelectionMethodAlgorithm):
    def calculate(self):
        pass


class SelectionTournamentMethod(SelectionMethodAlgorithm):
    def calculate(self):
        pass

from core.algorithms import AsyncGeneticAlgorithm


class FormModel:
    def __init__(self):
        self.__population_size = None
        self.__selection_method = None

    @property
    def population_size(self):
        return self.__population_size

    @population_size.setter
    def population_size(self, value):
        if value:
            self.__population_size = value
        else:
            raise ValueError("Empty population size")

    @property
    def selection_method(self):
        return self.__selection_method

    @selection_method.setter
    def selection_method(self, value):
        self.__selection_method = value
        if value:
            self.__selection_method = value
        else:
            raise ValueError("Empty selection method")

    def run_algorithm(self):
        algorithm_thread = AsyncGeneticAlgorithm(
            self.population_size,
            self.selection_method)
        algorithm_thread.start()

from abc import ABC, abstractmethod


class FitnessFunction(ABC):
    @classmethod
    @property
    @abstractmethod
    def NUM_OF_VARIABLES(cls):
        pass

    @abstractmethod
    def evaluate(self, variables):
        pass


class TestFunction(FitnessFunction):
    # example function, minimum in (0, 0)

    NUM_OF_VARIABLES = 2

    def evaluate(self, variables):
        if len(variables) != TestFunction.NUM_OF_VARIABLES:
            raise Exception("Function takes {} arguments, but {} were given."
                            .format(TestFunction.NUM_OF_VARIABLES, len(variables)))
        x, y = variables

        return x * x + y * y

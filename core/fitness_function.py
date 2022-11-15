from abc import ABC, abstractmethod

import math

from core.models import AlgorithmOptions, FitnessFunction


class BaseFitnessFunction(ABC):
    @classmethod
    @property
    @abstractmethod
    def NUM_OF_VARIABLES(cls):
        pass

    @abstractmethod
    def evaluate(self, variables):
        pass


class FitnessFunctionFactory:
    @staticmethod
    def create(options: AlgorithmOptions) -> BaseFitnessFunction:
        match options.fitness_function:
            case FitnessFunction.BEALE_FUNCTION:
                return BealeFunction()
            case FitnessFunction.EGGHOLDER_FUNCTION:
                return EggholderFunction()
            case FitnessFunction.CROSS_IN_TRAY_FUNCTION:
                return CrossInTrayFunction()
            case FitnessFunction.TEST_FUNCTION:
                return TestFunction()
            case _:
                raise Exception("")


class BealeFunction(BaseFitnessFunction):
    # example function, minimum = 0 in (3, 0.5), range [-4.5, 4.5], maximum in the corners

    NUM_OF_VARIABLES = 2

    def evaluate(self, variables):
        if len(variables) != BealeFunction.NUM_OF_VARIABLES:
            raise Exception("Function takes {} arguments, but {} were given."
                            .format(BealeFunction.NUM_OF_VARIABLES, len(variables)))
        x, y = variables

        return (1.5 - x + x*y)**2 + (2.25 - x + x*y*y)**2 + (2.625 - x + x*y**3)**2


class EggholderFunction(BaseFitnessFunction):
    # example function, minimum = -959.6407 in (512, 404.2319), range [-512, 512], maximum in the corners

    NUM_OF_VARIABLES = 2

    def evaluate(self, variables):
        if len(variables) != EggholderFunction.NUM_OF_VARIABLES:
            raise Exception("Function takes {} arguments, but {} were given."
                            .format(EggholderFunction.NUM_OF_VARIABLES, len(variables)))
        x, y = variables
        a = math.sqrt(math.fabs(y + x / 2 + 47))
        b = math.sqrt(math.fabs(x - (y + 47)))

        return -(y + 47) * math.sin(a) - x * math.sin(b)


class CrossInTrayFunction(BaseFitnessFunction):
    # example function, minimum = -2.06261 in (+-1.3491, +=1.3491), range [-10, 10], maximum in (0,0) range [-2, 2]

    NUM_OF_VARIABLES = 2

    def evaluate(self, variables):
        if len(variables) != CrossInTrayFunction.NUM_OF_VARIABLES:
            raise Exception("Function takes {} arguments, but {} were given."
                            .format(CrossInTrayFunction.NUM_OF_VARIABLES, len(variables)))
        x, y = variables
        a = math.fabs(100 - math.sqrt(x * x + y * y) / math.pi)
        b = math.fabs(math.sin(x) * math.sin(y) * math.exp(a)) + 1

        return -0.0001 * b ** 0.1


class TestFunction(BaseFitnessFunction):
    # example function, minimum = 0 in (0, 0)

    NUM_OF_VARIABLES = 2

    def evaluate(self, variables):
        if len(variables) != TestFunction.NUM_OF_VARIABLES:
            raise Exception("Function takes {} arguments, but {} were given."
                            .format(TestFunction.NUM_OF_VARIABLES, len(variables)))
        x, y = variables

        return x * x + y * y

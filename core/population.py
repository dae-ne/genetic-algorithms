import math
import random
import statistics

from core.fitness_function import BaseFitnessFunction


class Population:
    def __init__(self):
        self.__candidates = []

    @property
    def candidates(self):
        return self.__candidates

    @property
    def size(self):
        return len(self.candidates)

    def __str__(self):
        return "\n".join("{}. {}".format(i + 1, candidate) for i, candidate in enumerate(self.candidates))

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def get_best_candidate(self, maximization=False):
        return self.get_n_best_candidates(maximization=maximization)[0]

    def get_n_best_candidates(self, n=1, maximization=False):
        return sorted(self.candidates, key=lambda candidate: candidate.score, reverse=maximization)[:n]

    def get_average_score(self):
        return statistics.mean([candidate.score for candidate in self.candidates])

    def get_standard_deviation(self):
        return statistics.stdev([candidate.score for candidate in self.candidates])


class Candidate:
    def __init__(self, chromosomes, fitness_function):
        self.chromosomes = chromosomes
        self.fitness_function = fitness_function

    @property
    def chromosomes(self):
        return self.__chromosomes

    @chromosomes.setter
    def chromosomes(self, value):
        if not isinstance(value, list):
            raise ValueError("Given object is not an instance of list.")
        self.__chromosomes = value

    @property
    def fitness_function(self):
        return self.__fitness_function

    @fitness_function.setter
    def fitness_function(self, value):
        if not isinstance(value, BaseFitnessFunction):
            raise ValueError("Given object is not an instance of BaseFitnessFunction.")
        self.__fitness_function = value

    @property
    def decoded_chromosomes(self):
        return [chromosome.decode_to_decimal() for chromosome in self.chromosomes]

    @property
    def score(self):
        return self.fitness_function.evaluate(self.decoded_chromosomes)

    def __str__(self):
        return "score = {}, {}".format(self.score, ", ".join(
            ["x{} = {} ({})".format(i, solution, chromosome) for i, (chromosome, solution)
             in enumerate(zip(self.chromosomes, self.decoded_chromosomes))]))


class Chromosome:
    def __init__(self, gen_list, range_from, range_to):
        self.gen_list = gen_list
        self.range_from = range_from
        self.range_to = range_to

    @property
    def gen_list(self):
        return self.__gen_list

    @gen_list.setter
    def gen_list(self, value):
        if not isinstance(value, list):
            raise ValueError("Given object is not an instance of list.")
        self.__gen_list = value

    @property
    def range_from(self):
        return self.__range_from

    @range_from.setter
    def range_from(self, value):
        if value != float(value):
            raise ValueError("Given value should be float.")
        self.__range_from = value

    @property
    def range_to(self):
        return self.__range_to

    @range_to.setter
    def range_to(self, value):
        if value != float(value):
            raise ValueError("Given value should be float.")
        self.__range_to = value

    @property
    def num_of_bits(self):
        return len(self.__gen_list)

    def __str__(self):
        return "".join([str(x) for x in self.gen_list])

    def decode_to_decimal(self):
        binary_str = ''.join([str(x) for x in self.gen_list])
        decimal_num = int(binary_str, 2)

        return self.range_from + decimal_num * (self.range_to - self.range_from) / (pow(2, self.num_of_bits) - 1)

    @staticmethod
    def calculate_num_of_bits(range_from, range_to, precision):
        return math.ceil(math.log2((range_to - range_from) * pow(10, precision) + 1))


class Generator:
    @staticmethod
    def generate_random_population(size, range_from, range_to, precision, fitness_function):
        if range_from > range_to:
            range_from, range_to = range_to, range_from

        population = Population()
        num_of_bits = Chromosome.calculate_num_of_bits(range_from, range_to, precision)

        for _ in range(size):
            candidate = Generator.generate_random_candidate(num_of_bits, range_from, range_to, fitness_function)
            population.add_candidate(candidate)

        return population

    @staticmethod
    def generate_random_candidate(num_of_bits, range_from, range_to, fitness_function):
        chromosomes = []
        for _ in range(fitness_function.NUM_OF_VARIABLES):
            chromosomes.append(Generator.generate_random_chromosome(num_of_bits, range_from, range_to))

        return Candidate(chromosomes, fitness_function)

    @staticmethod
    def generate_random_chromosome(num_of_bits, range_from, range_to):
        return Chromosome([random.randint(0, 1) for _ in range(num_of_bits)], range_from, range_to)

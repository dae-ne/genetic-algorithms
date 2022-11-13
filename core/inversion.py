import random

from core.population import Candidate


class InversionMethod:
    def __init__(self, probability):
        self.probability = probability / 100

    def should_inverse(self):
        return random.random() < self.probability

    def inverse(self, candidate: Candidate):
        if not self.should_inverse():
            return candidate

        for chromosome in candidate.chromosomes:
            inversion_range = [random.randint(0, len(chromosome.gen_list)) for _ in range(2)]
            inversion_range.sort()
            chromosome.gen_list[inversion_range[0]:inversion_range[1]] = \
                reversed(chromosome.gen_list[inversion_range[0]:inversion_range[1]])

        return candidate

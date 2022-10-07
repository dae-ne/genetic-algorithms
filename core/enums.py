from strenum import StrEnum
from enum import auto


class SelectionMethod(StrEnum):
    BEST = auto()
    TOURNAMENT = auto()
    ROULETTE = auto()

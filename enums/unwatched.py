from enum import Enum


class Unwatched(Enum):
    @staticmethod
    def assign(val):
        return val

    @staticmethod
    def get_factor(val):
        return val * 300
from enum import Enum


class Watched(Enum):
    LOVE = "love"
    LIKE = "like"
    NEUTRAL = "neutral"
    DISLIKE = "dislike"

    @staticmethod
    def assign(val):
        if val in [Watched.LOVE, "love", "LOVE"]:
            return Watched.LOVE

        if val in [Watched.LIKE, "like", "LIKE"]:
            return Watched.LIKE

        if val in [Watched.NEUTRAL, "neutral", "NEUTRAL"]:
            return Watched.NEUTRAL

        if val in [Watched.DISLIKE, "dislike", "DISLIKE"]:
            return Watched.DISLIKE

        return None

    @staticmethod
    def get_factor(val):
        if val == Watched.LOVE:
            return 300
        if val == Watched.LIKE:
            return 200
        if val == Watched.NEUTRAL:
            return 100
        if val == Watched.DISLIKE:
            return 0

        return None

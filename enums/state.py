from enums.unwatched import *
from enums.watched import *
from enums.state import *

class State(Enum):
    WATCHED = 1
    UNWATCHED = 0

    @staticmethod
    def status(value):
        if Watched.assign(value) is not None:
            return State.WATCHED
        else:
            return State.UNWATCHED
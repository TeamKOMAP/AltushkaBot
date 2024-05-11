from enum import Enum
from typing import Tuple


class ACommandsType(Enum):
    PREV = 'Prev'
    SKIP = 'Skip'
    PAUSE = 'Pause'
    RESUME = 'Resume'
    CONTEXT = 'Context'
    PLAY = 'Play'
    STOP = 'Stop'
    RESET = 'Reset'
    NOW_PLAYING = 'Now Playing'
    TERMINATE = 'Terminate'
    VOLUME = 'Volume'
    SLEEPING = 'Sleeping'


class ACommands:
    def __init__(self, type: ACommandsType, args=None) -> None:
        self.__type = type
        self.__args = args

    def getType(self) -> ACommandsType:
        return self.__type

    def getArgs(self) -> Tuple:
        return self.__args

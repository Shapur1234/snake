from enum import Enum


class Dir(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3

    def opposite(self):
        if self.value == 0:
            return Dir.DOWN
        if self.value == 1:
            return Dir.UP
        if self.value == 2:
            return Dir.LEFT
        if self.value == 3:
            return Dir.RIGHT

        raise Exception("Unhandeled Dir")

from typing import Tuple
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

    def move_pos(self, pos: Tuple[int, int], by: int = 1) -> Tuple[int, int]:
        if self.value == 0:
            return (pos[0], pos[1] + by)
        if self.value == 1:
            return (pos[0], pos[1] - by)
        if self.value == 2:
            return (pos[0] + by, pos[1])
        if self.value == 3:
            return (pos[0] + by, pos[1])

        raise Exception("Unhandeled Dir")

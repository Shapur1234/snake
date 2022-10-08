from typing import Tuple

from params import background_color, food_color, wall_color
from enum import Enum


class Tile(Enum):
    EMPTY = 0
    FOOD = 1
    WALL = 2

    def color(self) -> Tuple[int, int, int]:
        if self.value == 0:
            return background_color
        if self.value == 1:
            return food_color
        if self.value == 2:
            return wall_color

        raise Exception("Unhandeled Tile")

from typing import Tuple

from params import background_color, food_color
from enum import Enum


# Enum representing possible tiles on the map
class Tile(Enum):
    EMPTY = 0
    FOOD = 1

    def color(self) -> Tuple[int, int, int]:
        if self.value == 0:
            return background_color
        if self.value == 1:
            return food_color

        raise Exception("Unhandeled Tile")

from tile import Tile

import pygame
import random as rnd
from typing import Tuple


class GameField:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.data = [Tile.EMPTY] * (width * height)

        self.spawn_food()

    def get_field(self, key: Tuple[int, int]) -> Tile:
        return self.data[key[0] * self.height + key[1]]

    def spawn_food(self) -> None:
        # TODO: Check snake
        for _ in range(self.width * self.height):
            key = (rnd.randint(0, self.width - 1),
                   rnd.randint(0, self.height - 1))

            if self.get_field(key) != Tile.FOOD:
                self.set_field(key, Tile.FOOD)
                break

    def set_field(self, key: Tuple[int, int], value: Tile) -> None:
        self.data[key[0] * self.height + key[1]] = value

    def block_size(self, surface) -> Tuple[int, int]:
        return (surface.get_width() // self.width, surface.get_height() // self.height)

    def xy_from_index(self, index: int) -> Tuple[int, int]:
        x = index % self.width
        y = (index - x) // self.width

        return (x, y)

    def draw(self, surface) -> None:
        block_width, block_height = self.block_size(surface)
        for index, tile in enumerate(self.data):
            x, y = self.xy_from_index(index)

            pygame.draw.rect(surface, tile.color(), pygame.Rect(
                x * block_width, y * block_height, block_width, block_height))

    width: int

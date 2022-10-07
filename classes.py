from params import background_color, food_color, wall_color

import pygame
import random as rnd
from typing import Tuple
from enum import Enum


class Tile(Enum):
    EMPTY = 0
    WALL = 1
    FOOD = 2


def color_from_tile(tile: Tile) -> Tuple[int, int, int]:
    if tile == Tile.EMPTY:
        return background_color
    if tile == Tile.FOOD:
        return food_color
    if tile == Tile.WALL:
        return wall_color

    raise Exception("Unhandeled tyle color")


class GameField:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.data = [Tile.EMPTY] * (width * height)

        self.spawn_food()

    def get_field(self, key: Tuple[int, int]) -> Tile:
        return self.data[key[0] * self.height + key[1]]

    def set_field(self, key: Tuple[int, int], value: Tile) -> None:
        self.data[key[0] * self.height + key[1]] = value

    def xy_from_index(self, index: int) -> Tuple[int, int]:
        x = index % self.width
        y = (index - x) // self.width

        return (x, y)

    def spawn_food(self) -> None:
        for _ in range(self.width * self.height):
            key = (rnd.randint(0, self.width - 1),
                   rnd.randint(0, self.height - 1))

            if self.get_field(key) != Tile.FOOD:
                self.set_field(key, Tile.FOOD)
                break

    def draw(self, surface) -> None:
        block_width, block_height = surface.get_width(
        ) / self.width, surface.get_height() / self.height

        for index, tile in enumerate(self.data):
            color = color_from_tile(tile)
            x, y = self.xy_from_index(index)

            pygame.draw.rect(surface, color, pygame.Rect(
                x * block_width, y * block_height, block_width, block_height))

    width: int
    height: int
    data: list[Tile]

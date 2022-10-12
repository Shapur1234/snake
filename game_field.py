from tile import Tile

import pygame
from typing import Tuple


class GameField:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.data = [Tile.EMPTY] * (width * height)

    def get_field(self, key: Tuple[int, int]) -> Tile:
        return self.data[key[1] * self.width + key[0]]

    def set_field(self, key: Tuple[int, int], value: Tile) -> None:
        self.data[key[1] * self.width + key[0]] = value

    def block_size(self, surface) -> Tuple[int, int]:
        return (surface.get_width() // self.width, surface.get_height() // self.height)

    def xy_from_index(self, index: int) -> Tuple[int, int]:
        x = index % self.width
        y = (index - x) // self.width

        return (x, y)

    def draw(self, surface, offset: Tuple[int, int] = (0, 0)) -> None:
        block_width, block_height = self.block_size(surface)
        for index, tile in enumerate(self.data):
            if tile != Tile.EMPTY:
                x, y = self.xy_from_index(index)

                pygame.draw.rect(surface, tile.color(), pygame.Rect(
                    x * block_width + 1 + offset[0], y * block_height + offset[1], block_width - 2, block_height - 2))

    width: int
    height: int
    data: list[Tile]

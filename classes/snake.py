from params import snake_head_color, snake_body_color
from dir import Dir

from typing import Tuple
import pygame


class Snake:
    def __init__(self, pos: tuple[int, int], facing: Dir = Dir.RIGHT) -> None:
        self.head_pos = pos
        self.facing = facing
        self.body = list[SnakePiece]

    def move(self) -> None:
        pass

    def draw(self, block_size: Tuple[int, int], surface) -> None:
        pygame.draw.rect(surface, snake_head_color,
                         self.pos[0] * block_size[0], self.pos[1] * block_size[1], block_size[0], block_size[1])

        for snake_piece in self.body:
            snake_piece.draw(block_size, surface)

    pos: tuple[int, int]
    facing: Dir


class SnakePiece:
    def __init__(self, pos: tuple[int, int]) -> None:
        self.pos = pos

    def draw(self, block_size: Tuple[int, int], surface) -> None:
        pygame.draw.rect(surface, snake_body_color,
                         self.pos[0] * block_size[0], self.pos[1] * block_size[1], block_size[0], block_size[1])

    pos: tuple[int, int]

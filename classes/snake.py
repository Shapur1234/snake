from params import snake_head_color, snake_body_color
from dir import Dir

from typing import Tuple
import pygame


class SnakePiece:
    def __init__(self, pos: tuple[int, int]) -> None:
        self.pos = pos

    def draw(self, block_size: Tuple[int, int], surface) -> None:
        pygame.draw.rect(surface, snake_body_color, pygame.Rect(
            self.pos[0] * block_size[0], self.pos[1] * block_size[1], block_size[0], block_size[1]))

    pos: tuple[int, int]


class Snake:
    def __init__(self, pos: tuple[int, int], facing: Dir = Dir.RIGHT) -> None:
        self.pos = pos
        self.facing = facing
        self.body = [SnakePiece((facing.opposite().move_pos(pos)))]

    def move(self) -> None:
        if len(self.body) > 1:
            self.body[-1].pos = self.pos

        self.pos = self.facing.move_pos(self.pos)

    def rotate(self, dir: Dir) -> None:
        if dir != self.dir.opposite():
            self.dir = dir

    def draw(self, block_size: Tuple[int, int], surface) -> None:
        pygame.draw.rect(surface, snake_head_color, pygame.Rect(
            self.pos[0] * block_size[0], self.pos[1] * block_size[1], block_size[0], block_size[1]))

        for snake_piece in self.body:
            snake_piece.draw(block_size, surface)

    pos: tuple[int, int]
    facing: Dir
    body = list[SnakePiece]

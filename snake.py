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
        self.skip_adding_segment = False

    def move(self) -> None:
        if len(self.body) != 0:
            if not self.skip_adding_segment:
                last_piece = self.body.pop()
                last_piece.pos = self.pos
                self.body.insert(0, last_piece)
            else:
                self.skip_adding_segment = False

        self.pos = self.facing.move_pos(self.pos)

    def append_segment(self) -> None:
        self.skip_adding_segment = True
        self.body.insert(0, SnakePiece(self.pos))

    def rotate(self, facing: Dir) -> None:
        if facing != self.facing.opposite():
            self.facing = facing

    def draw(self, block_size: Tuple[int, int], surface) -> None:
        pygame.draw.rect(surface, snake_head_color, pygame.Rect(
            self.pos[0] * block_size[0], self.pos[1] * block_size[1], block_size[0], block_size[1]))

        for snake_piece in self.body:
            snake_piece.draw(block_size, surface)

    def segment_posses(self, including_head=True):
        return [self.pos] if including_head else [] + [segment.pos for segment in self.body]

    pos: tuple[int, int]
    facing: Dir
    body:  list[SnakePiece]
    skip_adding_segment: bool

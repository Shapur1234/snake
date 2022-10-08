from params import snake_head_color, snake_light_color, repetition_length
from dir import Dir

from typing import Tuple
import pygame


class SnakePiece:
    def __init__(self, pos: tuple[int, int]) -> None:
        self.pos = pos

    def draw(self, block_size: Tuple[int, int], color_index, surface) -> None:
        pygame.draw.rect(surface, snake_body_color(color_index + 1), pygame.Rect(
            self.pos[0] * block_size[0] + 1, self.pos[1] * block_size[1] + 1, block_size[0] - 2, block_size[1] - 2))

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

        for index, snake_piece in enumerate(self.body):
            snake_piece.draw(block_size, index, surface)

    def segment_posses(self, including_head=True):
        return [self.pos] if including_head else [] + [segment.pos for segment in self.body]

    pos: tuple[int, int]
    facing: Dir
    body:  list[SnakePiece]
    skip_adding_segment: bool


def snake_body_color(color_index: int) -> Tuple[int, int, int]:
    index = None
    if ((color_index // repetition_length)) % 2 == 0:
        index = color_index % repetition_length
    else:
        index = repetition_length - (color_index % repetition_length)

    return lerp_color(snake_head_color, snake_light_color, index / repetition_length)


def lerp(a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b


def lerp_color(col_a: Tuple[int, int, int], col_b: Tuple[int, int, int], by: float) -> Tuple[int, int, int]:
    return (int(lerp(float(col_a[0]), float(col_b[0]), by)), int(lerp(float(col_a[1]), float(col_b[1]), by)), int(lerp(float(col_a[2]), float(col_b[2]), by)))

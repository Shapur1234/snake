import random
import pygame

from game_field import GameField
from snake import Snake
from params import background_color, key_up, key_down, key_right, key_left, border_color
from dir import Dir
from tile import Tile


# Object storing game state and game logic
class Game:
    def __init__(self, width: int, height: int, num_of_foods: int = 1) -> None:
        self.game_field = GameField(width, height)
        self.snake = Snake((width // 2, height // 2))

        for _ in range(num_of_foods):
            self.spawn_food()

    def draw(self, surface) -> None:
        block_size = self.game_field.block_size(surface)
        screen_size = (surface.get_width(), surface.get_height())
        offset = (
            (screen_size[0] % block_size[0]) // 2,
            (screen_size[1] % block_size[1]) // 2,
        )

        surface.fill(background_color)
        pygame.draw.rect(
            surface, border_color, pygame.Rect(0, 0, offset[0], screen_size[1])
        )
        pygame.draw.rect(
            surface, border_color, pygame.Rect(0, 0, screen_size[0], offset[1])
        )
        pygame.draw.rect(
            surface,
            border_color,
            pygame.Rect(screen_size[0] - offset[0], 0, offset[0], screen_size[1]),
        )
        pygame.draw.rect(
            surface,
            border_color,
            pygame.Rect(0, screen_size[1] - offset[1], screen_size[0], offset[1]),
        )

        self.game_field.draw(surface, offset)
        self.snake.draw(self.game_field.block_size(surface), surface, offset)

    def spawn_food(self) -> None:
        for _ in range(self.game_field.width * self.game_field.height):
            key = (
                random.randint(0, self.game_field.width - 1),
                random.randint(0, self.game_field.height - 1),
            )

            if (
                self.game_field.get_field(key) == Tile.EMPTY
                and key not in self.snake.segment_posses()
            ):
                self.game_field.set_field(key, Tile.FOOD)
                break

    def check_food_colision(self) -> bool:
        return self.game_field.get_field(self.snake.pos) == Tile.FOOD

    def check_wall_collision(self) -> bool:
        x, y = self.snake.pos
        return (x < 0 or x >= self.game_field.width) or (
            y < 0 or y >= self.game_field.height
        )

    def check_segment_collision(self) -> bool:
        return self.snake.pos in self.snake.segment_posses(False)

    def game_tick(self) -> bool:
        self.snake.move()

        if self.check_wall_collision() or self.check_segment_collision():
            return True

        if self.check_food_colision():
            self.snake.append_segment()

            self.game_field.set_field(self.snake.pos, Tile.EMPTY)
            self.spawn_food()

        return False

    def handle_input(self, key) -> None:
        if key == key_up[0] or key == key_up[1]:
            self.snake.rotate(Dir.UP)
        elif key == key_down[0] or key == key_down[1]:
            self.snake.rotate(Dir.DOWN)
        elif key == key_right[0] or key == key_right[1]:
            self.snake.rotate(Dir.RIGHT)
        elif key == key_left[0] or key == key_left[1]:
            self.snake.rotate(Dir.LEFT)

    def score(self) -> int:
        return len(self.snake.body) + 1

    game_field: GameField
    snake: Snake

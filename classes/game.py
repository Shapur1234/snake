from game_field import GameField
from snake import Snake
from params import key_up, key_down, key_right, key_left
from dir import Dir


class Game:
    def __init__(self, width: int, height: int) -> None:
        self.game_field = GameField(width, height)
        self.snake = Snake((width // 2, height // 2))

    def draw(self, surface) -> None:
        self.game_field.draw(surface)
        self.snake.draw(self.game_field.block_size(surface), surface)

    def game_tick(self) -> None:
        self.snake.move()

    def handle_input(self, key) -> None:
        if key == key_up:
            self.snake.rotate(Dir.UP)
        elif key == key_down:
            self.snake.rotate(Dir.DOWN)
        elif key == key_right:
            self.snake.rotate(Dir.RIGHT)
        elif key == key_left:
            self.snake.rotate(Dir.LEFT)

    def score(self) -> int:
        return len(self.snake.body) + 1

    game_field: GameField
    snake: Snake

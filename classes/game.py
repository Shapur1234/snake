from game_field import GameField
from snake import Snake


class Game:
    def __init__(self, width: int, height: int) -> None:
        self.game_field = GameField(width, height)
        self.snake = Snake((width // 2, height // 2))

    def draw(self, surface) -> None:
        self.game_field.draw(surface)
        self.snake.draw(self.game_field.block_size(surface), surface)

    def step(self) -> None:
        self.snake.move()

    def handle_input(self) -> None:
        pass

    game_field: GameField
    snake: Snake

import sys
sys.path.insert(1, "./classes")

from params import screen_width, screen_height
from game_field import GameField
import pygame

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    game_field = GameField(screen_width // 20, screen_height // 20)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_field.draw(screen)
        pygame.display.flip()

pygame.quit()

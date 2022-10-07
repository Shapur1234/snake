from params import screen_width, screen_height
from classes import GameField

import pygame

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    game_field = GameField(20, 40)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_field.draw(screen)
        pygame.display.flip()

pygame.quit()

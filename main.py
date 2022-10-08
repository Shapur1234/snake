import sys
sys.path.insert(1, "./classes")

from params import screen_width, screen_height, fps_target
from dir import Dir
from game import Game
import pygame


if __name__ == "__main__":
    clock = pygame.time.Clock()

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    game_state = Game(screen_width // 20, screen_height // 20)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                game_state.handle_input(event.key)

        game_state.game_tick()

        game_state.draw(screen)
        pygame.display.flip()

        clock.tick(fps_target)

pygame.quit()

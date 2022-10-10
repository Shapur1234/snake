from params import text_color, screen_width, screen_height, fps_target, key_reset, key_quit, num_of_foods, tile_scale, key_speed_up, key_speed_down
from game import Game
import pygame


if __name__ == "__main__":
    clock = pygame.time.Clock()

    pygame.init()
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode(
        (screen_width, screen_height), pygame.RESIZABLE)
    font = pygame.font.Font(pygame.font.get_default_font(), 36)

    game_state = Game(screen.get_width() // tile_scale,
                      screen.get_height() // tile_scale, num_of_foods)

    stopped = False
    running = True
    while running:
        input_to_handle = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == key_quit:
                    running = False
                if event.key == key_reset:
                    game_state = Game(screen.get_width() // tile_scale,
                                      screen.get_height() // tile_scale, num_of_foods)
                    stopped = False
                    continue
                if event.key == key_speed_up:
                    fps_target = max(fps_target + 4, 1)
                if event.key == key_speed_down:
                    fps_target = max(fps_target - 4, 1)

                input_to_handle = event.key

        if not stopped:
            game_state.handle_input(input_to_handle)
            if game_state.game_tick():
                stopped = True

        game_state.draw(screen)
        if stopped:
            screen.blit(font.render(
                f"Score: {game_state.score()}", True, text_color), (16, 16))

        pygame.display.flip()
        clock.tick(fps_target)

pygame.quit()

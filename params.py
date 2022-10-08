import pygame

screen_width = 1200
screen_height = 800

fps_target = 20

num_of_foods = 100

text_color = (255, 255, 255)
background_color = (7, 42, 108)
wall_color = (190, 190, 190)
food_color = (255, 0, 0)

snake_body_color = (28, 107, 0)
snake_head_color = (108, 187, 80)

key_up = (pygame.K_w, pygame.K_UP)
key_down = (pygame.K_s, pygame.K_DOWN)
key_right = (pygame.K_d, pygame.K_RIGHT)
key_left = (pygame.K_a, pygame.K_LEFT)
key_reset = pygame.K_r
key_quit = pygame.K_q

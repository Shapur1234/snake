import pygame

screen_width = 640
screen_height = 360
tile_scale = 32
fps_target = 16

num_of_foods = 64

text_color = (255, 255, 255)
background_color = (7, 42, 108)
wall_color = (190, 190, 190)
food_color = (255, 0, 0)
border_color = (0, 0, 63)

snake_head_color = (2, 48, 32)
snake_light_color = (124, 252, 0)
repetition_length = 32

key_up = (pygame.K_w, pygame.K_UP)
key_down = (pygame.K_s, pygame.K_DOWN)
key_right = (pygame.K_d, pygame.K_RIGHT)
key_left = (pygame.K_a, pygame.K_LEFT)
key_reset = pygame.K_r
key_quit = pygame.K_q
key_speed_up = pygame.K_k
key_speed_down = pygame.K_j

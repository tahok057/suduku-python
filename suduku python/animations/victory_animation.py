import pygame
import random
import time


def play_victory_animation(screen):
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
    for _ in range(30):
        color = random.choice(colors)
        radius = random.randint(10, 50)
        position = (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))
        pygame.draw.circle(screen, color, position, radius)
        pygame.display.flip()
        time.sleep(0.1)

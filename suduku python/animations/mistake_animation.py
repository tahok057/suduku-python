import pygame
import time


def play_mistake_animation(screen, position, cell_size):
    red = (255, 0, 0)
    for _ in range(5):
        pygame.draw.rect(screen, red, (*position, cell_size, cell_size), 3)
        pygame.display.flip()
        time.sleep(0.1)
        pygame.draw.rect(screen, (255, 255, 255), (*position, cell_size, cell_size), 3)
        pygame.display.flip()
        time.sleep(0.1)

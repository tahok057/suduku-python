import pygame


class GameEnd:
    def __init__(self, screen):
        self.screen = screen
        self.restart_game = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.restart_game = True

    def update(self):
        pass

    def render(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 255, 255))
        self.screen.blit(text, (200, 250))

    def reset(self):
        self.restart_game = False

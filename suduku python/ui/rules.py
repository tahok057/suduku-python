import pygame


class Rules:
    def __init__(self, screen):
        self.screen = screen
        self.back_to_menu = False
        self.font = pygame.font.Font(None, 36)
        self.rules_text = [
            "Sudoku Rules:",
            "1. Each row must contain the numbers 1-9 without repetition.",
            "2. Each column must contain the numbers 1-9 without repetition.",
            "3. Each 3x3 sub-grid must contain the numbers 1-9 without repetition.",
            "4. Use the numbers from 1 to 9 to fill the grid.",
            "5. Click on a cell to select it, and then type a number to enter it."
        ]
        self.back_button = pygame.Rect(250, 500, 100, 50)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.back_button.collidepoint(x, y):
                self.back_to_menu = True

    def update(self):
        pass

    def render(self):
        self.screen.fill((255, 255, 255))
        for i, line in enumerate(self.rules_text):
            text = self.font.render(line, True, (0, 0, 0))
            self.screen.blit(text, (20, 20 + i * 40))

        pygame.draw.rect(self.screen, (0, 200, 0), self.back_button)
        back_text = self.font.render("Back", True, (255, 255, 255))
        self.screen.blit(back_text, (self.back_button.x + 20, self.back_button.y + 10))

    def reset(self):
        self.back_to_menu = False

import pygame


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.title_text = self.font.render("Sudoku Game", True, (0, 0, 0))

        self.button_font = pygame.font.Font(None, 48)
        self.button_color = (0, 200, 0)

        button_width = 300
        button_height = 70

        self.start_button_rect = pygame.Rect((self.screen.get_width() - button_width) // 2, 300, button_width,
                                             button_height)
        self.rules_button_rect = pygame.Rect((self.screen.get_width() - button_width) // 2, 400, button_width,
                                             button_height)
        self.quit_button_rect = pygame.Rect((self.screen.get_width() - button_width) // 2, 500, button_width,
                                            button_height)

        self.start_button_text = self.button_font.render("Start Game", True, (255, 255, 255))
        self.rules_button_text = self.button_font.render("Rules", True, (255, 255, 255))
        self.quit_button_text = self.button_font.render("Quit Game", True, (255, 255, 255))

    def handle_event(self, event):
        try:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.start_button_rect.collidepoint(x, y):
                    return "start"
                elif self.rules_button_rect.collidepoint(x, y):
                    return "rules"
                elif self.quit_button_rect.collidepoint(x, y):
                    pygame.quit()
                    exit()
        except Exception as e:
            print(f"An error occurred in MainMenu.handle_event: {e}")
        return None

    def render(self):
        try:
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.title_text, ((self.screen.get_width() - self.title_text.get_width()) // 2, 150))

            pygame.draw.rect(self.screen, self.button_color, self.start_button_rect)
            self.screen.blit(self.start_button_text, (
                self.start_button_rect.x + (self.start_button_rect.width - self.start_button_text.get_width()) // 2,
                self.start_button_rect.y + (self.start_button_rect.height - self.start_button_text.get_height()) // 2))

            pygame.draw.rect(self.screen, self.button_color, self.rules_button_rect)
            self.screen.blit(self.rules_button_text, (
                self.rules_button_rect.x + (self.rules_button_rect.width - self.rules_button_text.get_width()) // 2,
                self.rules_button_rect.y + (self.rules_button_rect.height - self.rules_button_text.get_height()) // 2))

            pygame.draw.rect(self.screen, self.button_color, self.quit_button_rect)
            self.screen.blit(self.quit_button_text, (
                self.quit_button_rect.x + (self.quit_button_rect.width - self.quit_button_text.get_width()) // 2,
                self.quit_button_rect.y + (self.quit_button_rect.height - self.quit_button_text.get_height()) // 2))
        except Exception as e:
            print(f"An error occurred in MainMenu.render: {e}")


class RulesScreen:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font(None, 60)
        self.title_text = self.title_font.render("Game Rules", True, (0, 0, 0))
        self.font = pygame.font.Font(None, 30)
        self.rules_text = [
            "1. Fill all the empty cells in the grid with digits from 1 to 9.",
            "2. Each row, column, and 3x3 sub-grid must contain all digits from 1 to 9.",
            "3. No row, column, or 3x3 sub-grid can have repeated digits.",
            "4. Use logic and deduction to find the correct numbers.",
            "5. The game ends when the entire grid is correctly filled."
        ]

        self.button_font = pygame.font.Font(None, 48)
        self.button_color = (0, 200, 0)
        self.back_button_rect = pygame.Rect((self.screen.get_width() - 200) // 2, 600, 200, 50)
        self.back_button_text = self.button_font.render("Back", True, (255, 255, 255))

    def handle_event(self, event):
        try:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.back_button_rect.collidepoint(x, y):
                    return "back"
        except Exception as e:
            print(f"An error occurred in RulesScreen.handle_event: {e}")
        return None

    def render(self):
        try:
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.title_text, ((self.screen.get_width() - self.title_text.get_width()) // 2, 50))

            for i, line in enumerate(self.rules_text):
                rules_line_text = self.font.render(line, True, (0, 0, 0))
                self.screen.blit(rules_line_text, (50, 150 + i * 40))

            pygame.draw.rect(self.screen, self.button_color, self.back_button_rect)
            self.screen.blit(self.back_button_text, (
                self.back_button_rect.x + (self.back_button_rect.width - self.back_button_text.get_width()) // 2,
                self.back_button_rect.y + (self.back_button_rect.height - self.back_button_text.get_height()) // 2))
        except Exception as e:
            print(f"An error occurred in RulesScreen.render: {e}")

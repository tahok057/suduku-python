import pygame
import random
from logic.sudoku import Sudoku
from animations.mistake_animation import play_mistake_animation
from animations.victory_animation import play_victory_animation


class Game:
    def __init__(self, screen):
        try:
            self.screen = screen
            self.sudoku = Sudoku()
            self.game_over = False
            self.selected_cell = None
            self.font = pygame.font.Font(None, 48)
            self.cell_size = 80
            self.grid_offset = 50
            self.initial_grid = [row[:] for row in self.sudoku.grid]
            self.mistake = False
            self.mistake_timer = 0
            self.mistake_duration = 1000
            self.buzz_sound = pygame.mixer.Sound('sounds/buzz.mp3')
            self.victory_sound = pygame.mixer.Sound('sounds/victory.mp3')
            self.mistake_text = None
            self.mistake_text_pos = (0, 0)
            self.shake_effect = 0

            button_width = 200
            button_height = 50
            self.victory_button_color = (0, 200, 0)

            self.new_game_button_rect = pygame.Rect((self.screen.get_width() - button_width) // 2, 450, button_width,
                                                    button_height)
            self.new_game_button_text = self.font.render("New Game", True, (255, 255, 255))

            self.main_menu_button_rect = pygame.Rect((self.screen.get_width() - button_width) // 2, 520, button_width,
                                                     button_height)
            self.main_menu_button_text = self.font.render("Main Menu", True, (255, 255, 255))

            self.quit_game_button_rect = pygame.Rect((self.screen.get_width() - button_width) // 2, 590, button_width,
                                                     button_height)
            self.quit_game_button_text = self.font.render("Quit Game", True, (255, 255, 255))

            self.display_victory = False
        except Exception as e:
            print(f"An error occurred during Game initialization: {e}")

    def handle_event(self, event):
        try:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.display_victory and self.new_game_button_rect.collidepoint(x, y):
                    self.reset()
                    return
                if self.display_victory and self.quit_game_button_rect.collidepoint(x, y):
                    pygame.quit()
                    exit()
                if self.display_victory and self.main_menu_button_rect.collidepoint(x, y):
                    return "main_menu"
                if self.grid_offset < x < self.grid_offset + 9 *\
                        self.cell_size and self.grid_offset < y < self.grid_offset + 9 * self.cell_size:
                    row = (y - self.grid_offset) // self.cell_size
                    col = (x - self.grid_offset) // self.cell_size
                    if self.initial_grid[row][col] == 0:
                        self.selected_cell = (row, col)
            elif event.type == pygame.KEYDOWN and self.selected_cell:
                row, col = self.selected_cell
                if self.initial_grid[row][col] == 0:
                    if event.key == pygame.K_1:
                        self.check_and_place_number(row, col, 1)
                    elif event.key == pygame.K_2:
                        self.check_and_place_number(row, col, 2)
                    elif event.key == pygame.K_3:
                        self.check_and_place_number(row, col, 3)
                    elif event.key == pygame.K_4:
                        self.check_and_place_number(row, col, 4)
                    elif event.key == pygame.K_5:
                        self.check_and_place_number(row, col, 5)
                    elif event.key == pygame.K_6:
                        self.check_and_place_number(row, col, 6)
                    elif event.key == pygame.K_7:
                        self.check_and_place_number(row, col, 7)
                    elif event.key == pygame.K_8:
                        self.check_and_place_number(row, col, 8)
                    elif event.key == pygame.K_9:
                        self.check_and_place_number(row, col, 9)
                    elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                        self.sudoku.grid[row][col] = 0
        except Exception as e:
            print(f"An error occurred in Game.handle_event: {e}")

    def check_and_place_number(self, row, col, number):
        try:
            if self.sudoku.is_valid_move(row, col, number):
                self.sudoku.grid[row][col] = number
            else:
                self.mistake = True
                self.mistake_timer = pygame.time.get_ticks()
                self.buzz_sound.play()
                self.shake_effect = 10
                font = pygame.font.Font(None, 74)
                self.mistake_text = font.render("Mistake", True, (255, 0, 0))
                self.mistake_text_pos = (
                    self.grid_offset + 2 * self.cell_size,
                    self.grid_offset + 4 * self.cell_size
                )
                play_mistake_animation(self.screen, (self.grid_offset + col * self.cell_size, self.grid_offset + row *
                                                     self.cell_size), self.cell_size)
        except Exception as e:
            print(f"An error occurred in Game.check_and_place_number: {e}")

    def complete_game(self):
        try:
            if self.solve_sudoku():
                self.game_over = True
                self.display_victory = True
                self.victory_sound.play()
                play_victory_animation(self.screen)
        except Exception as e:
            print(f"An error occurred in Game.complete_game: {e}")

    def solve_sudoku(self):
        try:
            empty = self.find_empty()
            if not empty:
                return True
            row, col = empty

            for num in range(1, 10):
                if self.sudoku.is_valid_move(row, col, num):
                    self.sudoku.grid[row][col] = num

                    if self.solve_sudoku():
                        return True

                    self.sudoku.grid[row][col] = 0

            return False
        except Exception as e:
            print(f"An error occurred in Game.solve_sudoku: {e}")

    def find_empty(self):
        try:
            for row in range(9):
                for col in range(9):
                    if self.sudoku.grid[row][col] == 0:
                        return row, col
            return None
        except Exception as e:
            print(f"An error occurred in Game.find_empty: {e}")

    def update(self):
        try:
            if not self.game_over and self.sudoku.check_victory():
                self.game_over = True
                self.display_victory = True
                self.victory_sound.play()
            if self.mistake and pygame.time.get_ticks() - self.mistake_timer > self.mistake_duration:
                self.mistake = False
            if self.shake_effect > 0:
                self.shake_effect -= 1
        except Exception as e:
            print(f"An error occurred in Game.update: {e}")

    def render(self):
        try:
            self.screen.fill((255, 255, 255))
            for row in range(9):
                for col in range(9):
                    value = self.sudoku.grid[row][col]
                    if value != 0:
                        color = (0, 0, 0) if self.initial_grid[row][col] != 0 else (0, 0, 255)
                        text = self.font.render(str(value), True, color)
                        x_offset = 0 if self.shake_effect == 0 else random.randint(-5, 5)
                        y_offset = 0 if self.shake_effect == 0 else random.randint(-5, 5)
                        self.screen.blit(text, (
                            self.grid_offset + col * self.cell_size + 20 + x_offset,
                            self.grid_offset + row * self.cell_size + 15 + y_offset
                        ))

            for i in range(10):
                line_width = 1 if i % 3 != 0 else 3
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (self.grid_offset, self.grid_offset + i * self.cell_size),
                                 (self.grid_offset + 9 * self.cell_size, self.grid_offset + i * self.cell_size),
                                 line_width)
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (self.grid_offset + i * self.cell_size, self.grid_offset),
                                 (self.grid_offset + i * self.cell_size, self.grid_offset + 9 * self.cell_size),
                                 line_width)

            if self.selected_cell and not self.display_victory:
                row, col = self.selected_cell
                pygame.draw.rect(self.screen, (255, 0, 0), (self.grid_offset + col *
                                                            self.cell_size, self.grid_offset + row *
                                                            self.cell_size, self.cell_size, self.cell_size), 3)

            if self.mistake:
                self.screen.blit(self.mistake_text, self.mistake_text_pos)

            if self.display_victory:
                font = pygame.font.Font(None, 74)
                text = font.render("Victory!", True, (0, 200, 0))
                self.screen.blit(text, ((self.screen.get_width() - text.get_width()) // 2, 350))

                pygame.draw.rect(self.screen, self.victory_button_color, self.new_game_button_rect)
                self.screen.blit(self.new_game_button_text, (self.new_game_button_rect.x + (self.new_game_button_rect.width - self.new_game_button_text.get_width()) // 2, self.new_game_button_rect.y + (self.new_game_button_rect.height - self.new_game_button_text.get_height()) // 2))

                pygame.draw.rect(self.screen, self.victory_button_color, self.main_menu_button_rect)
                self.screen.blit(self.main_menu_button_text, (self.main_menu_button_rect.x + (self.main_menu_button_rect.width - self.main_menu_button_text.get_width()) // 2, self.main_menu_button_rect.y + (self.main_menu_button_rect.height - self.main_menu_button_text.get_height()) // 2))

                pygame.draw.rect(self.screen, self.victory_button_color, self.quit_game_button_rect)
                self.screen.blit(self.quit_game_button_text, (self.quit_game_button_rect.x + (self.quit_game_button_rect.width - self.quit_game_button_text.get_width()) // 2, self.quit_game_button_rect.y + (self.quit_game_button_rect.height - self.quit_game_button_text.get_height()) // 2))
        except Exception as e:
            print(f"An error occurred in Game.render: {e}")

    def reset(self):
        try:
            self.sudoku = Sudoku()
            self.game_over = False
            self.selected_cell = None
            self.initial_grid = [row[:] for row in self.sudoku.grid]
            self.mistake = False
            self.mistake_timer = 0
            self.shake_effect = 0
            self.display_victory = False
        except Exception as e:
            print(f"An error occurred in Game.reset: {e}")

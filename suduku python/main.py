import pygame
from ui.game import Game
from ui.menu import MainMenu, RulesScreen


def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Sudoku Game")

        main_menu = MainMenu(screen)
        game = Game(screen)
        rules_screen = RulesScreen(screen)

        clock = pygame.time.Clock()

        state = "main_menu"

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                try:
                    if state == "main_menu":
                        action = main_menu.handle_event(event)
                        if action == "start":
                            game.reset()
                            state = "game"
                        elif action == "rules":
                            state = "rules"
                    elif state == "game":
                        action = game.handle_event(event)
                        if action == "main_menu":
                            state = "main_menu"
                    elif state == "rules":
                        action = rules_screen.handle_event(event)
                        if action == "back":
                            state = "main_menu"
                except Exception as e:
                    print(f"An error occurred: {e}")
                    running = False

            try:
                if state == "main_menu":
                    main_menu.render()
                elif state == "game":
                    game.update()
                    game.render()
                elif state == "rules":
                    rules_screen.render()
            except Exception as e:
                print(f"An error occurred during rendering: {e}")
                running = False

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
    except Exception as e:
        print(f"An error occurred during initialization or shutdown: {e}")


if __name__ == "__main__":
    main()

import pygame
import truppen
import ui

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 1000))
        self.clock = pygame.time.Clock()
        self.spielaktiv = True

        self.ui = ui.UIManager(self.screen)

        #Variabeln
        self.game_speed = 1
        self.truppen_liste = []

    def run(self):
        while self.spielaktiv:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.spielaktiv = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.game_speed = 1
                    if event.key == pygame.K_2:
                        self.game_speed = 2
                    if event.key == pygame.K_3:
                        self.game_speed = 3
                    if event.key == pygame.K_4:
                        self.game_speed = 4
                    if event.key == pygame.K_5:
                        self.game_speed = 5

                self.ui.handle_events(event)

            self.screen.fill((255, 255, 255))

            # HIER: Den Trupp aktualisieren und zeichnen
            self.ui.update(self.game_speed)

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()



if __name__ == "__main__":
    game = Main()
    game.run()
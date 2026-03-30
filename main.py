import pygame
import truppen

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.spielaktiv = True
        self.game_speed = 1

        # HIER: Den Trupp nur EINMAL erstellen!
        self.truppe = truppen.Trupp(self.screen, (255, 0, 0), (100, 100), 25)

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

                self.truppe.handle_event(event)

            self.screen.fill((255, 255, 255))

            # HIER: Den Trupp aktualisieren und zeichnen
            self.truppe.update(self.game_speed)
            self.truppe.zeichnen()

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    game = Main()
    game.run()
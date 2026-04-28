import pygame


class Trupp:
    def __init__(self, screen, color, pos, size):
        self.screen = screen
        self.color = color
        self.pos = pygame.math.Vector2(pos)
        self.size = size
        self.clicked = False  # Wir merken uns den Zustand
        self.arrow = False
        self.pos_arrow = None
        self.has_events = True


    def handle_event(self, event):
        """Behandelt nur die Mausklicks."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Linksklick: Auswahl
                mouse_pos = pygame.math.Vector2(event.pos)
                if self.pos.distance_to(mouse_pos) <= self.size:
                    self.clicked = not self.clicked

            if event.button == 3:  # Rechtsklick: Ziel setzen
                if self.clicked and self.arrow == False:
                    self.pos_arrow = pygame.math.Vector2(event.pos)
                    self.arrow = True

    def update(self, game_speed):
        speed = game_speed
        """Behandelt die kontinuierliche Bewegung (jeden Frame aufrufen)."""
        if self.pos_arrow:
            distanz = self.pos.distance_to(self.pos_arrow)

            if distanz > speed:
                richtung = (self.pos_arrow - self.pos).normalize()
                self.pos += richtung * speed
            else:
                self.pos = pygame.math.Vector2(self.pos_arrow)
                self.pos_arrow = None
                self.arrow = False

        # 2. Wenn er ausgewählt ist, einen schwarzen Rahmen drumherum
        if self.clicked:
            pygame.draw.circle(self.screen, (0, 0, 0), self.pos, self.size + 2, 3)

        if self.arrow:
            pygame.draw.line(self.screen, (0, 0, 0), self.pos, self.pos_arrow, 5)

        # 1. Den Hauptkreis zeichnen
        pygame.draw.circle(self.screen, self.color, self.pos, self.size)


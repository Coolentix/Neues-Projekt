import pygame
import truppen

class UIManager:
    def __init__(self, screen):
        self.elements = \
        [
            Map(screen),
            Button(screen, (100, 100, 100), (0, screen.get_height()-50), (50, 50)),
            truppen.Trupp(screen, (255, 0, 0), (25, 25), 25)
        ]

    def update(self, game_speed):
        for e in self.elements:
            try:
                e.update(game_speed)
            except TypeError:
                e.update()

    def handle_events(self, event):
        for e in self.elements:
            if hasattr(e, 'has_events'):
                e.handle_event(event)         # Methode in deiner Button-Klasse

class Button:
    def __init__(self, screen, color, pos, size, action=None):
        self.screen = screen
        self.size = size
        self.pos = pygame.math.Vector2(pos)
        self.color = color
        self.has_events = True
        self.action = action

    def handle_event(self, event):
        """Behandelt nur die Mausklicks."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Linksklick: Auswahl
                mouse_pos = pygame.math.Vector2(event.pos)
                if self.pos.distance_to(mouse_pos) <= self.size[0] and self.pos.distance_to(mouse_pos) <= self.size[1]:
                    self.color = (200,200,200)
                    return True
        else:
            self.color = (100,100,100)

        return False

    def update(self):
        pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))

class Map:
    def __init__(self,screen):
        self.screen = screen
        self.rows = 8
        self.cols = 8

    def update(self):
        w = self.screen.get_width()
        h = self.screen.get_height()
        for i in range(self.rows):
            for j in range(self.cols):
                x = w * i // self.rows
                y = h * j // self.cols
                tile_w = w * (i + 1) // self.rows - x
                tile_h = h * (j + 1) // self.cols - y
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, tile_w, tile_h), 1)
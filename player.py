import pygame
from settings import *
vector = pygame.math.Vector2
class Player:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = vector(((self.grid_pos.x*self.app.cell_width)+border_padding//2)+self.app.cell_width//2, ((self.grid_pos.y*self.app.cell_height)+border_padding//2)+self.app.cell_height//2)

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.app.screen, pacman_yellow, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width-5)


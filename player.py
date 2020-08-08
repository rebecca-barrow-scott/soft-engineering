import pygame
from settings import *
vector = pygame.math.Vector2
class Player:
    def __init__(self, app, pos):
        self.app = app
        self.grid_position = pos
        self.point_position = vector((border_padding//2 + self.grid_position.x * self.app.cell_width) + self.app.cell_width // 2,
                                     (border_padding//2 + self.grid_position.y * self.app.cell_height) + self.app.cell_height // 2)
        self.path = vector(1, 0)
        self.stored_path = None
        self.radius = self.app.cell_width // 2 - 3

    def update(self):
        # move the point position
        self.point_position += self.path
        if (int(self.point_position.x-self.radius) % self.app.cell_width) == 0:
            if self.path == vector(1, 0) or self.path == vector(-1, 0):
                if self.stored_path is not None:
                    self.path = self.stored_path

        if (int(self.point_position.y-self.radius) % self.app.cell_height) == 0:
            if self.path == vector(0, 1) or self.path == vector(0, -1):
                if self.stored_path is not None:
                    self.path = self.stored_path

        # move the grid position relative to the point position
        self.grid_position.x = (self.point_position.x - border_padding + self.app.cell_width//2) // self.app.cell_width + 1
        self.grid_position.y = (self.point_position.y - border_padding + self.app.cell_height//2) // self.app.cell_height + 1
        # move pacman to the other side of the screen
        if self.point_position.x <= -5:
            self.point_position.x = width
        if self.point_position.x >= width+5:
            self.point_position.x = -5

    def draw(self):
        pygame.draw.circle(self.app.screen,
                           pacman_yellow,
                           (int(self.point_position.x), int(self.point_position.y)),
                           (self.radius))
        #draw tracking rect
        pygame.draw.rect(self.app.screen, ghost_red, (self.grid_position[0] * self.app.cell_width + border_padding // 2,
                                                      self.grid_position[1] * self.app.cell_height + border_padding // 2,
                                                      self.app.cell_width, self.app.cell_height), 1 )

    def move(self, path):
        self.stored_path = path


import pygame
from settings import *
class Map:
    def __init__(self, app):
        self.app = app
        self.map = """wwwwwwwwwwwwwwwwwww
w........w........w
w.ww.www.w.www.ww.w
w.................w
w.ww.w.wwwww.w.ww.w
w....w...w...w....w
wwww.www.w.www.wwww
...w.w.......w.w...
wwww.w.wwbww.w.wwww
.......w...w.......
wwww.w.wwwww.w.wwww
...w.w.......w.w...
wwww.w.wwwww.w.wwww
w........w........w
w.ww.www.w.www.ww.w
w..w...........w..w
ww.w.w.wwwww.w.w.ww
w....w...w...w....w
w.wwwwww.w.wwwwww.w
w.................w
wwwwwwwwwwwwwwwwwww"""
        #self.tile = pygame.Rect(0, 0, self.app.cell_width, self.app.cell_height)


    def draw(self):
        map_lines = self.map.splitlines()
        for y, lines in enumerate(map_lines):
            for x, letter in enumerate(lines):
                if letter == 'w':
                    pygame.draw.rect(self.app.background, blue, (x*self.app.cell_width, y*self.app.cell_height, self.app.cell_width, self.app.cell_height))
                if letter == 'b':
                    pygame.draw.line(self.app.background, ghost_pink, (x*self.app.cell_width, (y+0.5)*self.app.cell_height), ((x+1)*self.app.cell_width, (y+0.5)*self.app.cell_height), 5)
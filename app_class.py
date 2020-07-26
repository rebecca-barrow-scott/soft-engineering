import pygame
import sys

from settings import *

pygame.init()
vector = pygame.math.Vector2

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'intro'
        self.cell_width = width//28
        self.cell_height = height//30

        self.load()

    def run(self):
        while self.running:
            if self.state == 'intro':
                self.intro_events()
                self.intro_update()
                self.intro_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(fps)
        pygame.quit()
        sys.exit()

    #-#-- HELPER FUNCTIONS --#-#
    def draw_text(self, text, screen, pos, font_size, color, font_name):
        font = pygame.font.SysFont(font_name, font_size)
        rend_text = font.render(text, False, color)
        text_size = rend_text.get_size()
        pos[0] = pos[0]-text_size[0]//2
        pos[1] = pos[1] - text_size[1] // 2
        screen.blit(rend_text, pos)

    def load(self):
        self.background = pygame.image.load('maze.png')
        self.background = pygame.transform.scale(self.background, (width, height))

    def draw_grid(self):
        for w in range(width//self.cell_width):
            pygame.draw.line(self.screen, ghost_orange, (w*width//self.cell_width, 0), (w*width//self.cell_width, height))
        for h in range(height//self.cell_height):
            pygame.draw.line(self.screen, ghost_orange, (0, h*height//self.cell_height), (width, h*height//self.cell_height))

    #-#-- STATE FUNCTIONS --#-#
    # INTRO
    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def intro_update(self): pass

    def intro_draw(self):
        self.screen.fill(black)
        self.draw_text('WELCOME TO PACMAN', self.screen, [width//2, height//2-97],intro_text_size_title, ghost_red, intro_font)
        self.draw_text('WELCOME TO PACMAN', self.screen, [width//2+2, height//2-100],intro_text_size_title, purple, intro_font)
        self.draw_text('WELCOME TO PACMAN', self.screen, [width//2, height//2-100],intro_text_size_title, pacman_yellow, intro_font)
        self.draw_text('PRESS SPACEBAR TO START', self.screen, [width//2+1, height//2-49],intro_text_size_subtitle, hot_pink, intro_font)
        self.draw_text('PRESS SPACEBAR TO START', self.screen, [width//2, height//2-50],intro_text_size_subtitle, ghost_pink, intro_font)
        self.draw_text('REBECCA BARROW-SCOTT', self.screen, [width//2, height-40],intro_text_size, ghost_cyan, intro_font)
        self.draw_text('3815 ICT SOFTWARE ENGINEERING', self.screen, [width//2, height-20],intro_text_size, blue, intro_font)
        pygame.display.update()

    # PLAYING
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                pass

    def playing_update(self):
        pass

    def playing_draw(self):
        self.screen.blit(self.background, (0, 0))
        self.draw_grid()
        pygame.display.update()
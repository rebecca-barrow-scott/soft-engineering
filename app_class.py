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

    def run(self):
        while self.running:
            if self.state == 'intro':
                self.intro_events()
                self.intro_update()
                self.intro_draw()
            self.clock.tick(fps)
        pygame.quit()
        sys.exit()

    def draw_text(self, text, screen, pos, font_size, color, font_name):
        font = pygame.font.SysFont(font_name, font_size)
        rend_text = font.render(text, False, color)
        text_size = rend_text.get_size()
        pos[0] = pos[0]-text_size[0]//2
        pos[1] = pos[1] - text_size[1] // 2
        screen.blit(rend_text, pos)

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def intro_update(self): pass

    def intro_draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_text('WELCOME TO PACMAN', self.screen, [width//2, height//2-97],intro_text_size_title, red, intro_font)
        self.draw_text('WELCOME TO PACMAN', self.screen, [width//2+2, height//2-100],intro_text_size_title, purple, intro_font)
        self.draw_text('WELCOME TO PACMAN', self.screen, [width//2, height//2-100],intro_text_size_title, yellow, intro_font)
        self.draw_text('PRESS SPACEBAR TO START', self.screen, [width//2+1, height//2-49],intro_text_size_subtitle, hot_pink, intro_font)
        self.draw_text('PRESS SPACEBAR TO START', self.screen, [width//2, height//2-50],intro_text_size_subtitle, pink, intro_font)
        self.draw_text('REBECCA BARROW-SCOTT', self.screen, [width//2, height-40],intro_text_size, cyan, intro_font)
        self.draw_text('3815 ICT SOFTWARE ENGINEERING', self.screen, [width//2, height-20],intro_text_size, blue, intro_font)

        pygame.display.update()

import pygame, random, sys
import pygame as pg
import cv2 
import numpy as np 
from pygame import mixer
pygame.init()
pygame.font.init()
pygame.mixer.init()

#VARIABLES
WIDTH, HEIGHT = 1280, 720

#SCREEN
CANVAS = pygame.Surface((WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load('dice.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Dungeon Crawling Demo")

#IMAGES
IMG = pygame.image.load('bck.jpg')
IMG = pygame.transform.scale(IMG, (WIDTH, HEIGHT))
RECT = IMG.get_rect(center=(WIDTH / 2, HEIGHT / 2))
SCREENBG = pygame.image.load('screen.png')
SCREENBG = pygame.transform.scale(SCREENBG, (WIDTH, HEIGHT))
op = pygame.image.load('op.png')
alpha = 64

#CHOICEBOX
cbox1 = pygame.image.load('box.png')
cbox1 = pygame.transform.scale(cbox1, (500, 500))

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (190, 190, 190)



#GAME CONTENT
FONT = pg.font.SysFont('Comic Sans MS', 32)
# Default button images/pygame.Surfaces.
IMAGE_NORMAL = pg.Surface((1, 1))
IMAGE_NORMAL.fill(pg.Color('dodgerblue1'))
IMAGE_HOVER = pg.Surface((100, 32))
IMAGE_HOVER.fill(pg.Color('lightskyblue'))
IMAGE_DOWN = pg.Surface((100, 32))
IMAGE_DOWN.fill(pg.Color('aquamarine1'))


# Button is a sprite subclass, that means it can be added to a sprite group.
# You can draw and update all sprites in a group by
# calling `group.update()` and `group.draw(screen)`.
class Button(pg.sprite.Sprite):

    def __init__(self, x, y, width, height, callback,
                 font=FONT, text='', text_color=(0, 0, 0),
                 image_normal=IMAGE_NORMAL, image_hover=IMAGE_HOVER,
                 image_down=IMAGE_DOWN):
        super().__init__()
        # Scale the images to the desired size (doesn't modify the originals).
        self.image_normal = pg.transform.scale(image_normal, (width, height))
        self.image_hover = pg.transform.scale(image_hover, (width, height))
        self.image_down = pg.transform.scale(image_down, (width, height))

        self.image = self.image_normal  # The currently active image.
        self.rect = self.image.get_rect(topleft=(x, y))
        # To center the text rect.
        image_center = self.image.get_rect().center
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=image_center)
        # Blit the text onto the images.
        for image in (self.image_normal, self.image_hover, self.image_down):
            image.blit(text_surf, text_rect)

        # This function will be called when the button gets pressed.
        self.callback = callback
        self.button_down = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.image = self.image_down
                self.button_down = True
        elif event.type == pg.MOUSEBUTTONUP:
            # If the rect collides with the mouse pos.
            if self.rect.collidepoint(event.pos) and self.button_down:
                self.callback()  # Call the function.
                self.image = self.image_hover
            self.button_down = False
        elif event.type == pg.MOUSEMOTION:
            collided = self.rect.collidepoint(event.pos)
            if collided and not self.button_down:
                self.image = self.image_hover
            elif not collided:
                self.image = self.image_normal

class Game:

    def __init__(self, screen):
        self.done = False
        self.clock = pg.time.Clock()
        self.screen = screen
        # Contains all sprites. Also put the button sprites into a
        # separate group in your own game.
        self.all_sprites = pg.sprite.Group()
        self.number = 0
        # Create the button instances. You can pass your own images here.
        self.start_button = Button(
            320, 70, 170, 65, self.start_game,
            FONT, 'Start', (255, 255, 255),
            IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # If you don't pass images, the default images will be used.
        self.quit_button = Button(
            320, 240, 170, 65, self.quit_game,
            FONT, 'Quit', (255, 255, 255))
        # Add the button sprites to the sprite group.
        self.all_sprites.add(self.start_button, self.quit_button)

    def openingT(self):
        WIN.blit(op, (WIDTH / 200, HEIGHT / 200))

    def cbox(self):
        WIN.blit(cbox1, (120, 80))

    def background(self):
        IMG.set_alpha(alpha)
        CANVAS.fill(BLACK)
        CANVAS.blit(IMG, RECT)
        WIN.blit(CANVAS, (0,0,0,0))
        CANVAS.blit(IMG, (WIDTH, HEIGHT))

    def redrawWindow(self):
        WIN.fill((WHITE))

    def fade(self, WIDTH, HEIGHT):
        fade = pygame.Surface((WIDTH, HEIGHT))
        fade.fill((BLACK))
        for alpha in range(0, 50):
            fade.set_alpha(alpha)
            self.redrawWindow()
            WIN.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(3)

    def chapterOne(self):
        self.PASS = True
        while self.PASS:
            self.background()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            pygame.display.update()

    def OPENING(self): 
        self.INTRO = True
        while self.INTRO:
            self.openingT()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.redrawWindow()
                    self.fade(WIDTH, HEIGHT)
                    self.chapterOne()
                    self.INTRO = False
            pygame.display.update()

    def SCREENOP(self):
        self.SCREEN = True
        while self.SCREEN:
            WIN.blit(SCREENBG, (WIDTH / 1500, HEIGHT / 1000))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.OPENING()
                    self.SCREEN = False
            pygame.display.update()

    def quit_game(self):
        """Callback method to quit the game."""
        self.done = True

    def start_game(self):
        """Callback method to increment the number."""
        self.SCREENOP()
        pg.display.flip()

    def run(self):
        while not self.done:
            self.dt = self.clock.tick(30) / 1000
            self.handle_events()
            self.run_logic()
            self.draw()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            for button in self.all_sprites:
                button.handle_event(event)

    def run_logic(self):
        self.all_sprites.update(self.dt)

    def draw(self):
        self.screen.blit(SCREENBG, (WIDTH / 1500, HEIGHT / 1000))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

if __name__ == '__main__':
    pg.init()
    Game(WIN).run()
    pg.quit()
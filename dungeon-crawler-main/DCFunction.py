import pygame, random, sys
import keyboard
from pygame.locals import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

#VARIABLES
WIDTH, HEIGHT = 1280, 720
RUN = True

#TITLESCREEN
CANVAS = pygame.Surface((WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
ICON = pygame.image.load('dice.png')
pygame.display.set_icon(ICON)
pygame.display.set_caption("Dungeon Crawling Demo")

#IMAGES
IMG = pygame.image.load('bck.jpg')
IMG = pygame.transform.scale(IMG, (WIDTH, HEIGHT))

RECT = IMG.get_rect(center=(WIDTH / 2, HEIGHT / 2))

SCREENBG = pygame.image.load('screen.png')
SCREENBG = pygame.transform.scale(SCREENBG, (WIDTH, HEIGHT))

FONT = pygame.font.Font('./Font/Montserrat-Medium.otf', 24)
op = pygame.image.load('op.png')
alpha = 64
MAX_WIDTH = 1200
clock = pygame.time.Clock()

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (190, 190, 190)


#FUNCTION
def openingT():
    WIN.blit(op, (WIDTH / 1500, HEIGHT / 1500))

# SEMI-TRANSPARENT BACKGROUND
def background():
    IMG.set_alpha(alpha)
    CANVAS.fill(BLACK)
    CANVAS.blit(IMG, RECT)
    WIN.blit(CANVAS, (0,0,0,0))
    CANVAS.blit(IMG, (WIDTH, HEIGHT))

# SIMPLE FADE OUT TRANSITION
def fade(WIDTH, HEIGHT):
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((WHITE))
    for alpha in range(0, 100):
        fade.set_alpha(alpha)
        WIN.blit(fade, (0,0))
        pygame.event.pump()
        pygame.display.update()
        pygame.time.delay(50)

def CHAPTERONE():
    while True:
        background()
        if QUIT_BUTTON_GAME.draw():
            sys.exit()

        if MOVE_BUTTON.draw() or keyboard.is_pressed('Space'):
            pygame.time.delay(200)
            print("Moved.")

        if CHECKINVENTORY_BUTTON.draw():
            print ("Checked Inventory.")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        
def OPENING(): 
    while True:
        WIN.blit(SCREENBG, (WIDTH / 1500, HEIGHT / 1500))

        if START_BUTTON.draw():
            CHAPTERONE()
        
        if QUIT_BUTTON.draw():
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

def display_text_animation(string):
    FONT = pygame.font.Font('./Font/Montserrat-Light.otf', 88)
    text = ''

    for i in range(len(string)):
        WIN.fill(WHITE)
        text += string[i]
        text_surface = FONT.render(text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (WIDTH/2, HEIGHT/2)
        WIN.blit(text_surface, text_rect)
        if pygame.mouse.get_pressed()[0] == 1 or keyboard.is_pressed('Space'):
            main()
        
        pygame.display.update()
        pygame.event.pump()
        pygame.time.wait(100)



#BUTTON
IMAGE_START = pygame.image.load('START.png')
IMAGE_QUIT = pygame.image.load('QUIT.png')
IMAGE_MOVE = pygame.image.load('MOVE.png')
IMAGE_CHECKINVENTORY = pygame.image.load('CHECKINVENTORY.png')


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False


    def draw(self):
        START = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                START = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        WIN.blit(self.image, (self.rect.x, self.rect.y))
        
        return START

#BUTTON
START_BUTTON = Button(100, 200, IMAGE_START, 0.9)
QUIT_BUTTON = Button(100, 400, IMAGE_QUIT, 0.9)
QUIT_BUTTON_GAME = Button(900, 600, IMAGE_QUIT, 0.9)
MOVE_BUTTON = Button(100, 600, IMAGE_MOVE, 0.9)
CHECKINVENTORY_BUTTON = Button(500, 600, IMAGE_CHECKINVENTORY, 0.9)

#RUN
def main():
    while True:
        OPENING()

display_text_animation("The battle has just begun!")
fade(WIDTH, HEIGHT)
main()
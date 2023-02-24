import pygame, random, sys
import narrative
import textoverflow

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
#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (190, 190, 190)

#####
def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh
#####

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
"""def fade(WIDTH, HEIGHT):
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((BLACK))
    for alpha in range(0, 150):
        fade.set_alpha(alpha)
        WIN.fill((WHITE))
        WIN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)"""

ONE = "It was with you I realized that true happiness lie upon the clarity of the upheaving grief we all overcome."
def CHAPTERONE():
    PASS = True
    while PASS:
        background()
        renderTextCenteredAt(ONE, FONT, WHITE, HEIGHT / 1.15, WIDTH / 25, WIN, MAX_WIDTH)
        if QUIT_BUTTON_GAME.draw():
            sys.exit()

        if MOVE_BUTTON.draw():
            print ("Moved.")

        if CHECKINVENTORY_BUTTON.draw():
            print ("Checked Inventory.")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
        pygame.display.update()
        
def OPENING(): 
    INTRO = True
    while INTRO:
        openingT()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    CHAPTERONE()
        pygame.display.update()

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
                self.clicked = True
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
while RUN:
    WIN.blit(SCREENBG, (WIDTH / 1500, HEIGHT / 1500))

    if START_BUTTON.draw():
        OPENING()
    
    if QUIT_BUTTON.draw():
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    pygame.display.update()
                




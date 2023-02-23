import pygame, random
import cv2 
import numpy as np 
from pygame import mixer
pygame.init()
pygame.font.init()
pygame.mixer.init()

#variables
WIDTH, HEIGHT = 1280, 700
PASS = True
INTRO = True
CANVAS = pygame.Surface((WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load('dice.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Dungeon Crawling Demo")
IMG = pygame.image.load('bck.jpg')
IMG = pygame.transform.scale(IMG, (WIDTH, HEIGHT))
RECT = IMG.get_rect(center=(WIDTH / 2, HEIGHT / 2))

#full-screen dialogue box
alpha = 64

#choice box variable
cbox1 = pygame.image.load('box.png')
cbox1 = pygame.transform.scale(cbox1, (500, 500))

cx = 120
cy = 80

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (190, 190, 190)

#GAME CONTENTS

#OPENINGP
font = pygame.font.Font('Montserrat-Bold.otf', 25) #PARAGRAPH
font1 = pygame.font.Font('Montserrat-Bold.otf', 15) #HEADER
text0 = font1.render('A MESSAGE SENT FROM THE HIGHER UPS', True, WHITE)
text = font.render('You have a job to do, Hired Assassin.', True, WHITE)
text1 = font.render('The Holy Grail has been sighted inside the deepest parts of the Arkan Dungeon.', True, WHITE)
text2 = font.render('We have provided a useful map for you outlining many paths in and out.', True, WHITE) 
text3 = font.render('While their guards are down, sneak inside and acquire it immediately.', True, WHITE)
text4 = font.render('—N', True, WHITE)
text5 = font1.render('ENTER TO START THE GAME', True, WHITE)

#CHAPTERONE
partf = pygame.font.Font('Montserrat-Bold.otf', 15) #PARAGRAPH
partfh = pygame.font.Font('Montserrat-Bold.otf', 25) #HEADER
part = partf.render('You wake up, mesmerized by the current scenery around you. You tried to remember... and you finally did.', True, WHITE)
part1 = partf.render('After you sneak through the entrance with precise movement, you were able to secure a path to the staircase leading to the depths of the dungeon.', True, WHITE)
part2 = partf.render('However, and without knowing yourself, the stairs leading down collapsed. You fell down. Luckily, you are still alive. Very miraculous.', True, WHITE) 
part3 = partf.render('You seem to have lost your equipments, but the map you had is still in your hand, grasped tightly.', True, WHITE)
part4 = partf.render('As you stood, you finally realized how you are still alive. It was a layer of fabrics that stacked during your fall.', True, WHITE)
part5 = partf.render('Remembering the act of graciousness of god, you move on to finish your job.', True, WHITE)
part6 = partf.render('PICK YOUR ACTIONS:', True, WHITE)

#functions

def cbox():
    WIN.blit(cbox1, (cx, cy))

def background():
    IMG.set_alpha(alpha)
    CANVAS.fill(BLACK)
    CANVAS.blit(IMG, RECT)
    WIN.blit(CANVAS, (0,0,0,0))
    CANVAS.blit(IMG, (WIDTH, HEIGHT))

def fade(WIDTH, HEIGHT):
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((BLACK))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        redrawWindow()
        WIN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)

def redrawWindow():
    WIN.fill((WHITE))
#CHOICES
def isPressed():
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True

def openingP():
    WIN.blit(text, (WIDTH / 18, HEIGHT / 5))
    WIN.blit(text1, (WIDTH / 18, HEIGHT / 3.8))
    WIN.blit(text2, (WIDTH / 18, HEIGHT / 3))
    WIN.blit(text3, (WIDTH / 18, HEIGHT / 2.5))
    WIN.blit(text4, (WIDTH / 1.2, HEIGHT / 1.7))
    WIN.blit(text5, (WIDTH / 1.3, HEIGHT / 1.1))
    WIN.blit(text0, (WIDTH / 21, HEIGHT / 8))

def chapterOne():
    WIN.blit(part, (WIDTH / 21, HEIGHT / 5))
    WIN.blit(part1, (WIDTH / 21, HEIGHT / 3.8))
    WIN.blit(part2, (WIDTH / 21, HEIGHT / 3))
    WIN.blit(part3, (WIDTH / 21, HEIGHT / 2.5))
    WIN.blit(part4, (WIDTH / 21, HEIGHT / 1.7))
    WIN.blit(part5, (WIDTH / 21, HEIGHT / 1.1))
    WIN.blit(part6, (WIDTH / 21, HEIGHT / 8))
# if fade is finished with its text, then the while-loop starts! Text first, and mouse interaction
# leads to change in scenery (dungeon background and the dialogue box for narrative)

#demo opening

while INTRO:
    openingP()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            INTRO = False
            PASS = False     
        if event.type == pygame.MOUSEBUTTONDOWN:
            redrawWindow()
            fade(WIDTH, HEIGHT)
            INTRO = False
    pygame.display.update()

#where everything starts
while PASS:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PASS = False
        #if Continue.isPressed(event):
            #Menu()
            
    background()
    #cbox()
    pygame.display.update()
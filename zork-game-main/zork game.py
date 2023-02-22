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

#INTRO dialogue
font = pygame.font.Font('Montserrat-Bold.otf', 25)
font1 = pygame.font.Font('Montserrat-Bold.otf', 15)
text0 = font1.render('A MESSAGE SENT FROM THE HIGHER UPS', True, WHITE)
text = font.render('You have a job to do, Hired Assassin.', True, WHITE)
text1 = font.render('The Holy Grail has been sighted inside the deepest parts of the Arkan Dungeon.', True, WHITE)
text2 = font.render('We have provided a useful map for you outlining many paths in and out.', True, WHITE) 
text3 = font.render('While their guards are down, sneak inside and acquire it immediately.', True, WHITE)
text4 = font.render('—N', True, WHITE)
text5 = font1.render('ENTER TO START THE GAME', True, WHITE)

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

def narrative():
    WIN.blit(text, (WIDTH / 18, HEIGHT / 5))
    WIN.blit(text1, (WIDTH / 18, HEIGHT / 3.8))
    WIN.blit(text2, (WIDTH / 18, HEIGHT / 3))
    WIN.blit(text3, (WIDTH / 18, HEIGHT / 2.5))
    WIN.blit(text4, (WIDTH / 1.2, HEIGHT / 1.7))
    WIN.blit(text5, (WIDTH / 1.3, HEIGHT / 1.1))
    WIN.blit(text0, (WIDTH / 21, HEIGHT / 8))

# if fade is finished with its text, then the while-loop starts! Text first, and mouse interaction
# leads to change in scenery (dungeon background and the dialogue box for narrative)

#demo opening

while INTRO:
    narrative()
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
            
    background()
    #cbox()
    pygame.display.update()
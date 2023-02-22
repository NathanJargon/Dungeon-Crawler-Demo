import pygame
import sys
pygame.init()

screenSizeX = 1080
screenSizeY = 720
screenSize = (screenSizeX,screenSizeY)
screen = pygame.display.set_mode(screenSize,0)
pygame.display.set_caption("Test Functions")

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
MAGENTA = (139,0,139)

def horCenter(font, size, text, colour, y):
    if shadow == True:
        fontTitle = pygame.font.SysFont(font, size)
        textTitle = fontTitle.render(text, True, colour)
        textWidth = textTitle.get_width()
        screen.blit(textTitle, (screenSizeX/2 - textWidth/2, y))

def verCenter(font, size, text, colour, x):
    fontTitle = pygame.font.SysFont(font, size)
    textTitle = fontTitle.render(text, True, colour)
    textHeight = textTitle.get_height()
    screen.blit(textTitle, (x, screenSizeY/2 - textHeight/2))

def cenCenter(font, size, text, colour):
    fontTitle = pygame.font.SysFont(font, size)
    textTitle = fontTitle.render(text, True, colour)
    textHeight = textTitle.get_height()
    textWidth = textTitle.get_width()
    screen.blit(textTitle, (screenSizeX/2 - textWidth/2, screenSizeY/2 - textHeight/2))   


pygame.display.update()

go = True
while go:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            go = False


    screen.fill(WHITE)
    horCenter("Comic Sans MS", 40, "Text1", MAGENTA, 100)
    verCenter("Georgia", 10, "Tex2", GREEN, 500)
    cenCenter("Impact", 50, "Text3", RED)
    verCenter("Verdana", 60, "89274", BLACK, 50)
    pygame.display.update()

pygame.quit()
sys.exit()
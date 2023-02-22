import pygame, sys
# Window size
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 700
screenColor = (30, 30, 30)

pygame.init()
pygame.display.set_caption("4160 Pong")
surface = pygame.display.set_mode(SCREEN_SIZE)

def createScreen():
    surface.fill(screenColor)

def updateScreen(rectColor, paddle1, paddle2, ball):
    pygame.draw.rect(surface, rectColor, paddle1)
    pygame.draw.rect(surface, rectColor, paddle2)
    pygame.draw.rect(surface, rectColor, ball)
    pygame.display.update()
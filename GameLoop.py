import pygame, sys, Pong, EventHandler, View, time

clock = pygame.time.Clock()

# Game loop
while True:
    EventHandler.findEvent()
    
    View.createScreen()
    ticks = clock.tick(50)
    deltaTime = ticks / 5000.0

    Pong.move_paddles(Pong.paddle1, Pong.paddle2, deltaTime)
    Pong.gameBall.move_ball(deltaTime)

    View.updateScreen(Pong.rectColor, Pong.paddle1, Pong.paddle2, Pong.gameBall.model)
import pygame, sys, math
import View

# Bounds
boundsRect = pygame.Rect(0, 0, 1000, 700)
lowerWall = pygame.Rect(0, 693, 1000, 7)
upperWall = pygame.Rect(0, 0, 1000, 7)
leftWall = pygame.Rect(0, 0, 1, 700)
rightWall = pygame.Rect(999, 0, 1, 700)

# Paddles
rectColor = (0, 255, 0)
paddleSize = paddleWidth, paddleHeight = 7, 70
paddle1Pos = paddle1X, paddle1Y = 0, 415
paddle2Pos = paddle2X, paddle2Y = 993, 415
paddle1 = pygame.Rect(paddle1X, paddle1Y, paddleWidth, paddleHeight)
paddle2 = pygame.Rect(paddle2X, paddle2Y, paddleWidth, paddleHeight)
paddleSpeed = 1000

def move_paddles(paddle1, paddle2, deltaTime):
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP]):
        paddle2.move_ip(0, -paddleSpeed * deltaTime)
    elif (keys[pygame.K_DOWN]):
        paddle2.move_ip(0, paddleSpeed * deltaTime)
    if (keys[pygame.K_w]):
        paddle1.move_ip(0, -paddleSpeed * deltaTime)
    elif (keys[pygame.K_s]):
        paddle1.move_ip(0, paddleSpeed * deltaTime)
    paddle1.clamp_ip(boundsRect)
    paddle2.clamp_ip(boundsRect)
    
# Ball
class Ball:
    def __init__(self):
        self.size = ballWidth, ballHeight = 7, 7
        self.pos = ballX, ballY = 443, 443
        self.model = pygame.Rect(ballX, ballY, ballWidth, ballHeight)
        self.down = True
        self.right = True
        self.speed = 750
        self.hits = 0

    def check_collision(self):

        ballLowerCollide = pygame.Rect.colliderect(self.model, lowerWall)
        if (ballLowerCollide): self.down = False
        ballUpperCollide = pygame.Rect.colliderect(self.model, upperWall)
        if (ballUpperCollide): self.down = True
        ballRightPaddleCollide = pygame.Rect.colliderect(self.model, paddle2)
        if (ballRightPaddleCollide): 
            self.right = False
            self.hits += 1
        ballLeftPaddleCollide = pygame.Rect.colliderect(self.model, paddle1)
        if (ballLeftPaddleCollide): 
            self.right = True
            self.hits += 1

        self.speed = min(750 + (100 * self.hits), 2000)

        ballRightWallCollide = pygame.Rect.colliderect(self.model, rightWall)
        if (ballRightWallCollide): 
            self.speed = 0
            return
        ballLeftWallCollide = pygame.Rect.colliderect(self.model, leftWall)
        if (ballLeftWallCollide): 
            self.speed = 0
            return

    def move_ball(self, deltaTime):

        self.check_collision()
        deltaSpeed = self.speed * deltaTime
        if (self.right and self.down):
            self.model.move_ip(deltaSpeed, deltaSpeed)
        elif (self.right and not self.down): 
            self.model.move_ip(deltaSpeed, -deltaSpeed)
        elif (not self.right and self.down):
            self.model.move_ip(-deltaSpeed, deltaSpeed)
        elif (not self.right and not self.down):
            self.model.move_ip(-deltaSpeed, -deltaSpeed)
        self.model.clamp_ip(boundsRect)
    
    

gameBall = Ball()


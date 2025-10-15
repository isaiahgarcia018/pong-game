import pygame
import sys


pygame.init()
hit_sound = pygame.mixer.Sound("assets/ballsmackracket.wav")

width, height = 800, 600
WINDOW = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

#Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
PADDLE_SPEED = 7 

BALL_SIZE = 20 
BALL_SPEED_X, BALL_SPEED_Y = 6,7 

LEFT_PADDLE = pygame.Rect(30, height // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
RIGHT_PADDLE = pygame.Rect(width - 30 - PADDLE_WIDTH, height // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(width // 2 - BALL_SIZE // 2, height // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE )


#MAIN LOOP FOR GAME
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
            
        keys = pygame.key.get_pressed()
            
   
    if keys [pygame.K_w] and LEFT_PADDLE.top > 0:
        LEFT_PADDLE.y -= PADDLE_SPEED
    if keys[pygame.K_s] and LEFT_PADDLE.bottom < height:
        LEFT_PADDLE.y += PADDLE_SPEED
                    
           
    if keys [pygame.K_UP] and RIGHT_PADDLE.top > 0:
        RIGHT_PADDLE.y -= PADDLE_SPEED
    if keys [pygame.K_DOWN] and RIGHT_PADDLE.bottom < height:
        RIGHT_PADDLE.y += PADDLE_SPEED
            
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y
                    
    if ball.top <= 0 or ball.bottom >= height:
        BALL_SPEED_Y *= -1
                        
    if ball.colliderect(LEFT_PADDLE) or ball.colliderect(RIGHT_PADDLE):
        BALL_SPEED_X *= -1
        
        hit_sound.play()
           
        
                        
    if ball.left <= 0 or ball.right >= width:
                            
        ball.x = width // 2 - BALL_SIZE // 2
        ball.y = height // 2 - BALL_SIZE // 2
        BALL_SPEED_X *= -1
        
                            
    WINDOW.fill(BLACK)
    pygame.draw.rect(WINDOW, BLUE, LEFT_PADDLE)
    pygame.draw.rect(WINDOW, BLUE, RIGHT_PADDLE)
    pygame.draw.ellipse(WINDOW, BLUE, ball)
    pygame.draw.aaline(WINDOW, BLUE, (width // 2, 0), (width // 2, height))
                                   
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
        
        
                
                            
                    
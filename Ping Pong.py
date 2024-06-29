import pygame
import sys
import random
from datetime import date
print("Today's date:", date.today())
print("Kaleb Masterson")
# I state the code submitted is my own work.


def main_menu():
    while True:
        screen.fill((52, 78, 91)) #fills the screen with blue
        draw_text("PING PONG", font, text_col, 340, 250) #displays PING PONG
        draw_text("Press SPACE to start", font, text_col, 250, 350) #displays SPACE TO START
        draw_text("Press ESC to quit", font, text_col, 270, 450) #displays ESC TO QUIT
        pygame.display.flip()
        
        # allows the space and ESC commands to work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #defines closing the game
                sys.exit() #defines closing the program
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True  # Start the game
                elif event.key == pygame.K_ESCAPE: #closes the game
                    pygame.quit()  
                    sys.exit()


#allows draw_text to have a spefic font and size allows places it on the sceen on the left
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    text_width, text_height = font.size(text)
    screen.blit(img, (x - text_width // 2, y - text_height // 2))



#allows the ball to move around the screen
def ball_animation():
    global ball_speed_x
    ball.x += ball_speed_x
    global ball_speed_y
    ball.y += ball_speed_y
    

    #tells the ball when it hits the top
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    #tells the ball when it hits the left or right
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
        
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    #Allows your pong paddle to move
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
     
def opponent_animation():
    #Allows the opponents pong paddle to move
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart():
    #resests the ball and put it in a random direction
    global ball_speed_x
    global ball_speed_y

    ball.center = (screen_width/2, screen_height/2)    
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))
    
#sets up pygame by running all start up modudles
pygame.init()
clock = pygame.time.Clock()

#Doing the setup for the main window on the game.
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
#Gives the window a title
pygame.display.set_caption("PING PONG")


#Creates the empty rectangles for the ball player and opponent
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 -15,30,30) #sets the ball to the middles of the screen
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140) #sets the player to the middle left of the screen
opponent = pygame.Rect(10,screen_height/2 - 70, 10, 140) #sets the opponent to the middle right of the screen


#stating the color codes
bg_color = pygame.Color('gray12')
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7
#Sets what type of font I want
font = pygame.font.SysFont("arialblack", 40)
score_font = pygame.font.SysFont("arialblack", 36)
score_text_col = (255, 255, 255)


#sets text color
text_col = (255,255,255)

if main_menu():
        #Updates the game
    while True:
    #checks if the user has clicked the close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #quit = closing the window
                pygame.quit() #closes the window
                sys.exit() #closes the program
                #allows you to move your player down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed +=7
                if event.key == pygame.K_UP:
                    player_speed -=7
                #allows you to move your player up
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -=7
                if event.key == pygame.K_DOWN:
                    player_speed +=7
                
                



    



        #allows the ball to move
        ball_animation()  
        #allows your player to move
        player.y += player_speed
        #your paddle to move
        player_animation()
        #allows the opponents paddle to move
        opponent_animation()
    


    

        #fills the screen with gray12
        screen.fill(bg_color)
        #sets the players to light grey
        pygame.draw.rect(screen,light_grey, player)
        pygame.draw.rect(screen,light_grey, opponent)
        #sets the ball to light greay and makes it a ball by stating "ellipse"
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (screen_width/2,0),(screen_width/2,screen_height))


        #draws a picutre in the loop
        pygame.display.flip()
        #lmits how fast the loop runs 
        # "60 times a second"
        clock.tick(60)






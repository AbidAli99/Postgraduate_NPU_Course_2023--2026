## A 2D Snake Game using Pygame module

##Imports

from pygame.locals import *
from pygame import mixer
import pygame
import random

##Initialize..

pygame.init()
Win_Size = [800,500]
iconPath = 'images/icon.png'
icon = pygame.image.load(iconPath)
Display = pygame.display.set_mode(Win_Size)
pygame.display.set_caption("Snake_Abid Ali_2023280099")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

##Images...

startScreenPath = 'images/start.png'
ApplePath = 'images/Apple.png'
pausedPath = 'images/pause.png'

startScreen = pygame.image.load(startScreenPath)
Apple = pygame.image.load(ApplePath)
paused = pygame.image.load(pausedPath)

##Colors..

red = [254,5,0]
green = [192,255,24]
blue = [17,29,94]
black = [0,0,0]
white = [255,255,255]
orange = [243,113,33]


## Sounds...

mixer.pre_init(44100, -16, 2, 512)

gameMusicPath = 'sounds/GameMusic.mp3'
gameOverPath = 'sounds/GameOver.mp3'
eatApplePath = 'sounds/eat_apple.wav'

mixer.music.load(gameMusicPath)
gameover_sound = mixer.Sound(gameOverPath)
eat_apple_sound = mixer.Sound(eatApplePath)


##Highest Score...

HS = 0

##Font Object...

font = pygame.font.SysFont("comicsansms", 30)

# pygame.draw.rect(): This function is used to draw a rectangle.
# It takes the surface, color, and pygame Rect object as an input parameter and draws a rectangle on the surface.
def snake(block_width, block_height, SnakeList):
    head_image = pygame.image.load('images/snake_head.png')  # Load the image of the snake's head
    for i, XnY in enumerate(SnakeList):
        if i == len(SnakeList) - 1:  # If it's the last segment, draw the head
            Display.blit(head_image, (XnY[0], XnY[1]))
        else:  # Otherwise, draw the body segments
            pygame.draw.rect(Display, green, (XnY[0], XnY[1], block_width, block_height))



def text_object(text,color):
    text_area = font.render(text, True, color)
    return text_area , text_area.get_rect()

def text(msg,color):
    surface , textRect = text_object(msg, color)
    textRect.center = (Win_Size[0]/2),(Win_Size[1]/2)
    Display.blit(surface, textRect)


##Pause function...

def Pause_Screen():
    Pause = True
    mixer.music.fadeout(3000)
    while Pause:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_s:
                    mixer.music.play(-1)
                    Pause = False

                if event.key == K_q:
                    pygame.quit()
                    quit()


        Display.blit(paused,[0,0])
        pygame.display.update()
        clock.tick(5)

def Start_Screen():
    StartLoop = True

    while StartLoop == True:
        Display.fill(white)
        Display.blit(startScreen, [0,0])


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_s:
                    StartLoop = False

                if event.key == K_q:
                    pygame.quit()
                    quit()


def Game_Loop():

    ##Snake_Object
    SnakeList = []
    SnakeLength = 3


    pos_x = Win_Size[0]/2
    pos_y = Win_Size[1]/2
    pos_x_change = 0
    pos_y_change = 0
    snake_width = 10
    snake_height = 10
    snake_step = 15

    ##Apple_Object

    apple_width = 20
    apple_height = 20
    randApple_x = round(random.randrange(0,Win_Size[0]-apple_width))
    randApple_y = round(random.randrange(0,Win_Size[1]-apple_height))

    ##Game_setting
    Game_Exit = False
    Game_Over = False
    Game_Update = True
    #Snake speed control
    Fps = 10

    #The music repeats indefinitely if this argument is set to -1
    mixer.music.play(-1)
    #get the music volume
    #Returns the current volume for the mixer. The value will be between 0.0 and 1.0.

    mixer.music.set_volume(0.9)


    while not Game_Exit:
        global HS
        #Giving scores bassed on snake length
        score = (SnakeLength-3)

        if score > HS:
            HS = score

        while Game_Over == True:
            Display.fill(black)
            gameover_sound.set_volume(0.1)
            gameover_sound.play()

            text("GAME OVER! HIGHEST SCORE : {}".format(str(HS)), white)
            pygame.display.update()

            #Pygame will register all events from the user into an event queue which can be received with the code pygame. event. get() .
            for event in pygame.event.get():
                if event.type == QUIT:
                    Game_Exit = True
                    Game_Over = False
                if event.type == KEYDOWN:
                    if event.key == K_s:
                        mixer.music.play(-1)
                        gameover_sound.fadeout(100)
                        Game_Loop()
                    if event.key == K_q:
                        Game_Exit = True
                        Game_Over = False

        #While Playing Game
        for event in pygame.event.get():
            if event.type == QUIT:
                mixer.music.fadeout(100)
                Game_Exit = True

            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    pos_x_change = -snake_step
                    pos_y_change = 0
                if event.key == K_RIGHT or event.key == ord('d'):
                    pos_x_change = snake_step
                    pos_y_change = 0
                if event.key == K_UP or event.key == ord('w'):
                    pos_y_change = -snake_step
                    pos_x_change = 0
                if event.key == K_DOWN or event.key == ord('s'):
                    pos_y_change = snake_step
                    pos_x_change = 0

                if event.key == K_p:
                    Pause_Screen()

        ## Wall collision...
        if pos_x < 0 or pos_x > Win_Size[0] or pos_y < 0 or pos_y > Win_Size[1]:
            mixer.music.fadeout(1000)
            Game_Over = True

        ## Snake Collision with Apple...
        if pos_x > randApple_x and pos_x < randApple_x + apple_width or pos_x + snake_width > randApple_x and pos_x + snake_width < randApple_x + apple_width:
            if pos_y > randApple_y and pos_y < randApple_y + apple_height or pos_y + snake_height > randApple_y and pos_y + snake_height < randApple_y + apple_height:
                randApple_x = round(random.randrange(0,Win_Size[0]-apple_width))
                randApple_y = round(random.randrange(0,Win_Size[1]-apple_height))
                SnakeLength +=1
                eat_apple_sound.play()  # Playing the sound effect when the snake eats the apple

        pos_x += pos_x_change
        pos_y += pos_y_change

        ##Canvas

        Display.fill(blue)

        ## Apple Object...

        #surface.blit() function draws a source Surface onto this Surface
        Display.blit(Apple,[randApple_x,randApple_y])
        SnakeHead = []
        SnakeHead.append(pos_x)
        SnakeHead.append(pos_y)
        SnakeList.append(SnakeHead)


        if len(SnakeList) > SnakeLength:
            del SnakeList[0]

        ## Self collision...
        for eachSegment in SnakeList[:-3]:
            if eachSegment == SnakeHead:
                mixer.music.fadeout(1000)
                Game_Over = True

        ## Snake Object...
        snake(snake_width,snake_height,SnakeList)

        ## Score Board...
        if (SnakeLength-3) > 0:
            text(str(SnakeLength-3),white)

        #It allows only a portion of the screen to updated, instead of the entire area.
        pygame.display.update()
        #clock.tick(Fps) means that for every second at most 40 frames should pass.
        clock.tick(Fps)

    pygame.quit()
    quit()


## Game call...
Start_Screen()

## Looping the game to start the next round
Game_Loop()

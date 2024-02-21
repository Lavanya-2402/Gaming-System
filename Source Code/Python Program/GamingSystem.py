import pygame
from pygame.locals import *
import sys
import random

FPS = 32
SCREEN_WIDTH = 1333
SCREEN_HEIGHT =750
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
TARGET = ''
SCALE = ''
PLAYER_1Name = ''
PLAYER_2Name = ''
PLAYER_1=""
PLAYER_2=""
PLAYER1NUM = 0
PLAYER2NUM = 0
TARGET1 = 0
SCALE1 = 0
MODE = 0
inp_x = 600
inp_y = 420
GAME_SPRITES = {}
GAME_SOUNDS = {}
BACKGROUND = pygame.image.load('sprites/background.jpg')
clock = pygame.time.Clock()
clock.tick(30)

def resetGame():
    global TARGET, SCALE, PLAYER_1Name, PLAYER_2Name, PLAYER_1, PLAYER_2, PLAYER1NUM, PLAYER2NUM, TARGET1, SCALE1, inp_x, inp_y
    TARGET = ''
    SCALE = ''
    PLAYER_1Name = ''
    PLAYER_2Name = ''
    PLAYER_1=""
    PLAYER_2=""
    PLAYER1NUM = 0
    PLAYER2NUM = 0
    TARGET1 = 0
    SCALE1 = 0
    inp_x = 600
    inp_y = 420

def compOUT(font):
    global TARGET
    jobdone = False
    while not jobdone:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display_ground(font)
        t = str(TARGET1)
        player2_inp = font.render(t, True, (255, 255, 255))
        SCREEN.blit(player2_inp, (920, 500))
        pygame.display.update()
        jobdone  = True
        pygame.time.wait(2000)

def gameOver( x):
    pygame.time.wait(2000)
    font = pygame.font.Font(None, 92)
    global PLAYER_1, PLAYER_2
    SCREEN.fill((255, 255, 255))
    p1name = font.render(PLAYER_1Name, True, (255, 255, 255))
    p2name = font.render(PLAYER_2Name, True, (255, 255, 255))
    playAgain_rect = GAME_SPRITES['playAgain'].get_rect()
    image_width, image_height = GAME_SPRITES['playAgain'].get_size()
    x1 = (SCREEN.get_width() - image_width) - 250
    y1 = (SCREEN.get_height() - image_height) - 80
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                playAgain_rect = pygame.Rect(x1, y1, image_width, image_height)
                if playAgain_rect.collidepoint(mouse_pos):
                    resetGame()
                    home()
            if(x==1):
                SCREEN.blit(GAME_SPRITES['player1Won'], (0, 0))
                SCREEN.blit(p1name, (550, 325))
                GAME_SOUNDS['victory'].play()
            elif(x==2):
                SCREEN.blit(GAME_SPRITES['player2Won'], (0, 0))
                SCREEN.blit(p2name, (550, 325))
                GAME_SOUNDS['victory'].play()
            if(x==3):
                SCREEN.blit(GAME_SPRITES['ComputerWon'], (0, 0))
                SCREEN.blit(p1name, (510, 325))
            SCREEN.blit(GAME_SPRITES['playAgain'], (x1, y1))
            pygame.display.update()

def valid(x, sum):
    if sum - x >= 1 and sum - x <= SCALE1 and sum <= TARGET1:
        GAME_SOUNDS['point'].play()
        return True
    else:
        return False

def won(x):
    if x == TARGET1:
        return True
    else:
        return False

def get_user_input(font, id):
    
    user_text = ""
    inp1_x = 350
    inp1_y = 500
    inp2_x = 920
    inp2_y = 500
    stopwatch_duration = 7000  
    stopwatch_start_time = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                clicked = True
                if event.key == pygame.K_RETURN:
                    return user_text
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        # p1name = font.render(PLAYER_1Name, True, (255, 255, 255))
        # p2name = font.render(PLAYER_2Name, True, (255, 255, 255))
        # p1inp = font.render(PLAYER_2, True, (255, 255, 255))

        # if MODE==1:
        #     SCREEN.blit(GAME_SPRITES['mode1_screen'], (0, 0))
        # else:
        #     SCREEN.blit(GAME_SPRITES['mode2_screen'], (0, 0))
        #     SCREEN.blit(p1name, (270, 350))
        #     SCREEN.blit(p2name, (870, 350))
        
        elapsed_time = pygame.time.get_ticks() - stopwatch_start_time
        current_image_index = min(int(elapsed_time / 1000), 6)
        current_image = GAME_SPRITES['numbers'][current_image_index]
        SCREEN.blit(current_image, (600, 140))

        text_surface = font.render(user_text, True, (255, 255, 255))
        if id==1:
            SCREEN.blit(text_surface, (inp1_x, inp1_y))
        else:
            SCREEN.blit(text_surface, (inp2_x, inp2_y))
        pygame.display.update()
        if elapsed_time >= stopwatch_duration:
            if(MODE==1):
                gameOver(3)
            gameOver(id)

def display_ground(font):
    global PLAYER_1, PLAYER_2
    inp1_x = 350
    inp1_y = 500
    inp2_x = 920
    inp2_y = 500
    p1name = font.render(PLAYER_1Name, True, (255, 255, 255))
    p2name = font.render(PLAYER_2Name, True, (255, 255, 255))
    
    if MODE==1:
        SCREEN.blit(GAME_SPRITES['mode1_screen'], (0, 0))
        SCREEN.blit(p1name, (270, 350))
        SCREEN.blit(p2name, (870, 350))
    else:
        SCREEN.blit(GAME_SPRITES['mode2_screen'], (0, 0))
        SCREEN.blit(p1name, (270, 350))
        SCREEN.blit(p2name, (870, 350))
    
def play():
    global TARGET, SCALE, PLAYER_1Name, PLAYER_2Name, PLAYER_1, PLAYER_2, PLAYER1NUM, PLAYER2NUM, TARGET1, SCALE1
    font = pygame.font.Font(None, 72)
    global PLAYER_1, PLAYER_2
    display_ground(font)

    PLAYER_1 = get_user_input(font, 1)
    PLAYER1NUM = int(PLAYER_1)
    display_ground(font)
    if PLAYER1NUM < 1 or PLAYER1NUM > SCALE1:
        if MODE != 1:
            gameOver(2)
        else:
            gameOver(3)

    while True:
        display_ground(font)
        player1_inp = font.render(PLAYER_1, True, (255, 255, 255))
        SCREEN.blit(player1_inp, (350, 500))

        if MODE == 1:
            if TARGET1 - PLAYER1NUM <= SCALE1:
                PLAYER2NUM = TARGET1
                PLAYER_2 = str(PLAYER2NUM)
                compOUT(font)
                gameOver(3)

            else:
                PLAYER2NUM=random_number = random.randint(PLAYER1NUM+1, PLAYER1NUM+6)
            PLAYER_2 = str(PLAYER2NUM)

        else:
            PLAYER_2 = get_user_input(font, 2)
            PLAYER2NUM = int(PLAYER_2)
            if not valid(PLAYER1NUM, PLAYER2NUM):
                gameOver( 1)
        if valid(PLAYER1NUM, PLAYER2NUM) and won(PLAYER2NUM):
            if MODE != 1:
                gameOver(2)
            else:
                
                gameOver(3)

        display_ground(font)
        player2_inp = font.render(PLAYER_2, True, (255, 255, 255))
        SCREEN.blit(player2_inp, (920, 500))
        
        PLAYER_1 = get_user_input(font, 1)
        PLAYER1NUM = int(PLAYER_1)
        if not valid(PLAYER2NUM, PLAYER1NUM):
            if MODE != 1:
                gameOver(2)
            else:
                gameOver(3)
        if valid(PLAYER2NUM, PLAYER1NUM) and won(PLAYER1NUM):
            gameOver( 1)
            
def home():
    SCREEN.fill((255, 255, 255))
    image_rect = GAME_SPRITES['playBtn'].get_rect()

    image_width, image_height = GAME_SPRITES['playBtn'].get_size()
    x2 = (SCREEN.get_width() - image_width) / 2
    y2 = (SCREEN.get_height() - image_height) / 2 + 150

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                image_rect = pygame.Rect(x2, y2, image_width, image_height)
                if image_rect.collidepoint(mouse_pos):
                    mode()
            GAME_SOUNDS['start'].play()


        SCREEN.blit(GAME_SPRITES['homeImg'], (0, 0))
        SCREEN.blit(GAME_SPRITES['playBtn'], (x2, y2))
        pygame.display.update()

def mode():
    SCREEN.fill((255, 255, 255))
    image_rect1 = GAME_SPRITES['compBtn'].get_rect()
    image_rect2 = GAME_SPRITES['friendsBtn'].get_rect()

    image_width, image_height = GAME_SPRITES['compBtn'].get_size()
    x1 = (SCREEN.get_width() - image_width) / 2 -280
    y1 = (SCREEN.get_height() - image_height) / 2+200

    image_width1, image_height1 = GAME_SPRITES['friendsBtn'].get_size()
    x2 = (SCREEN.get_width() - image_width1) / 2 +190
    y2 = (SCREEN.get_height() - image_height1) / 2 + 190
    global MODE
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                friend_rect = pygame.Rect(x2, y2, image_width1, image_height1)
                comp_rect = pygame.Rect(x1, y1, image_width, image_height)
                if friend_rect.collidepoint(mouse_pos):
                    MODE = 2
                    GAME_SOUNDS['start'].stop()
                    setGame()
                if comp_rect.collidepoint(mouse_pos):
                    MODE = 1
                    GAME_SOUNDS['start'].stop()
                    setGame()
        SCREEN.blit(GAME_SPRITES['modeImg'], (0, 0))
        SCREEN.blit(GAME_SPRITES['compBtn'], (x1, y1))
        SCREEN.blit(GAME_SPRITES['friendsBtn'], (x2, y2))
        pygame.display.update()

def getInput(font, id):

    user_text = ""
    global inp_y
    size = (400, 300)
    line_color = (0, 0, 0)
    line_x = size[0] // 2
    line_width = 3
    line_height = 50
    blink_rate = 20
    blink_timer = blink_rate // 2
    clicked = False

    nextBtn_rect = GAME_SPRITES['nextBtn'].get_rect()
    image_width, image_height = GAME_SPRITES['nextBtn'].get_size()
    x1 = (SCREEN.get_width() - image_width) - 100
    y1 = (SCREEN.get_height() - image_height) - 80

    backBtn_rect = GAME_SPRITES['backBtn'].get_rect()
    image_width1, image_height1 = GAME_SPRITES['backBtn'].get_size()
    x2 = 80
    y2 = (SCREEN.get_height() - image_height1) - 80

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                clicked = True
                if event.key == pygame.K_RETURN:   
                    GAME_SOUNDS['input'].play()                
                    return user_text
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                nextBtn_rect = pygame.Rect(x1, y1, image_width1, image_height1)
                backBtn_rect = pygame.Rect(x2, y2, image_width1, image_height1)
                if nextBtn_rect.collidepoint(mouse_pos):
                    return
                if backBtn_rect.collidepoint(mouse_pos):
                    resetGame()
                    mode()

        if not clicked:
            blink_timer -= 1
            if blink_timer == 0:
                blink_timer = blink_rate
            if line_color == (0, 0, 0):
                line_color = (255, 255, 255)
            else:
                line_color = (0, 0, 0)
        if id==1:
            SCREEN.blit(GAME_SPRITES['getTarget'], (0,0))
        elif id==2:
            SCREEN.blit(GAME_SPRITES['getScale'], (0,0))
        elif id==3:
            SCREEN.blit(GAME_SPRITES['getP1Name'], (0,0))
        elif id==4:
            SCREEN.blit(GAME_SPRITES['getP2Name'], (0,0))
        if not clicked:
            pygame.draw.line(SCREEN, line_color, (inp_x, inp_y - line_height // 2 +25), (inp_x, inp_y + line_height // 2 + 25), line_width)

        text_surface = font.render(user_text, True, (255, 255, 255))
        SCREEN.blit(text_surface, (inp_x, inp_y))
        SCREEN.blit(GAME_SPRITES['nextBtn'], (x1, y1))
        SCREEN.blit(GAME_SPRITES['backBtn'], (x2, y2))

        pygame.display.update()

def setGame():
    global inp_x, id, PLAYER_1Name, PLAYER_2Name, TARGET, TARGET1, SCALE, SCALE1
    font = pygame.font.Font(None, 72)
    TARGET = getInput( font, 1)
    TARGET1 = int(TARGET)
    SCALE = getInput( font, 2)
    SCALE1 = int(SCALE)
    inp_x -= 100
    PLAYER_1Name = getInput( font, 3)
    if(MODE == 2):
        PLAYER_2Name = getInput( font, 4)
        play()
    else:
        PLAYER_2Name = "Computer"
    play()

if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('GAMING SYSTEM')

    base_font = pygame.font.SysFont('Calibri', 25)


    GAME_SPRITES['playBtn'] =pygame.image.load('sprites/playButton.png').convert_alpha()
    GAME_SPRITES['nextBtn'] =pygame.image.load('sprites/nextBtn.png').convert_alpha()
    GAME_SPRITES['backBtn'] =pygame.image.load('sprites/backBtn.png').convert_alpha()
    GAME_SPRITES['compBtn'] =pygame.image.load('sprites/compBtn.png').convert_alpha()
    GAME_SPRITES['friendsBtn'] =pygame.image.load('sprites/friendsBtn.png').convert_alpha()
    GAME_SPRITES['mode1'] =pygame.image.load('sprites/mode1.png').convert_alpha()
    GAME_SPRITES['mode2'] =pygame.image.load('sprites/mode2.png').convert_alpha()
    GAME_SPRITES['homeImg'] =pygame.image.load('sprites/homeImg.png').convert_alpha()
    GAME_SPRITES['modeImg'] =pygame.image.load('sprites/modeImg.png').convert_alpha()
    GAME_SPRITES['player1Won'] = pygame.image.load('sprites/player1Won.png').convert_alpha()
    GAME_SPRITES['player2Won'] = pygame.image.load('sprites/player2Won.png').convert_alpha()
    GAME_SPRITES['ComputerWon'] = pygame.image.load('sprites/ComputerWon.png').convert_alpha()
    GAME_SPRITES['mode1_screen'] = pygame.image.load('sprites/mode1_screen.png')
    GAME_SPRITES['mode2_screen'] = pygame.image.load('sprites/mode2_screen.png')
    GAME_SPRITES['getTarget'] = pygame.image.load('sprites/target.png')
    GAME_SPRITES['getScale'] = pygame.image.load('sprites/scale.png')
    GAME_SPRITES['getP1Name'] = pygame.image.load('sprites/p1Name.png')
    GAME_SPRITES['getP2Name'] = pygame.image.load('sprites/p2Name.png')
    GAME_SPRITES['playAgain'] = pygame.image.load('sprites/playAgain.png')
    GAME_SPRITES['numbers'] = ( 
        pygame.image.load('sprites/0.png').convert_alpha(),
        pygame.image.load('sprites/1.png').convert_alpha(),
        pygame.image.load('sprites/2.png').convert_alpha(),
        pygame.image.load('sprites/3.png').convert_alpha(),
        pygame.image.load('sprites/4.png').convert_alpha(),
        pygame.image.load('sprites/5.png').convert_alpha(),
        pygame.image.load('sprites/6.png').convert_alpha()
    )
    GAME_SOUNDS['input'] = pygame.mixer.Sound('audio/input.mp3')
    GAME_SOUNDS['start'] = pygame.mixer.Sound('audio/start.mp3')
    GAME_SOUNDS['victory'] = pygame.mixer.Sound('audio/victory.mp3')
    GAME_SOUNDS['start1'] = pygame.mixer.Sound('audio/start1.mp3')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('audio/point.wav')

    home()
    # play()



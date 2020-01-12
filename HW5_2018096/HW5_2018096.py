#name :shashikant kumar
#rollno: 2018096
#sec:A group:8

import pygame
from pygame.locals import *
pygame.init()
from numpy import loadtxt
import time
import random
import pygame.mixer
sound=pygame.mixer.Sound('ip.wav')
# sound.play()
no_sound=pygame.mixer.Sound('no.wav')
finist_sound=pygame.mixer.Sound('dst.wav')
poker_chips=pygame.mixer.Sound('pc.wav')
win_sound=pygame.mixer.Sound('ojj.wav')

#Constants for the game
def draw_wall(screen, pos):
    pixels = pixels_from_points(pos)
    #pygame.draw.rect(screen, WALL_COLOR, [pixels, (WIDTH, HEIGHT)])
    screen.blit(wall_texture,pixels)

def draw_pacman(screen, pos): 
    pixels = pixels_from_points(pos)
    pygame.draw.circle(screen, COIN_COLOR, (int(pixels[0]+16),int(pixels[1]+16)), WIDTH//2)

#Draws a rectangle for the coin
def draw_coin(screen, pos):
    pixels = pixels_from_points(pos)
    pygame.draw.circle(screen, COIN_COLOR, (int(pixels[0]+16),int(pixels[1]+16)), WIDTH//8)
def draw_enemy(enemy_number,screen,pos):
    pixels = pixels_from_points(pos)
    screen.blit(enemy_number,pixels)

#Uitlity functions
def add_to_pos(pos, pos2):
    return (pos[0]+pos2[0], pos[1]+pos2[1])
def pixels_from_points(pos):
    return (pos[0]*WIDTH, pos[1]*HEIGHT)
def ai_direction(pacman_position,enemy_position2):
    global move_direction_enemy2
    x_diffrence=(round(pacman_position[0]))-round(enemy_position2[0])
    y_diffrence=(round(pacman_position[1]))-round(enemy_position2[1])
    if abs(x_diffrence)>abs(y_diffrence) and x_diffrence<0:
        move_direction_enemy2=LEFT
    elif abs(x_diffrence)>abs(y_diffrence) and x_diffrence>0:
        move_direction_enemy2=RIGHT
    elif abs(x_diffrence)<abs(y_diffrence) and y_diffrence<0:
        move_direction_enemy2=TOP
    elif abs(x_diffrence)<abs(y_diffrence) and y_diffrence>0:
        move_direction_enemy2=DOWN

def ai_direction3(pacman_position,enemy_position3):
    global move_direction_enemy3
    x_diffrence=(round(pacman_position[0]))-round(enemy_position3[0])
    y_diffrence=(round(pacman_position[1]))-round(enemy_position3[1])
    if abs(x_diffrence)>abs(y_diffrence) and x_diffrence<0:
        move_direction_enemy3=LEFT
    elif abs(x_diffrence)>abs(y_diffrence) and x_diffrence>0:
        move_direction_enemy3=RIGHT
    elif abs(x_diffrence)<abs(y_diffrence) and y_diffrence<0:
        move_direction_enemy3=TOP
    elif abs(x_diffrence)<abs(y_diffrence) and y_diffrence>0:
        move_direction_enemy3=DOWN

def ai_direction4(pacman_position,enemy_position4):
    global move_direction_enemy4
    x_diffrence=(round(pacman_position[0]))-round(enemy_position4[0])
    y_diffrence=(round(pacman_position[1]))-round(enemy_position4[1])
    if abs(x_diffrence)>abs(y_diffrence) and x_diffrence<0:
        move_direction_enemy4=LEFT
    elif abs(x_diffrence)>abs(y_diffrence) and x_diffrence>0:
        move_direction_enemy4=RIGHT
    elif abs(x_diffrence)<abs(y_diffrence) and y_diffrence<0:
        move_direction_enemy4=TOP
    elif abs(x_diffrence)<abs(y_diffrence) and y_diffrence>0:
        move_direction_enemy4=DOWN

def ai_direction5(pacman_position,enemy_position5):
    global move_direction_enemy5
    x_diffrence=(round(pacman_position[0]))-round(enemy_position5[0])
    y_diffrence=(round(pacman_position[1]))-round(enemy_position5[1])

    if abs(x_diffrence)>abs(y_diffrence) and x_diffrence<0:
        move_direction_enemy5=LEFT
    elif abs(x_diffrence)>abs(y_diffrence) and x_diffrence>0:
        move_direction_enemy5=RIGHT

    elif abs(x_diffrence)<abs(y_diffrence) and y_diffrence<0:
        move_direction_enemy5=TOP
    elif abs(x_diffrence)<abs(y_diffrence) and y_diffrence>0:
        move_direction_enemy5=DOWN


def message_to_screen(msg,color,x,y,size): # this is the function print a message on the screen and the font is not predefined
    font=pygame.font.SysFont(None,size)
    screen_text=font.render(msg,True,color)
    screen.blit(screen_text,[x,y])

WIDTH, HEIGHT = (32, 32)
WALL_COLOR = pygame.Color(0, 0, 255, 255) # BLUE
PACMAN_COLOR = pygame.Color(255, 0, 0, 255) # RED
COIN_COLOR = pygame.Color(255, 255, 0, 255) # RED
DOWN = (0,0.1)
RIGHT = (0.1,0)
TOP = (0,-0.1)
LEFT = (-0.1,0)
STILL=(0,0)

move_direction_enemy2=TOP
move_direction_enemy3=DOWN
move_direction_enemy4=RIGHT
move_direction_enemy5=LEFT


en1=pygame.image.load('tatti.png')
en2=pygame.image.load('tatti1.png')
en3=pygame.image.load('tatti2.png')
en4=pygame.image.load('tatti3.png')

wall_texture=pygame.image.load('pa11.png')

clock=pygame.time.Clock()

screen = pygame.display.set_mode((640,640), 0, 32)
background = pygame.surface.Surface((640,640)).convert()
p1=pygame.image.load('pa1.png')
p2=pygame.image.load('pa2.png')
p3=pygame.image.load('pa3.png')
p4=pygame.image.load('pa4.png')
pac1,pac2,pac3,pac4=p1,p2,p3,p4
currentimage=1
rotationdirection=0

FPS=20
#Initializing variables

pacman_position = (1,1)
background.fill((0,0,0))
enemy_position2=(1,18)
enemy_position3=(18,1)
enemy_position4=(10,10)
enemy_position5=(18,18)
move_direction=STILL
df1=0
image1=pygame.image.load('sta.png')


def gameloop():
    sound.play()
    finist_sound.stop()
    win_sound.stop()
    global move_direction_enemy2
    global move_direction_enemy3
    global move_direction_enemy4
    global move_direction_enemy5
    global currentimage
    global rotationdirection
    global pacman_position
    global enemy_position2
    global enemy_position3
    global enemy_position4
    global enemy_position5
    global move_direction
    gamerun1=True
    gamerun2=False
    score=0
    life=5
    difficulty=0
    global pac1
    global pac2
    global pac3
    global pac4
    global df1
    layout = loadtxt('layout.txt', dtype=str)
    rows, cols = layout.shape
    number_of_coins=0
    for i in layout:
        for j in i:
            if j=='.':
                number_of_coins+=1
    # print(number_of_coins)
    screen.blit(image1,(0,0))
    pygame.display.update()
    timer_start=0

    intiate=True
    while intiate:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    difficulty=1
                    FPS=30
                    intiate=False
                elif event.key==pygame.K_2:
                    difficulty=3
                    FPS=30
                    intiate=False
                elif event.key==pygame.K_3:
                    difficulty=11
                    FPS=40
                    intiate=False

    while gamerun1:
        while gamerun2:
            if life==0:
                finist_sound.play()
                screen.fill((255,255,255))
                message_to_screen("GAME OVER",(148,0,211),160,200,80)
                message_to_screen("your score is : "+str(score),(255,0,0),190,320,50)
                message_to_screen("press c to play again or q to exit",(200,100,0),200,400,25)
                pygame.display.update()
                

                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_q:
                            exit()
                        elif event.key==pygame.K_c:
                            gameloop()
            else:
                win_sound.play()
                screen.fill((255,255,255))
                message_to_screen("YOU WIN",(148,0,211),175,200,80)
                message_to_screen("CONGRATULATIONS",(255,0,0),145,320,50)
                message_to_screen("press c to play again or q to exit",(200,100,0),195,400,25)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_q:
                            exit()
                        elif event.key==pygame.K_c:
                            gameloop()



        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type==pygame.KEYDOWN:
                sound.stop()
                if event.key==pygame.K_LEFT:
                    move_direction=LEFT
                    
                elif event.key==pygame.K_RIGHT:
                    move_direction=RIGHT
                    
                elif event.key==pygame.K_UP:
                    move_direction=TOP
                    
                elif event.key==pygame.K_DOWN:
                    move_direction=DOWN



        screen.blit(background, (0,0))

        for col in range(cols):
            for row in range(rows):
                value = layout[row][col]
                pos = (col, row)
                
                if value == 'w':
                    draw_wall(screen, pos)
                elif value == '.':
                    draw_coin(screen, pos)
           
        if move_direction==RIGHT:
            pac1,pac2,pac3,pac4=p1,p2,p3,p4
            if layout[round(pacman_position[1])][int(pacman_position[0])+1]=="w":
                move_direction=STILL
                

        elif move_direction==LEFT:
            pac1=pygame.transform.rotate(p1,180)
            pac2=pygame.transform.rotate(p2,180)
            pac3=pygame.transform.rotate(p3,180)
            pac4=pygame.transform.rotate(p4,180)
            if layout[round(pacman_position[1])][int(pacman_position[0])]=="w":
                move_direction=STILL
                
                
        elif move_direction==TOP:
            pac1=pygame.transform.rotate(p1,90)
            pac2=pygame.transform.rotate(p2,90)
            pac3=pygame.transform.rotate(p3,90)
            pac4=pygame.transform.rotate(p4,90)
            if layout[int(pacman_position[1])][round(pacman_position[0])]=="w":
                move_direction=STILL
                
                
        elif move_direction==DOWN:
            pac1=pygame.transform.rotate(p1,-90)
            pac2=pygame.transform.rotate(p2,-90)
            pac3=pygame.transform.rotate(p3,-90)
            pac4=pygame.transform.rotate(p4,-90)
            if layout[int(pacman_position[1])+1][round(pacman_position[0])]=="w":
                move_direction=STILL
                

        if move_direction==LEFT or move_direction==RIGHT:
            pacman_position=((pacman_position[0]),round(pacman_position[1]))
            if 0<(pacman_position[0])<0.1 and round(pacman_position[1])==3:
                pacman_position=(18.8,15)
            elif 18.9<pacman_position[0]<19 and round(pacman_position[1])==15:
                pacman_position=(0.2,3)
            elif 0<(pacman_position[0])<0.1 and round(pacman_position[1])==15:
                pacman_position=(18.8,3)
            elif 18.9<(pacman_position[0])<19 and round(pacman_position[1])==3:
                pacman_position=(0.2,15)  

            
        if move_direction==TOP or move_direction==DOWN:
            pacman_position=(round(pacman_position[0]),(pacman_position[1]))

        if layout[round(pacman_position[1])][round(pacman_position[0])]==".":
            layout[round(pacman_position[1])][round(pacman_position[0])]="s"
            score+=1
            poker_chips.play()
        message_to_screen("SCORE : "+str(score),(255,255,255),1,1,20) 
        

        #start of the enmy postions
        if move_direction_enemy2==RIGHT:
            if layout[round(enemy_position2[1])][int(enemy_position2[0])+1]=="w":
                move_direction_enemy2=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy2=TOP
                else:
                    move_direction_enemy2=DOWN
            elif (layout[round(enemy_position2[1]+1)][round(enemy_position2[0])]=="." or layout[round(enemy_position2[1]+1)][round(enemy_position2[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction(pacman_position,enemy_position2)

            elif (layout[round(enemy_position2[1])-1][round(enemy_position2[0])]=="." or layout[round(enemy_position2[1]-1)][round(enemy_position2[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction(pacman_position,enemy_position2)

        elif move_direction_enemy2==LEFT:
            if layout[round(enemy_position2[1])][int(enemy_position2[0])]=="w" :
                move_direction_enemy2=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy2=TOP
                else:
                    move_direction_enemy2=DOWN
            elif (layout[round(enemy_position2[1]+1)][round(enemy_position2[0])]=="." or layout[round(enemy_position2[1]+1)][round(enemy_position2[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction(pacman_position,enemy_position2)

            elif (layout[round(enemy_position2[1]-1)][round(enemy_position2[0])]=="." or layout[round(enemy_position2[1]-1)][round(enemy_position2[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction(pacman_position,enemy_position2)
                
        elif move_direction_enemy2==TOP:
            if layout[int(enemy_position2[1])][round(enemy_position2[0])]=="w":
                move_direction_enemy2=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy2=RIGHT
                else:
                    move_direction_enemy2=LEFT
            elif (layout[round(enemy_position2[1])][round(enemy_position2[0]-1)]=="." or layout[round(enemy_position2[1])][round(enemy_position2[0]-1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction(pacman_position,enemy_position2)
            elif (layout[round(enemy_position2[1])][round(enemy_position2[0]+1)]=="." or layout[round(enemy_position2[1])][round(enemy_position2[0]+1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction(pacman_position,enemy_position2)

        elif move_direction_enemy2==DOWN:
            if layout[int(enemy_position2[1])+1][round(enemy_position2[0])]=="w":
                move_direction_enemy2=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy2=RIGHT
                else:
                    move_direction_enemy2=LEFT
            elif (layout[round(enemy_position2[1])][round(enemy_position2[0]-1)]=="." or layout[round(enemy_position2[1])][round(enemy_position2[0]-1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction(pacman_position,enemy_position2)

            elif (layout[round(enemy_position2[1])][round(enemy_position2[0]+1)]=="." or layout[round(enemy_position2[1])][round(enemy_position2[0]+1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction(pacman_position,enemy_position2)


        if move_direction_enemy2==LEFT or move_direction_enemy2==RIGHT:
            enemy_position2=((enemy_position2[0]),round(enemy_position2[1]))
            if 0<(enemy_position2[0])<0.1 and round(enemy_position2[1])==3:
                enemy_position2=(18.8,15)
            elif 18.9<enemy_position2[0]<19 and round(enemy_position2[1])==15:
                enemy_position2=(0.2,3)
            elif 0<(enemy_position2[0])<0.1 and round(enemy_position2[1])==15:
                enemy_position2=(18.8,3)
            elif 18.9<(enemy_position2[0])<19 and round(enemy_position2[1])==3:
                enemy_position2=(0.2,15)            

            
        elif move_direction_enemy2==TOP or move_direction_enemy2==DOWN:
            enemy_position2=(round(enemy_position2[0]),(enemy_position2[1]))
            


        draw_enemy(en1,screen,enemy_position2)
        enemy_position2= add_to_pos(enemy_position2,move_direction_enemy2)

        if round(pacman_position[1])==round(enemy_position2[1]) and round(pacman_position[0])==round(enemy_position2[0]):
            df1+=1
            no_sound.play()
            
            message_to_screen("GOT YOU!!",(255,0,0),pacman_position[0]*32,pacman_position[1]*32,20)
            pygame.display.update()
            time.sleep(1)
            pacman_position=(1,1)
            move_direction=STILL
            enemy_position2=(1,18)
            enemy_position3=(18,1)
            enemy_position4=(10,10)
            enemy_position5=(18,18)
            life-=1
            time.sleep(2)


        #2nd enemy motions
        if move_direction_enemy3==RIGHT:
            if layout[round(enemy_position3[1])][int(enemy_position3[0])+1]=="w":
                move_direction_enemy3=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy3=TOP
                else:
                    move_direction_enemy3=DOWN
            elif (layout[round(enemy_position3[1]+1)][round(enemy_position3[0])]=="." or layout[round(enemy_position3[1]+1)][round(enemy_position3[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction3(pacman_position,enemy_position3)

            elif (layout[round(enemy_position3[1])-1][round(enemy_position3[0])]=="." or layout[round(enemy_position3[1]-1)][round(enemy_position3[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction3(pacman_position,enemy_position3)

        elif move_direction_enemy3==LEFT:
            if layout[round(enemy_position3[1])][int(enemy_position3[0])]=="w" :
                move_direction_enemy3=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy3=TOP
                else:
                    move_direction_enemy3=DOWN
            elif (layout[round(enemy_position3[1]+1)][round(enemy_position3[0])]=="." or layout[round(enemy_position3[1]+1)][round(enemy_position3[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction3(pacman_position,enemy_position3)

            elif (layout[round(enemy_position3[1]-1)][round(enemy_position3[0])]=="." or layout[round(enemy_position3[1]-1)][round(enemy_position3[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction3(pacman_position,enemy_position3)
                
        elif move_direction_enemy3==TOP:
            if layout[int(enemy_position3[1])][round(enemy_position3[0])]=="w":
                move_direction_enemy3=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy3=RIGHT
                else:
                    move_direction_enemy3=LEFT
            elif (layout[round(enemy_position3[1])][round(enemy_position3[0]-1)]=="." or layout[round(enemy_position3[1])][round(enemy_position3[0]-1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction3(pacman_position,enemy_position3)
            elif (layout[round(enemy_position3[1])][round(enemy_position3[0]+1)]=="." or layout[round(enemy_position3[1])][round(enemy_position3[0]+1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction3(pacman_position,enemy_position3)

        elif move_direction_enemy3==DOWN:
            if layout[int(enemy_position3[1])+1][round(enemy_position3[0])]=="w":
                move_direction_enemy3=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy3=RIGHT
                else:
                    move_direction_enemy3=LEFT
            elif (layout[round(enemy_position3[1])][round(enemy_position3[0]-1)]=="." or layout[round(enemy_position3[1])][round(enemy_position3[0]-1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction3(pacman_position,enemy_position3)

            elif (layout[round(enemy_position3[1])][round(enemy_position3[0]+1)]=="." or layout[round(enemy_position3[1])][round(enemy_position3[0]+1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction3(pacman_position,enemy_position3)


        if move_direction_enemy3==LEFT or move_direction_enemy3==RIGHT:
            enemy_position3=((enemy_position3[0]),round(enemy_position3[1]))
            if 0<(enemy_position3[0])<0.1 and round(enemy_position3[1])==3:
                enemy_position3=(18.8,15)
            elif 18.9<enemy_position3[0]<19 and round(enemy_position3[1])==15:
                enemy_position3=(0.2,3)
            elif 0<(enemy_position3[0])<0.1 and round(enemy_position3[1])==15:
                enemy_position3=(18.8,3)
            elif 18.9<(enemy_position3[0])<19 and round(enemy_position3[1])==3:
                enemy_position3=(0.2,15)            

            
        elif move_direction_enemy3==TOP or move_direction_enemy3==DOWN:
            enemy_position3=(round(enemy_position3[0]),(enemy_position3[1]))
            


        draw_enemy(en2,screen,enemy_position3)
        enemy_position3= add_to_pos(enemy_position3,move_direction_enemy3)

        if round(pacman_position[1])==round(enemy_position3[1]) and round(pacman_position[0])==round(enemy_position3[0]):
            df1+=1
            no_sound.play()
            message_to_screen("GOT YOU!!",(255,0,0),pacman_position[0]*32,pacman_position[1]*32,20)
            pygame.display.update()
            time.sleep(1)
            pacman_position=(1,1)
            move_direction=STILL
            enemy_position2=(1,18)
            enemy_position3=(18,1)
            enemy_position4=(10,10)
            enemy_position5=(18,18)
            life-=1
            time.sleep(2)

        # 3rd villan
        if move_direction_enemy4==RIGHT:
            if layout[round(enemy_position4[1])][int(enemy_position4[0])+1]=="w":
                move_direction_enemy4=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy4=TOP
                else:
                    move_direction_enemy4=DOWN
            elif (layout[round(enemy_position4[1]+1)][round(enemy_position4[0])]=="." or layout[round(enemy_position4[1]+1)][round(enemy_position4[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction4(pacman_position,enemy_position4)

            elif (layout[round(enemy_position4[1])-1][round(enemy_position4[0])]=="." or layout[round(enemy_position4[1]-1)][round(enemy_position4[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction4(pacman_position,enemy_position4)

        elif move_direction_enemy4==LEFT:
            if layout[round(enemy_position4[1])][int(enemy_position4[0])]=="w" :
                move_direction_enemy4=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy4=TOP
                else:
                    move_direction_enemy4=DOWN
            elif (layout[round(enemy_position4[1]+1)][round(enemy_position4[0])]=="." or layout[round(enemy_position4[1]+1)][round(enemy_position4[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction4(pacman_position,enemy_position4)

            elif (layout[round(enemy_position4[1]-1)][round(enemy_position4[0])]=="." or layout[round(enemy_position4[1]-1)][round(enemy_position4[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction4(pacman_position,enemy_position4)
                
        elif move_direction_enemy4==TOP:
            if layout[int(enemy_position4[1])][round(enemy_position4[0])]=="w":
                move_direction_enemy4=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy4=RIGHT
                else:
                    move_direction_enemy4=LEFT
            elif (layout[round(enemy_position4[1])][round(enemy_position4[0]-1)]=="." or layout[round(enemy_position4[1])][round(enemy_position4[0]-1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction4(pacman_position,enemy_position4)
            elif (layout[round(enemy_position4[1])][round(enemy_position4[0]+1)]=="." or layout[round(enemy_position4[1])][round(enemy_position4[0]+1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction4(pacman_position,enemy_position4)

        elif move_direction_enemy4==DOWN:
            if layout[int(enemy_position4[1])+1][round(enemy_position4[0])]=="w":
                move_direction_enemy4=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy4=RIGHT
                else:
                    move_direction_enemy4=LEFT
            elif (layout[round(enemy_position4[1])][round(enemy_position4[0]-1)]=="." or layout[round(enemy_position4[1])][round(enemy_position4[0]-1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction4(pacman_position,enemy_position4)

            elif (layout[round(enemy_position4[1])][round(enemy_position4[0]+1)]=="." or layout[round(enemy_position4[1])][round(enemy_position4[0]+1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction4(pacman_position,enemy_position4)


        if move_direction_enemy4==LEFT or move_direction_enemy4==RIGHT:
            enemy_position4=((enemy_position4[0]),round(enemy_position4[1]))            
            if 0<(enemy_position4[0])<0.1 and round(enemy_position4[1])==3:
                enemy_position4=(18.8,15)
            elif 18.9<enemy_position4[0]<19 and round(enemy_position4[1])==15:
                enemy_position4=(0.2,3)
            elif 0<(enemy_position4[0])<0.1 and round(enemy_position4[1])==15:
                enemy_position4=(18.8,3)
            elif 18.9<(enemy_position4[0])<19 and round(enemy_position4[1])==3:
                enemy_position4=(0.2,15)
            
        elif move_direction_enemy4==TOP or move_direction_enemy4==DOWN:
            enemy_position4=(round(enemy_position4[0]),(enemy_position4[1]))
            


        draw_enemy(en3,screen,enemy_position4)
        enemy_position4= add_to_pos(enemy_position4,move_direction_enemy4)

        if round(pacman_position[1])==round(enemy_position4[1]) and round(pacman_position[0])==round(enemy_position4[0]):
            df1+=1
            no_sound.play()
            
            message_to_screen("GOT YOU!!",(255,0,0),pacman_position[0]*32,pacman_position[1]*32,20)
            pygame.display.update()
            time.sleep(1)
            pacman_position=(1,1)
            move_direction=STILL
            enemy_position2=(1,18)
            enemy_position3=(18,1)
            enemy_position4=(10,10)
            enemy_position5=(18,18)
            life-=1
            time.sleep(2)

        #4th enemy
        if move_direction_enemy5==RIGHT:
            if layout[round(enemy_position5[1])][int(enemy_position5[0])+1]=="w":
                move_direction_enemy5=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy5=TOP
                else:
                    move_direction_enemy5=DOWN
            elif (layout[round(enemy_position5[1]+1)][round(enemy_position5[0])]=="." or layout[round(enemy_position5[1]+1)][round(enemy_position5[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction5(pacman_position,enemy_position5)

            elif (layout[round(enemy_position5[1])-1][round(enemy_position5[0])]=="." or layout[round(enemy_position5[1]-1)][round(enemy_position5[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction5(pacman_position,enemy_position5)

        elif move_direction_enemy5==LEFT:
            if layout[round(enemy_position5[1])][int(enemy_position5[0])]=="w" :
                move_direction_enemy5=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy5=TOP
                else:
                    move_direction_enemy5=DOWN
            elif (layout[round(enemy_position5[1]+1)][round(enemy_position5[0])]=="." or layout[round(enemy_position5[1]+1)][round(enemy_position5[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction5(pacman_position,enemy_position5)

            elif (layout[round(enemy_position5[1]-1)][round(enemy_position5[0])]=="." or layout[round(enemy_position5[1]-1)][round(enemy_position5[0])]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction5(pacman_position,enemy_position5)
                
        elif move_direction_enemy5==TOP:
            if layout[int(enemy_position5[1])][round(enemy_position5[0])]=="w":
                move_direction_enemy5=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy5=RIGHT
                else:
                    move_direction_enemy5=LEFT
            elif (layout[round(enemy_position5[1])][round(enemy_position5[0]-1)]=="." or layout[round(enemy_position5[1])][round(enemy_position5[0]-1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction5(pacman_position,enemy_position5)
            elif (layout[round(enemy_position5[1])][round(enemy_position5[0]+1)]=="." or layout[round(enemy_position5[1])][round(enemy_position5[0]+1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction5(pacman_position,enemy_position5)

        elif move_direction_enemy5==DOWN:
            if layout[int(enemy_position5[1])+1][round(enemy_position5[0])]=="w":
                move_direction_enemy5=STILL
                a=random.randint(0,1)
                if a==0:
                    move_direction_enemy5=RIGHT
                else:
                    move_direction_enemy5=LEFT
            elif (layout[round(enemy_position5[1])][round(enemy_position5[0]-1)]=="." or layout[round(enemy_position5[1])][round(enemy_position5[0]-1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction5(pacman_position,enemy_position5)

            elif (layout[round(enemy_position5[1])][round(enemy_position5[0]+1)]=="." or layout[round(enemy_position5[1])][round(enemy_position5[0]+1)]=="s"):
                decide=random.randint(1,100)
                if 1<=decide<=difficulty:
                    ai_direction5(pacman_position,enemy_position5)


        if move_direction_enemy5==LEFT or move_direction_enemy5==RIGHT:
            enemy_position5=((enemy_position5[0]),round(enemy_position5[1]))
            if 0<(enemy_position5[0])<0.1 and round(enemy_position5[1])==3:
                enemy_position5=(18.8,15)
            elif 18.9<enemy_position5[0]<19 and round(enemy_position5[1])==15:
                enemy_position5=(0.2,3)
            elif 0<(enemy_position5[0])<0.1 and round(enemy_position5[1])==15:
                enemy_position5=(18.8,3)
            elif 18.9<(enemy_position5[0])<19 and round(enemy_position5[1])==3:
                enemy_position5=(0.2,15)            

            
        elif move_direction_enemy5==TOP or move_direction_enemy5==DOWN:
            enemy_position5=(round(enemy_position5[0]),(enemy_position5[1]))
            


        draw_enemy(en4,screen,enemy_position5)
        enemy_position5= add_to_pos(enemy_position5,move_direction_enemy5)

        if round(pacman_position[1])==round(enemy_position5[1]) and round(pacman_position[0])==round(enemy_position5[0]):
            df1+=1
            no_sound.play()
            
            message_to_screen("GOT YOU!!",(255,0,0),pacman_position[0]*32,pacman_position[1]*32,20)
            pygame.display.update()
            time.sleep(1)
            pacman_position=(1,1)
            move_direction=STILL
            enemy_position2=(1,18)
            enemy_position3=(18,1)
            enemy_position4=(10,10)
            enemy_position5=(18,18)
            life-=1
            time.sleep(2)


        message_to_screen("LIFES LEFT : "+str(life),(255,255,255),150,1,20)
        #Draw the player
        #draw_pacman(screen, pacman_position)   
        #pacimg(screen,pacman_position,currentimage,p1,p2)
        #TODO: Take input from the user and update pacman moving direction, Currently hardcoded to always move down
        
        pixels = pixels_from_points(pacman_position)
        if currentimage==1 or currentimage==2:
            screen.blit(pac1,pixels)
        elif (currentimage==3 or currentimage==4):
            screen.blit(pac2,pixels)
        elif currentimage==5 or currentimage==6:
            screen.blit(pac3,pixels)
        elif currentimage==7 or currentimage==8:
            screen.blit(pac4,pixels)
        if currentimage==8:
            currentimage=1
        else:
            currentimage+=1
       
        #Update player position based on movement.
        pacman_position = add_to_pos(pacman_position, move_direction)
        
        if life==0 or score==number_of_coins:
            gamerun2=True
        message_to_screen("TIMER : "+str('%.2f' %timer_start),(255,255,255),400,1,20) 
        
        timer_start+=(1/FPS)

        pygame.display.update()

        #Wait for a while, computers are very fast.
        clock.tick(FPS)
gameloop()
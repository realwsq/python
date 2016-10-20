import pygame, sys, random,string
from pygame.locals import *

def show_text(surface_handle,pos,text,color,back_color = (255,255,255),font_bold = False, font_size = 13, font_italic = False):
    cur_font = pygame.font.SysFont("Courier New",font_size)
    cur_font.set_bold(font_bold)
    cur_font.set_italic(font_italic)
    text_fmt = cur_font.render(text,1,color,back_color)
    surface_handle.blit(text_fmt,pos)

def readin_data(file):
    for line in file:
        line = line.rstrip()
        data.append(string.atoi(line))

def sort(data):
    data.sort(reverse=True)
    if(len(data)<=10):
        return data
    else:
        for i in range(0,10):
            data10.append(data[i])
        return data10

def show_data(data):
    length = len(data)
    for i in range(0,length):
        showData = "No"+str(i+1)+": "+str(data[i])
        show_text(windowSurface,(100,250+i*20),showData,WHITE,BLACK,False,15,False)

def collision_detect(head):
    length = len(snakeRect)
    for i in range(1,length):
        if snakeRect[i].left == head.left and snakeRect[i].top == head.top:
            return 1
    return 0

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 400
WINDOWHEIGHT = 500
rectLength = 18

windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Snake')

BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
f = open("out.txt", "a")
data = []
data10 = []
length = 0
showData = ''

snakeRect = []
for i in range(7,10):
    snakeRect.append(pygame.Rect(i*(rectLength+2)+1,0+1,rectLength,rectLength))
food = pygame.Rect(5*(rectLength+2),5*(rectLength+2),rectLength+2,rectLength+2)   
moveLeft = True
moveRight = False
moveUp = False
moveDown = False


scores = 0
show_text(windowSurface, (50,50), "welcome!",WHITE,BLACK,False,64,False)
pygame.display.update()
begin = 0
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                begin = 1
                break
    if begin == 1:
        break
    mainClock.tick(10)
    
SCORE = 'scores:'
score = ''
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT and moveRight==False:
                moveLeft = True
                moveRight = False
                moveUp = False
                moveDown = False
            if event.key == K_RIGHT and moveLeft==False:
                moveLeft = False
                moveRight = True
                moveUp = False
                moveDown = False
            if event.key == K_UP and moveDown==False:
                moveLeft = False
                moveRight = False
                moveUp = True
                moveDown = False
            if event.key == K_DOWN and moveUp==False:
                moveLeft = False
                moveRight = False
                moveUp = False
                moveDown = True
    head = pygame.Rect(snakeRect[0].left,snakeRect[0].top,snakeRect[0].width,snakeRect[0].height)
    if moveLeft == True:
        head.right = head.left-2
    if moveRight == True:
        head.left = head.right+2
    if moveUp == True:
        head.bottom = head.top-2
    if moveDown == True:
        head.top = head.bottom+2
    snakeRect.insert(0,head);
    if head.right<0 or head.left>WINDOWWIDTH or head.bottom<0 or head.top>WINDOWHEIGHT-100:
        break
    if collision_detect(head):
        break
    if food.left == snakeRect[0].left-1 and food.top == snakeRect[0].top-1:
        food.left = random.randint(0,WINDOWWIDTH/20-1)*(rectLength+2)
        food.top = random.randint(0,(WINDOWHEIGHT-100)/20-1)*(rectLength+2)
        scores += 1
        # pickUpSound.play()
    else:
         snakeRect.pop(len(snakeRect)-1)
    windowSurface.fill(BLACK)
    for i in range(len(snakeRect)):
        pygame.draw.rect(windowSurface,GREEN,snakeRect[i])
    pygame.draw.rect(windowSurface,RED,food)
    pygame.draw.line(windowSurface,WHITE, (0,400),(400,400), 1)
    score = SCORE+str(scores)
    show_text(windowSurface, (300,450), score,WHITE,BLACK,False,13,False)
    pygame.display.update()
    mainClock.tick(10)   

print >> f, "%d" % (scores)
f.close()
windowSurface.fill(BLACK)
fr = open("out.txt","r")
readin_data(fr)
data = sort(data)
show_data(data)
# print data
pygame.display.update()   
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    show_text(windowSurface, (50,50), "fuck hkc!",WHITE,BLACK,False,64,False)
    show_text(windowSurface, (70,150), score,WHITE,BLACK,False,64,False)
    show_data(data)
    pygame.display.update()
    mainClock.tick(10)
    
# begin screen
# game over
# score    (after game over)
# ai


 
            
    

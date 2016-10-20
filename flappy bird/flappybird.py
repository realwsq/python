import pygame, sys, random,string
from pygame.locals import *

class BIRD:
	def __init__(self):
		self.x = (WINDOWWIDTH-fbirdWidth)/2
		self.y = (WINDOWHEIGHT-fbirdHeight)/2
		self.vy = 10
		self.vx = 10
		self.a = 3
	def nextPos(self,pressed):
		if pressed:
			self.y = self.y - 20
			self.vy = 10
		else:
			self.y = self.y + self.vy 
			self.vy = self.vy + self.a
		self.x = self.x + self.vx

def draw(birdX,birdY): 
	windowSurface.fill(WHITE)
	windowSurface.blit(fbird,(fbirdDISleft,birdY))
	for i in range(len(pipe)):
		if pipe[i][0]>birdX-fbirdDISleft-pipeMiddleWidth and pipe[i][0]<birdX+fbirdDISright:
			for j in range(pipe[i][1]):
				windowSurface.blit(pipeMiddle,(pipe[i][0]-(birdX-fbirdDISleft),WINDOWHEIGHT-(j+1)*pipeMiddleHeight))
			windowSurface.blit(pipeTop,(pipe[i][0]+pipeMiddleWidth/2-pipeTopWidth/2-(birdX-fbirdDISleft),WINDOWHEIGHT-pipe[i][1]*pipeMiddleHeight-pipeTopHeight))
			for j in range(pipe[i][2]):
				windowSurface.blit(pipeMiddle,(pipe[i][0]-(birdX-fbirdDISleft),j*pipeMiddleHeight))
			windowSurface.blit(pipeTop,(pipe[i][0]+pipeMiddleWidth/2-pipeTopWidth/2-(birdX-fbirdDISleft),(pipe[i][2])*pipeMiddleHeight))
	pygame.display.update()

def drawScores(birdX):
	windowSurface.fill(WHITE)
	i = 0
	while pipe[i][0]+pipeMiddleWidth<birdX:
		i+=1
	show_text(windowSurface,(350,250), str(i), BLACK,WHITE,False,100,False)
	pygame.display.update()
	print >> f, "%d" % (i)
	f.close()
	

def show_text(surface_handle,pos,text,color,back_color = (255,255,255),font_bold = False, font_size = 13, font_italic = False):
	cur_font = pygame.font.SysFont("Courier New",font_size)
	cur_font.set_bold(font_bold)
	cur_font.set_italic(font_italic)
	text_fmt = cur_font.render(text,1,color,back_color)
	surface_handle.blit(text_fmt,pos)
		
			
def collision(birdX,birdY):
	for i in range(len(pipe)):
		if (pipe[i][0]<=birdX+fbirdWidth and pipe[i][0]+pipeMiddleWidth>birdX+fbirdWidth) or (pipe[i][0]<=birdX and pipe[i][0]+pipeMiddleWidth>birdX):
			if birdY>pipe[i][2]*pipeMiddleHeight+pipeTopHeight-20 and birdY+fbirdHeight<WINDOWHEIGHT-(pipe[i][1]*pipeMiddleHeight+pipeTopHeight)+20:
				return 0
			else:
				return 1
	if birdY<0:
		return 1 
	if birdY>WINDOWHEIGHT:
		return 1
	return 0
			

pygame.init()
mainClock = pygame.time.Clock()

BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
f = open("out.txt", "a")
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('wsq bird')
fbird = pygame.image.load('flappybird.png').convert()
pipeMiddle = pygame.image.load('PipeMiddle.PNG').convert()
pipeTop = pygame.image.load('PipeTop.PNG').convert()
pipeMiddleWidth = pipeMiddle.get_width()
pipeMiddleHeight = pipeMiddle.get_height()
pipeTopWidth = pipeTop.get_width()
pipeTopHeight = pipeTop.get_height()
fbirdWidth = fbird.get_width()
fbirdHeight = fbird.get_height()
fbirdDISleft = (WINDOWWIDTH-fbirdWidth)/2
fbirdDISright = (WINDOWWIDTH+fbirdWidth)/2



pipe = ((500,2,3),(770,8,5),(1050,3,8),(1400,8,5),(1800,5,7),(2200,5,5),(2800,6,5),(3700,1,12),(4700,12,1))
bird = BIRD()
pressed = 0
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_SPACE:
				pressed = 1
				bird.nextPos(pressed) 
	if not pressed :
		bird.nextPos(pressed)
	if pressed:
		pressed = 0
	draw(bird.x,bird.y)
	if collision(bird.x, bird.y):
		drawScores(bird.x)
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
	mainClock.tick(10)
				

# button
# last: scores led bazzer(music) motor 








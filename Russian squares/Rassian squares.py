import pygame,sys,random,string
from pygame.locals import*

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 500
WINDOWHEIGHT = 600
rectLength = 18
TOTAL = 7
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Rassian Squares')
HKC = pygame.image.load('hkc.jpg').convert()

fourSquares = []
chessBoard = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]


class bar:
	def __init__(self):
		self.state = 1

	def begin(self):
		fourSquares = []
		for i in range(8,12):
			fourSquares.append(pygame.Rect(i*(rectLength+2)+1,0+1,rectLength,rectLength))

	# boundary  collision
	def rotate(self):
		if self.state == 1:
			fourSquares[0].left = fourSquares[0].left+20
			fourSquares[0].top = fourSquares[0].top-20
			fourSquares[2].left = fourSquares[2].left-20
			fourSquares[2].top = fourSquares[2].top+20
			fourSquares[3].left = fourSquares[3].left-40
			fourSquares[3].top = fourSquares[3].top+40
			self.state+=1
			self.state = self.state%4 + 1
		elif self.state == 2:
			fourSquares[0].left = fourSquares[0].left+20
			fourSquares[0].top = fourSquares[0].top+20
			fourSquares[2].left = fourSquares[2].left-20
			fourSquares[2].top = fourSquares[2].top-20
			fourSquares[3].left = fourSquares[3].left-40
			fourSquares[3].top = fourSquares[3].top-40
			self.state+=1
			self.state = self.state%4 + 1
		elif self.state == 3:
			fourSquares[0].left = fourSquares[0].left-20
			fourSquares[0].top = fourSquares[0].top+20
			fourSquares[2].left = fourSquares[2].left+20
			fourSquares[2].top = fourSquares[2].top-20
			fourSquares[3].left = fourSquares[3].left+40
			fourSquares[3].top = fourSquares[3].top-40
			self.state+=1
			self.state = self.state%4 + 1
		elif self.state == 4:
			fourSquares[0].left = fourSquares[0].left-20
			fourSquares[0].top = fourSquares[0].top-20
			fourSquares[2].left = fourSquares[2].left+20
			fourSquares[2].top = fourSquares[2].top+20
			fourSquares[3].left = fourSquares[3].left+40
			fourSquares[3].top = fourSquares[3].top+40
			self.state+=1
			self.state = self.state%4 + 1

	def left(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left-20<0:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left -= 20

	def right(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left+20>400:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left += 20

	def down(self):
		for i in range(0,4):
			fourSquares[i].top += 20


class square:
	# def __init__(self):
	# 	self.state = 1

	def begin(self):
		fourSquares = []
		for i in range(9,10):
			fourSquares.append(pygame.Rect(i*(rectLength+2)+1,0+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(i*(rectLength+2)+1,20+1,rectLength,rectLength))

	# 
	def rotate(self):
		fourSquares[0].left = fourSquares[0].left
		fourSquares[0].top = fourSquares[0].top
		fourSquares[1].left = fourSquares[1].left
		fourSquares[1].top = fourSquares[1].top
		fourSquares[2].left = fourSquares[2].left
		fourSquares[2].top = fourSquares[2].top
		fourSquares[3].left = fourSquares[3].left
		fourSquares[3].top = fourSquares[3].top
		
	def left(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left-20<0:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left -= 20

	def right(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left+20>400:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left += 20

	def down(self):
		for i in range(0,4):
			fourSquares[i].top += 20


class mountain:
	def __init__(self):
		self.state = 1

	def begin(self):
		fourSquares = []
		fourSquares.append(pygame.Rect(10*(rectLength+2)+1,0+1,rectLength,rectLength))
		for i in range(9,12):
			fourSquares.append(pygame.Rect(i*(rectLength+2)+1,20+1,rectLength,rectLength))

	# 
	def rotate(self):
		if self.state == 1:
			fourSquares[0].left = fourSquares[0].left+20
			fourSquares[0].top = fourSquares[0].top+20
			fourSquares[1].left = fourSquares[1].left+20
			fourSquares[1].top = fourSquares[1].top-20
			fourSquares[3].left = fourSquares[3].left-20
			fourSquares[3].top = fourSquares[3].top+20
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 2:
			fourSquares[0].left = fourSquares[0].left-20
			fourSquares[0].top = fourSquares[0].top+20
			fourSquares[1].left = fourSquares[1].left+20
			fourSquares[1].top = fourSquares[1].top+20
			fourSquares[3].left = fourSquares[3].left-20
			fourSquares[3].top = fourSquares[3].top-20
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 3:
			fourSquares[0].left = fourSquares[0].left-20
			fourSquares[0].top = fourSquares[0].top-20
			fourSquares[1].left = fourSquares[1].left-20
			fourSquares[1].top = fourSquares[1].top+20
			fourSquares[3].left = fourSquares[3].left+20
			fourSquares[3].top = fourSquares[3].top-20
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 4:
			fourSquares[0].left = fourSquares[0].left+20
			fourSquares[0].top = fourSquares[0].top-20
			fourSquares[1].left = fourSquares[1].left-20
			fourSquares[1].top = fourSquares[1].top-20
			fourSquares[3].left = fourSquares[3].left+20
			fourSquares[3].top = fourSquares[3].top+20
			self.state+=1
			if self.state>4:
				self.state-=4

	def left(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left-20<0:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left -= 20

	def right(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left+20>400:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left += 20

	def down(self):
		for i in range(0,4):
			fourSquares[i].top += 20

class snake1:
	def __init__(self):
		self.state = 1

	def begin(self):
		fourSquares = []
		fourSquares.append(pygame.Rect(9*(rectLength+2)+1,0+1,rectLength,rectLength))
		fourSquares.append(pygame.Rect(10*(rectLength+2)+1,0+1,rectLength,rectLength))
		fourSquares.append(pygame.Rect(10*(rectLength+2)+1,20+1,rectLength,rectLength))
		fourSquares.append(pygame.Rect(11*(rectLength+2)+1,20+1,rectLength,rectLength))
	# 
	def rotate(self):
		if self.state == 1:
			fourSquares[0].left = fourSquares[0].left+40
			# fourSquares[0].top = fourSquares[0].top+20
			fourSquares[1].left = fourSquares[1].left+20
			fourSquares[1].top = fourSquares[1].top+20
			fourSquares[3].left = fourSquares[3].left-20
			fourSquares[3].top = fourSquares[3].top+20
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 2:
			# fourSquares[0].left = fourSquares[0].left-20
			fourSquares[0].top = fourSquares[0].top+40
			fourSquares[1].left = fourSquares[1].left-20
			fourSquares[1].top = fourSquares[1].top+20
			fourSquares[3].left = fourSquares[3].left-20
			fourSquares[3].top = fourSquares[3].top-20
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 3:
			fourSquares[0].left = fourSquares[0].left-40
			# fourSquares[0].top = fourSquares[0].top-20
			fourSquares[1].left = fourSquares[1].left-20
			fourSquares[1].top = fourSquares[1].top-20
			fourSquares[3].left = fourSquares[3].left+20
			fourSquares[3].top = fourSquares[3].top-20
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 4:
			# fourSquares[0].left = fourSquares[0].left+20
			fourSquares[0].top = fourSquares[0].top-40
			fourSquares[1].left = fourSquares[1].left+20
			fourSquares[1].top = fourSquares[1].top-20
			fourSquares[3].left = fourSquares[3].left+20
			fourSquares[3].top = fourSquares[3].top+20
			self.state+=1
			if self.state>4:
				self.state-=4

	def left(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left-20<0:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left -= 20

	def right(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left+20>400:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left += 20

	def down(self):
		for i in range(0,4):
			fourSquares[i].top += 20

class snake2:
	def __init__(self):
		self.state = 1

	def begin(self):
		fourSquares = []
		fourSquares.append(pygame.Rect(11*(rectLength+2)+1,0+1,rectLength,rectLength))
		fourSquares.append(pygame.Rect(10*(rectLength+2)+1,0+1,rectLength,rectLength))
		fourSquares.append(pygame.Rect(10*(rectLength+2)+1,20+1,rectLength,rectLength))
		fourSquares.append(pygame.Rect(9*(rectLength+2)+1,20+1,rectLength,rectLength))
	# 
	def rotate(self):
		if self.state == 1:
			# fourSquares[0].left = fourSquares[0].left+40
			fourSquares[0].top = fourSquares[0].top+40
			fourSquares[1].left = fourSquares[1].left+20
			fourSquares[1].top = fourSquares[1].top+20
			fourSquares[3].left = fourSquares[3].left+20
			fourSquares[3].top = fourSquares[3].top-20
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 2:
			fourSquares[0].left = fourSquares[0].left-40
			# fourSquares[0].top = fourSquares[0].top+40
			fourSquares[1].left = fourSquares[1].left-20
			fourSquares[1].top = fourSquares[1].top+20
			fourSquares[3].left = fourSquares[3].left+20
			fourSquares[3].top = fourSquares[3].top+20
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 3:
			# fourSquares[0].left = fourSquares[0].left-40
			fourSquares[0].top = fourSquares[0].top-40
			fourSquares[1].left = fourSquares[1].left-20
			fourSquares[1].top = fourSquares[1].top-20
			fourSquares[3].left = fourSquares[3].left-20
			fourSquares[3].top = fourSquares[3].top+20
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 4:
			fourSquares[0].left = fourSquares[0].left+40
			# fourSquares[0].top = fourSquares[0].top-40
			fourSquares[1].left = fourSquares[1].left+20
			fourSquares[1].top = fourSquares[1].top-20
			fourSquares[3].left = fourSquares[3].left-20
			fourSquares[3].top = fourSquares[3].top-20
			self.state+=1
			if self.state>4:
				self.state-=4

	def left(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left-20<0:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left -= 20

	def right(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left+20>400:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left += 20

	def down(self):
		for i in range(0,4):
			fourSquares[i].top += 20

class lType1:
	def __init__(self):
		self.state = 1

	def begin(self):
		fourSquares = []
		fourSquares.append(pygame.Rect(9*(rectLength+2)+1,0+1,rectLength,rectLength))
		fourSquares.append(pygame.Rect(9*(rectLength+2)+1,20+1,rectLength,rectLength))
		fourSquares.append(pygame.Rect(10*(rectLength+2)+1,20+1,rectLength,rectLength))
		fourSquares.append(pygame.Rect(11*(rectLength+2)+1,20+1,rectLength,rectLength))
	
	# 
	def rotate(self):
		if self.state == 1:
			fourSquares[0].left = fourSquares[0].left+20
			fourSquares[0].top = fourSquares[0].top+20
			fourSquares[2].left = fourSquares[2].left-20
			fourSquares[2].top = fourSquares[2].top+20
			fourSquares[3].left = fourSquares[3].left-40
			fourSquares[3].top = fourSquares[3].top+40
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 2:
			fourSquares[0].left = fourSquares[0].left-20
			fourSquares[0].top = fourSquares[0].top+20
			fourSquares[2].left = fourSquares[2].left-20
			fourSquares[2].top = fourSquares[2].top-20
			fourSquares[3].left = fourSquares[3].left-40
			fourSquares[3].top = fourSquares[3].top-40
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 3:
			fourSquares[0].left = fourSquares[0].left-20
			fourSquares[0].top = fourSquares[0].top-20
			fourSquares[2].left = fourSquares[2].left+20
			fourSquares[2].top = fourSquares[2].top-20
			fourSquares[3].left = fourSquares[3].left+40
			fourSquares[3].top = fourSquares[3].top-40
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 4:
			fourSquares[0].left = fourSquares[0].left+20
			fourSquares[0].top = fourSquares[0].top-20
			fourSquares[2].left = fourSquares[2].left+20
			fourSquares[2].top = fourSquares[2].top+20
			fourSquares[3].left = fourSquares[3].left+40
			fourSquares[3].top = fourSquares[3].top+40
			self.state+=1
			if self.state>4:
				self.state-=4

	def left(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left-20<0:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left -= 20

	def right(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left+20>400:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left += 20

	def down(self):
		for i in range(0,4):
			fourSquares[i].top += 20

class lType2:
	def __init__(self):
		self.state = 1

	def begin(self):
		fourSquares = []
		fourSquares.append(pygame.Rect(11*(rectLength+2)+1,0+1,rectLength,rectLength))
		fourSquares.append(pygame.Rect(11*(rectLength+2)+1,20+1,rectLength,rectLength))
		fourSquares.append(pygame.Rect(10*(rectLength+2)+1,20+1,rectLength,rectLength))
		fourSquares.append(pygame.Rect(9*(rectLength+2)+1,20+1,rectLength,rectLength))
	
	# 
	def rotate(self):
		if self.state == 1:
			fourSquares[0].left = fourSquares[0].left+20
			fourSquares[0].top = fourSquares[0].top+20
			fourSquares[2].left = fourSquares[2].left+20
			fourSquares[2].top = fourSquares[2].top-20
			fourSquares[3].left = fourSquares[3].left+40
			fourSquares[3].top = fourSquares[3].top-40
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 2:
			fourSquares[0].left = fourSquares[0].left-20
			fourSquares[0].top = fourSquares[0].top+20
			fourSquares[2].left = fourSquares[2].left+20
			fourSquares[2].top = fourSquares[2].top+20
			fourSquares[3].left = fourSquares[3].left+40
			fourSquares[3].top = fourSquares[3].top+40
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 3:
			fourSquares[0].left = fourSquares[0].left-20
			fourSquares[0].top = fourSquares[0].top-20
			fourSquares[2].left = fourSquares[2].left-20
			fourSquares[2].top = fourSquares[2].top+20
			fourSquares[3].left = fourSquares[3].left-40
			fourSquares[3].top = fourSquares[3].top+40
			self.state+=1
			if self.state>4:
				self.state-=4
		elif self.state == 4:
			fourSquares[0].left = fourSquares[0].left+20
			fourSquares[0].top = fourSquares[0].top-20
			fourSquares[2].left = fourSquares[2].left-20
			fourSquares[2].top = fourSquares[2].top-20
			fourSquares[3].left = fourSquares[3].left-40
			fourSquares[3].top = fourSquares[3].top-40
			self.state+=1
			if self.state>4:
				self.state-=4

	def left(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left-20<0:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left -= 20

	def right(self):
		flag = 1
		for i in range(0,4):
			if fourSquares[i].left+20>400:
				flag = 0
				break
		if flag:
			for i in range(0,4):
				fourSquares[i].left += 20

	def down(self):
		for i in range(0,4):
			fourSquares[i].top += 20
	
def gameOver(f,scores):
	print >> f, "%d" % (scores)
	f.close()
	windowSurface.fill(BLACK)
	fr = open("out.txt","r")
	data = []
	readin_data(fr,data)
	data = sort(data)
	show_data(data)
	# print data
	pygame.display.update()   
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		show_text(windowSurface, (50,50), "game over",WHITE,BLACK,False,64,False)
		show_text(windowSurface, (50,150), "scores:"+str(scores),WHITE,BLACK,False,64,False)
		show_data(data)
		pygame.display.update()
		mainClock.tick(10)

def readin_data(file,data):
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

def draw():
	windowSurface.fill(BLACK)
	for i in range(len(fourSquares)):
		windowSurface.blit(HKC,(fourSquares[i].left,fourSquares[i].top),(10,10,18,18))
		# pygame.draw.rect(windowSurface,GREEN,fourSquares[i])
	for i in range(0,30):
		for j in range(0,20):
			if chessBoard[i][j]:
				windowSurface.blit(HKC,(j*20+1,i*20+1),(10,10,18,18))
				# pygame.draw.rect(windowSurface,GREEN,((j*20+1,i*20+1),(18,18)))
	pygame.display.update()

def checkAndPut(fourSquares,chessBoard):
	can = 0
	for i in range(0,4):
		if (fourSquares[i].top-1)/20+1>=30 or chessBoard[(fourSquares[i].top-1)/20+1][(fourSquares[i].left-1)/20]:
			can = 1
			break
	if can:
		for i in range(0,4):
			if chessBoard[(fourSquares[i].top-1)/20][(fourSquares[i].left-1)/20]:
				gameOver(f,scores)
			else:
				chessBoard[(fourSquares[i].top-1)/20][(fourSquares[i].left-1)/20]=1
		if died(chessBoard):
			gameOver(f,scores)
		return 1
	return 0

def DeleteLine(chessBoard,scores):
	i = 29
	while i>= 0 :
		flag = 1
		for j in range(0,20):
			if not chessBoard[i][j]:
				flag = 0
				break;
		if flag:
			scores += 1
			for j in range(0,20):
				chessBoard[i][j] = 0
			k = i-1
			while k>=0:
				for l in range(0,20):
					if chessBoard[k][l]:
						chessBoard[k][l] = 0
						chessBoard[k+1][l] = 1
				k -= 1
		i -= 1
	return scores
			
def died(chessBoard):
	isDied = 0
	for i in range(0,20):
		if chessBoard[0][i]==1:
			isDied = 1
			break
	return isDied

def show_text(surface_handle,pos,text,color,back_color = (255,255,255),font_bold = False, font_size = 13, font_italic = False):
	cur_font = pygame.font.SysFont("Courier New",font_size)
	cur_font.set_bold(font_bold)
	cur_font.set_italic(font_italic)
	text_fmt = cur_font.render(text,1,color,back_color)
	surface_handle.blit(text_fmt,pos)


which = 1
thing = mountain()
ispressed = 0
f = open("out.txt","a")
# data = []
# for i in range(8,12):
# 	fourSquares.append(pygame.Rect(i*(rectLength+2)+1,0+1,rectLength,rectLength))
# draw()
# pygame.display.update()

# DeleteLine(chessBoard)
# draw()
# pygame.display.update()
# while True:
# 	draw()
# 	pygame.display.update()

# for i in range(9,11):
# 	fourSquares.append(pygame.Rect(i*(rectLength+2)+1,0+1,rectLength,rectLength))
# 	fourSquares.append(pygame.Rect(i*(rectLength+2)+1,20+1,rectLength,rectLength))
# draw()
# pygame.display.update()


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


fourSquares.append(pygame.Rect(10*(rectLength+2)+1,0+1,rectLength,rectLength))
for i in range(9,12):
	fourSquares.append(pygame.Rect(i*(rectLength+2)+1,20+1,rectLength,rectLength))
draw()
pygame.display.update()



while True:
	# draw()
	# pygame.display.update()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			ispressed = 1
			if event.key == K_SPACE:
				thing.rotate()
			elif event.key == K_LEFT:
				thing.left()
			elif event.key == K_RIGHT:
				thing.right()
	if not ispressed:
		thing.down()
	if checkAndPut(fourSquares,chessBoard):
		scores = DeleteLine(chessBoard,scores)
		draw()
		pygame.display.update()
		which = random.randint(1,TOTAL)
		fourSquares = []
		if which == 1:
			thing = bar()
			for i in range(8,12):
				fourSquares.append(pygame.Rect(i*(rectLength+2)+1,0+1,rectLength,rectLength))
		elif which == 2:
			thing = square()
			for i in range(9,11):
				fourSquares.append(pygame.Rect(i*(rectLength+2)+1,0+1,rectLength,rectLength))
				fourSquares.append(pygame.Rect(i*(rectLength+2)+1,20+1,rectLength,rectLength))
		elif which == 3:
			thing = mountain()
			fourSquares.append(pygame.Rect(10*(rectLength+2)+1,0+1,rectLength,rectLength))
			for i in range(9,12):
				fourSquares.append(pygame.Rect(i*(rectLength+2)+1,20+1,rectLength,rectLength))
		elif which == 4:
			thing = snake1()
			fourSquares.append(pygame.Rect(9*(rectLength+2)+1,0+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(10*(rectLength+2)+1,0+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(10*(rectLength+2)+1,20+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(11*(rectLength+2)+1,20+1,rectLength,rectLength))
		elif which == 5:
			thing = snake2()
			fourSquares.append(pygame.Rect(11*(rectLength+2)+1,0+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(10*(rectLength+2)+1,0+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(10*(rectLength+2)+1,20+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(9*(rectLength+2)+1,20+1,rectLength,rectLength))
		elif which == 6:
			thing = lType1()
			fourSquares.append(pygame.Rect(9*(rectLength+2)+1,0+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(9*(rectLength+2)+1,20+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(10*(rectLength+2)+1,20+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(11*(rectLength+2)+1,20+1,rectLength,rectLength))
		elif which == 7:
			thing = lType2()
			fourSquares.append(pygame.Rect(11*(rectLength+2)+1,0+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(11*(rectLength+2)+1,20+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(10*(rectLength+2)+1,20+1,rectLength,rectLength))
			fourSquares.append(pygame.Rect(9*(rectLength+2)+1,20+1,rectLength,rectLength))

	draw()
	pygame.draw.line(windowSurface,WHITE,(400,0),(400,600),1)
	show_text(windowSurface,(430,30), str(scores), WHITE,BLACK,False,64,False)
	pygame.display.update()
	ispressed = 0
	print 'len'+str(len(fourSquares))
	print 'which'+str(which)
	mainClock.tick(10)






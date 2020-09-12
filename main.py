import Solver
import pygame as pg
from pygame.locals import *
import time
size = 50 						# size of a square in px
bg_white = (112,128,144)		# chess black square bg color
bg_black = (47,79,79)			# chessboard white square bg color


def ask(screen):
	screen.fill(bg_black)
	pg.display.update()
	clock = pg.time.Clock()
	font = pg.font.Font(None, 32)
	done = False
	inp = ""
	while not done:
		for event in pg.event.get():
			surf = font.render("Enter dimension of chessboard then press ENTER: "+inp, True, (0,0,0), bg_black)
			rect = surf.get_rect()
			rect.center = (400, 100)
			screen.blit(surf,rect)
			pg.display.update()
			if event.type == pg.QUIT:
				done = True
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					done = True
				elif event.key == pg.K_BACKSPACE:
					inp = inp[:-1]
				else:
					inp+=event.unicode
	return inp
	clock.tick(30)

def drawSoln(screen, soln, posArray):
	img = [pg.transform.scale(pg.image.load('img/dark.png'), (size,size))]
	img.append(pg.transform.scale(pg.image.load('img/light.png'), (size,size)))
	col = 0
	print(soln)
	for i in soln:
		time.sleep(0.7)
		x,y = posArray[col][i]
		screen.blit(img[(i+col)%2], (x,y))
		col+=1
		pg.display.update()

def main():
	screen = pg.display.set_mode((800,200))
	pg.display.set_caption('Enter N:')
	icon = pg.image.load('img/dark.png')
	pg.display.set_icon(icon)
	pg.display.update()
	n=int(ask(screen))
	done = False
	screen.fill(bg_black)
	screen = pg.display.set_mode((size*n, size*n))
	pg.display.set_caption('Solution of N Queens')
	posArray = []
	
	for x in range(n):
		tempPos = []
		for y in range(n):
			tempPos.append((size*(x), size*(y)))
			if((x+y)&1^1):
				pg.draw.rect(screen, bg_white, (x*size, y*size, size, size))
		posArray.append(tempPos)
	
	soln = Solver.solver([], n)
	
	if soln:
		drawSoln(screen, soln, posArray)
	else:
		screen = pg.display.set_mode((800,200))
		font = pg.font.Font(None, 32)
		surf = font.render("Solution does not Exist!", True, (0,0,0), bg_black)
		rect = surf.get_rect()
		rect.center = (400, 100)
		screen.blit(surf,rect)
	
	pg.display.update()
	
	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				done = True



if __name__=="__main__":
	pg.init()
	main()
	pg.quit()
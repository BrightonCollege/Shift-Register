# Harry Beadle - Brighton College
# BCES - Brighton College Engineering Society

## Shift Register Simulator

import pygame
pygame.init()

display = pygame.display.set_mode((500,500))
pygame.display.set_caption('Shift Register')

data = True
size = 20

def bit(d):
	surface = pygame.Surface((size,size))
	if d:
		surface.fill((255,0,0))
	else:
		surface.fill((255,255,255))
	return surface

latched = [False for x in range(0,8)]
unlatched = [False for x in range(0,8)]

display.blit(bit(data), (0, 2*size))
display.blit(bit(data), (0, 4*size))

def clock():
	global data
	unlatched.insert(0, data)
	del unlatched[len(unlatched)-1]
	i = 0
	for d in unlatched:
		display.blit(bit(d), (2*size, i))
		i += 2*size
	pygame.display.flip()

def latch():
	global data
	latched = unlatched
	i = 0
	for d in latched:
		display.blit(bit(d), (4*size, i))
		i += 2*size
	i = 0
	for d in unlatched:
		display.blit(bit(d), (2*size, i))
		i += 2*size
	pygame.display.flip()

def dataline():
	global data
	data = not data
	display.blit(bit(data), (0,0))
	pygame.display.flip()

if __name__ == '__main__':
	clock()
	latch()
	dataline()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				posx, posy = pygame.mouse.get_pos()
				if 0 <= posy <= size:
					dataline()
				if 2*size <= posy <= 3*size:
					clock()
				if 4*size <= posy <= 5*size:
					latch()
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
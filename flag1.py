# flag1.py
# Christopher Mulkey
# 11/05/2012
# Lab 1


import pygame

width, height = 640, 480

def init():
	pygame.init()
                                # Screen

        return pygame.display.set_mode((width, height)
        

def draw_flag(screen):
	screen.fill((0,0,104))		# Pale blue background

	pygame.draw.circle(0, 0, 255) 	# Blue 
	pygame.draw.circle(255, 255, 0) # Yellow
	pygame.draw.circle(0, 0, 0) 	# Black
	pygame.draw.circle(0, 255, 0) 	# Green
	pygame.draw.circle(255, 0, 0)	# Red
	pygame.draw.rect(255, 255, 255) # White Outline

def main(screen):
	running = True
	while running:
		draw_flag(screen)
		pygame.display.flip() 	# Display screen in window
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key ==pygame.K_q): run = False

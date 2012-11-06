# basic_flag.py
# christopher mulkey
# 11/05/2012
# lab 1

import pygame

width = 640
height = 480

pygame.init()

screen = pygame.display.set_mode((width, height)) # Screen


screen.fill(0, 0, 0)            # Black Background
pygame.draw.rect(0, 0, 104)     # White Flag Background
pygame.draw.circle(0, 0, 255)   # Blue
pygame.draw.circle(255, 255, 0)	# Yellow
pygame.draw.circle(0, 0, 0)	# Black
pygame.draw.circle(0, 255, 0)	# Green
pygame.draw.circle(255, 0, 0)	# Red

running = True
for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key ==pygame.K_q : run = False


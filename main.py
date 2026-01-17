import sys, pygame
pygame.init()


#Window data 
win_size  = win_width, win_height  =  400 , 900
win  = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("First Game")


# Character info
# obj 1 ball
b_cord = bx, by = win_width//2, win_height//2
b_radius = 5
b_color = (255, 0, 0)
bvx , bvy = 0, 0

# obj 2 striker
sx, sy = win_width//2, win_height-15
s_dim = 50,5
s_color = (100, 100, 100)

running = True
while running:
	pygame.time.delay(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


	# controls for striker
	keys = pygame.key.get_pressed()

	if keys[pygame.K_RIGHT] and sx+4<=win_width- s_dim[0]:
			sx+=4

	if keys[pygame.K_LEFT] and sx-4>=4:
			sx-=4






	# drawing on the screen
	win.fill((0,0,0))
	pygame.draw.circle(win, b_color, (bx,by), b_radius)
	pygame.draw.rect(win, s_color, (sx,sy, *s_dim))
	pygame.display.update()


pygame.quit()
sys.exit()

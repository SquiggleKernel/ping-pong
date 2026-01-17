import sys, pygame , random
pygame.init()


#Window data 
win_size  = win_width, win_height  =  400 , 700
win  = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("First Game")

points =0 

# Character info
# obj 1 ball
bx, by = win_width//2, win_height//2
b_radius = 5
b_color = (255, 0, 0)
bvx , bvy = random.randint(4,5), 5

# obj 2 striker
sx, sy = win_width//2, win_height-15
s_dim = 70,5
s_color = (255, 255 , 255)

font = pygame.font.SysFont("Arial", 18)
fontb = pygame.font.SysFont("Arial", 40)

running = True
while running:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # controls for striker
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and sx+8<=win_width- s_dim[0]:
            sx+=8

    if keys[pygame.K_LEFT] and sx-8>=8:
            sx-=8;
    
    # updating ball position
    bx += bvx
    by += bvy

    # making collision with wall working
    if bx> win_width- b_radius:
        bvx*=-1
        bx = win_width-b_radius
    if bx < b_radius:
        bvx*=-1
        bx = b_radius
    if by < b_radius:
        bvy=bvy*(-1) +1
        by= b_radius



    if by > win_height:
        by = 0


    if  by>=win_height-15:
        if bx<sx+s_dim[0] and bx > sx:
            bvy*=-1
            by = win_height - 16 - b_radius
            points +=1
        else:
            win.blit(fontb.render(f"GAME OVER", True, (255, 255, 255)), (50,200))
            win.blit(fontb.render(f"Points: {points}", True, (255, 255, 255)), (50,260))


            try:
                with open("highscore.txt", "r") as f:
                    saved_value = int(f.read())
            except FileNotFoundError:
                print("file not FileNotFoundError")
                saved_value = 0 # Default if file doesn't exist yet
            if saved_value< points:
                with open("highscore.txt", "w") as f:
                    f.write(str(points)) # Convert the value to a string
            win.blit(fontb.render(f"High Score: {saved_value}", True, (255, 255, 255)), (50,320))

            pygame.display.update()
            running= False
            break

    # drawing on the screen
    win.fill((0,0,0))

    # font name , size
    try:
        with open("highscore.txt", "r") as f:
            saved_value = int(f.read())
    except FileNotFoundError:
        print("file not FileNotFoundError")
        saved_value = 0 
    ball_pos_text = font.render(f"Highscore: {saved_value}", True, (255, 255, 255))
    win.blit(ball_pos_text, (20, 20))
    win.blit(font.render(f"Points: {points}", True, (255, 255, 255)), (20,40))


    pygame.draw.circle(win, b_color, (bx,by), b_radius)
    pygame.draw.rect(win, s_color, (sx,sy, *s_dim))
    pygame.display.update()




pygame.display.update()
pygame.time.delay(3000)
pygame.quit()
sys.exit()

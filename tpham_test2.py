import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)



font = pygame.font.Font(None, 25)
clock = pygame.time.Clock()
scorelist = []




# Variables
frame_count = 0
frame_rate = 60
#main loopps
running = True
start = False
#clock stuff
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    total_seconds = frame_count / frame_rate  # total seconds passed
    roundedtime=round(total_seconds,2)# rounds time to 2 decimal places
    score= f"Time: {roundedtime}" # displays score
    text = font.render(score, True, BLACK) # render _ display
    screen.blit(text, [250, 250])
    frame_count += 66.6
    pygame.display.flip()
    clock.tick(frame_rate)
pygame.quit()


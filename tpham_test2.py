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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    total_seconds = frame_count // frame_rate  # total seconds passed
    score= f"Time: {total_seconds}"
    text = font.render(score, True, BLACK) # render _ display
    
    screen.blit(text, [250, 250])
    frame_count += 1
    pygame.display.flip()
    clock.tick(frame_rate)
   
pygame.quit()


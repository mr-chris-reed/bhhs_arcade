import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Timer Example")


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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and start == False:
                start = True
            elif event.key == pygame.K_LEFT and start == True:
                start = False

    
    screen.fill(WHITE)

    total_seconds = frame_count // frame_rate  # total seconds passed
    score= f"Time: {total_seconds}"
    
    # render _ display
    text = font.render(score, True, BLACK)
    if start:
        screen.blit(text, [250, 250])

       
        frame_count += 1
        pygame.display.flip()

        
        clock.tick(frame_rate)
    #elif not start and
     #   print(score)
#
pygame.quit()

#reminder of me, make it work so only after a button is pressed the timer starts and after another is pressed it resets
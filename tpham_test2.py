import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Timer Example")

# Set up font and clock
font = pygame.font.Font(None, 25)
clock = pygame.time.Clock()

# Variables
frame_count = 0
frame_rate = 60
#main loopps
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

    total_seconds = frame_count // frame_rate  # Total seconds passed
    output_string = f"Time: {total_seconds}"

    # render _ display
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 250])

    # Update frame count and display
    frame_count += 1
    pygame.display.flip()

    # Limit frames per second
    clock.tick(frame_rate)

# Close pygame properly
pygame.quit()

#reminder of me, make it work so only after a button is pressed the timer starts and after another is pressed it resets
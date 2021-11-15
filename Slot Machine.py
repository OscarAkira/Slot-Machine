import pygame

# Setup the window
pygame.init()
width = 700
height = 550
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slot Machine Game @Oscar")
logo = pygame.image.load('Assets/slot-machine.png')
pygame.display.set_icon(logo)
white = [250, 250, 250]
screen.fill(white)

# Load background image
background = pygame.image.load('Assets/slot-machine.png')



# Main loop
run = True
while run:
    screen.fill(white)
    # draw the bg image
    screen.blit(background, (0, 0))
    # update screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
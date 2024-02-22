import pygame
import math 


pygame.init()

#Background variables 
height = 400
width = 1600


screen = pygame.display.set_mode((width,height))

#general surface 
ground_surface = pygame.image.load('graphics/symbols/ground.png').convert()
sky_surface = pygame.image.load('graphics/symbols/sky.png').convert()

background_width = ground_surface.get_width()
#without +1 the background is blurry for a moment 
titles = math.ceil( width / background_width) + 1


clock = pygame.time.Clock()
game_active = True
player_gravity = 0
pygame.display.set_caption('untilted02')
scroll = 0

while game_active:
    for i in range(0,titles):
        screen.blit(ground_surface,(i * background_width + scroll,300))
        screen.blit(sky_surface,(i * background_width + scroll,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
 
    #scroll background
    scroll -= 1

    #reset scroll
    if abs(scroll) > background_width:
        scroll = 0


    pygame.display.update() 
    clock.tick(120)


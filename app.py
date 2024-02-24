import pygame
import math 


pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
        
        if keys[pygame.K_d] and self.rect.bottom >= 300:
                self.rect.x += 1

        if keys[pygame.K_a] and self.rect.bottom >= 300:
                self.rect.x -= 1

    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):

        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class MovementObstacle(pygame.sprite.Sprite):
    pass




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

player = pygame.sprite.GroupSingle()
player.add(Player())

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

    #player
    player.draw(screen)
    player.update()

    pygame.display.update() 
    clock.tick(120)


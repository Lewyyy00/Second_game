import pygame
import math 
from random import randint, choice


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
        
        if keys[pygame.K_d]:
            self.rect.x += 1

        if keys[pygame.K_a]:
            self.rect.x -= 1

        #if keys[pygame.K_d] and keys[pygame.K_SPACE]:
         #   self.rect.y =   
          #  self.rect.x -= 1

    
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

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'fly':
            fly_frame_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210

        else:
            snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(1500,1600),y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy 

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.level_ground = pygame.image.load('graphics/symbols/ground.png').convert_alpha()
        self.rect = self.level_ground.get_rect(midbottom = (x ,y))



#Background variables 
height = 400
width = 1200 

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else:
        return True

screen = pygame.display.set_mode((width,height))

#general surface 
ground_surface = pygame.image.load('graphics/symbols/ground.png').convert()
sky_surface = pygame.image.load('graphics/symbols/sky.png').convert()

background_width = ground_surface.get_width()
#without +1 the background is blurry for a moment 
titles = math.ceil( width / background_width) + 1

player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()

#platform
platforms = pygame.sprite.Group()
platform1 = Platform(100,100)
platform2 = Platform(100,200)
platforms.add(platform1, platform2)

clock = pygame.time.Clock()
game_active = True
pygame.display.set_caption('untilted02')
scroll = 0

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 200)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while game_active:
    for i in range(0,titles):
        screen.blit(ground_surface,(i * background_width + scroll,300))
        screen.blit(sky_surface,(i * background_width + scroll,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == obstacle_timer:
            obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
    
    #scroll background
    scroll -= 1

    #reset scroll
    if abs(scroll) > background_width:
        scroll = 0

    #player
    player.draw(screen)
    player.update()

    obstacle_group.draw(screen)
    obstacle_group.update()

    game_active = collision_sprite()

    #nie działa 
    hit = pygame.sprite.spritecollide(player.sprite,platforms,False)
    if hit:
        player.gravity = 0

    pygame.display.update() 
    clock.tick(120)


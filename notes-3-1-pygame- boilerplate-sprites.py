# intro to pygame
#   -boilerplate is useful to set up our environments
#   -the sprite class has some really cool things in it 

import random
import pygame
# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)
NUM_LOGOS = 20
#create a class representing the dvd logo
#   -child-class of pygame sprites
#   -create a constructor method
#       -image -> visual representation
#       - rect -> hitbox 
class Dvdlogo(pygame.sprite.Sprite):
    """represents DVD logo sprite"""
    def __init__(self):
        super().__init__()
        
        
        #image -> visual rep
        self.image = pygame.image.load("./images/dvd-logo.png")
        
        #rect -> hitbox rep
        #get_rect() -> rect
        #   [x,y width,height]

        self.rect = self.image.get_rect()

        # spawn in a random location 
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)



        # velocity og the Dvd logo
        self.vel_x = random.choice([-6, -5, -4, -3, 3, 4, 5, 6])
        self.vel_y = random.choice([-6, -5, -4, -3, 3, 4, 5, 6])
    
    def update(self):
        # update the location of the dvd logo
        self.rect.x += self.vel_x 
        self.rect.y += self.vel_y

        # # bounce if reaches bottom
        # # if the bottom of the sprite is past the bottom of the screen 
        # # convert to negative (* -1)
        if self.rect.bottom > HEIGHT:
            self.vel_y *= -1

        # top 
        if self.rect.top < 0:
            self.vel_y *= -1
      
        # left
        if self.rect.left < 0:
            self.vel_x *= -1

        # right
        if self.rect.right > WIDTH:
            self.vel_x *= -1



def start():
    """Environment Setup and Game Loop"""

    pygame.init()

    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    pygame.display.set_caption("DVD Logo Sreensaver")

    dvdlogo = Dvdlogo()

    #make a dvd logo object
    dvdlogo = Dvdlogo()

    #create a group of sprites
    all_sprites = pygame.sprite.Group()

    #move the dvd logo to middle 
    dvdlogo.rect.centerx = WIDTH // 2
    dvdlogo.rect.centery = HEIGHT // 2

    #create a group of sprites
    all_sprites = pygame.sprite.Group()

    #add the dvd logo to the group of sprite
    for _ in range(1):
        all_sprites.add(Dvdlogo())

    
    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # if space is pressed, create a new dvd logo
            # and add it to all_sprites
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    all_sprites.add(Dvdlogo())

        # --- Update the world state
        # TODO: update the location of the dvd logo 
        all_sprites.update()
      
        # --- Draw items
        screen.fill(BLACK)

        #draw all sprites on the screen
        all_sprites.draw(screen)

        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()


























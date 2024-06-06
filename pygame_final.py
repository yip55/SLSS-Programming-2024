# pygae final project 
# author: odyssa yip

import pygame as pg
import random 

NUM_ENEMIES = 5
# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 700  # Pixels
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)

# Create a background class
class Background(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./Images/background.jpeg")
        self.image = pg.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/galaga_ship.png")

        self.rect = self.image.get_rect()

        # Start it in the bottom middle
        self.rect.bottom = HEIGHT
        self.rect.centerx = WIDTH // 2

        self.change_x = 0
        self.change_y = 0
        
        self.lives_remaining = 9
    def update(self):
        # Move left/right
        self.rect.x += self.change_x

        # Make sure it stays in the screen (left)
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH 
        if self.rect.top <= 0:
            self.rect.top = 0 
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        
        # Move up/down
        self.rect.y += self.change_y

    
    # Player-controlled movement:
    def go_left(self):
        self.change_x = -6
 
    def go_right(self):
        self.change_x = 6
    
    def go_up(self):
        self.change_y = -6

    def go_down(self):
        self.change_y = 6
 
    def stop_x(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

    def stop_y(self):
        self.change_y = 0

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/twomp.png")
        self.image = pg.transform.scale(self.image, (107, 120))
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - 400)

        self.vel_y = random.choice(( 4, 5, 6 ))
        


    def update(self):
        self.rect.y += self.vel_y
        if self.rect.top > HEIGHT:
            # Change the x coordinate as well
            self.rect.y = -10
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)




def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()
    score = 0
    font = pg.font.SysFont("Furtura", 24)

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    enemy_sprites = pg.sprite.Group()
    player_sprites = pg.sprite.Group()
    background_group = pg.sprite.Group()
    # create a Player sprite object
    player = Player()

    all_sprites.add(player)
    
    # Background creation
    bg = Background()
    background_group.add(bg)
                         
    for _ in range(NUM_ENEMIES):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
    pg.display.set_caption("< Pew Pew >")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    player.go_left()
                if event.key == pg.K_RIGHT:
                    player.go_right()
                if event.key == pg.K_UP:
                    player.go_up()
                if event.key == pg.K_DOWN:
                    player.go_down()
 
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and player.change_x < 0:
                    player.stop_x()
                if event.key == pg.K_RIGHT and player.change_x > 0:
                    player.stop_x()
                if event.key == pg.K_UP and player.change_y < 0:
                    player.stop_y()
                if event.key == pg.K_DOWN and player.change_y > 0:
                    player.stop_y()
        
        # Detect collision with enemies
        enemies_collided = pg.sprite.spritecollide(player, enemy_sprites, False)
        
        # Iterate through enemies collided to notify in console
        for enemy in enemies_collided:
            # Decrease player's life by one life per second
            player.lives_remaining -= 1 / 60

            if player.lives_remaining <= 0:
                done = True


            # Print player's current lives remaining
            print(f"Lives: {int(player.lives_remaining)}")

        # --- Update the world state
        all_sprites.update()
        

        # --- Draw items

        background_group.draw(screen)

        all_sprites.draw(screen)
        
        # create text for score
        # create an image that has the score in it
        lives_image = font.render(
            f"Lives Remaining {int(player.lives_remaining)}", True, WHITE)
        
        # Draw/blit the image on the screen 
        screen.blit(lives_image, (5, 35))
        
        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


if __name__ == "__main__":
    start()
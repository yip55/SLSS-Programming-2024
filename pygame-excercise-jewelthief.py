# pygame-exercise-jewelthief.py
# Clone of Jewel Thief Game

import pygame as pg
import random

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
NUM_COINS = 1

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pg.image.load("./Images/mario.webp")

        self.rect = self.image.get_rect()

    def update(self):
        """update the location of the sprite to the mouse cursor"""
        self.rect.centerx = pg.mouse.get_pos()[0]
        self.rect.centery = pg.mouse.get_pos()[1]
    
class Coin(pg.sprite.Sprite):
   
    def __init__(self):
        super().__init__()
 
        self.image = pg.image.load("./Images/coin.png")
        self.rect = self.image.get_rect()

        # spaw in the random parts of the screen
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

    

def start():
    """Environment Setup and Game Loop"""

    pg.init()
    pg.mouse.set_visible(False)

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    
    # Coin sprites
    coin_sprites = all_sprites = pg.sprite.Group()
    for _ in range(NUM_COINS):
        coin = Coin()
        all_sprites.add(coin)
        coin_sprites.add(coin)

    # Create a player and store it in a variable
    player = Player()

    all_sprites.add(player)

    pg.display.set_caption("Jewel Thief Clone (Don't sue us Nintendo)")

    pg.display.set_caption("<WINDOW TITLE HERE>")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        all_sprites.update()

        # collision between player and coin_sprites
        # get a list of all coin_sprites that collide 
        #   with the player
        # for every coin that collides, print "COLLISION!"
        coins_collided = pg.sprite.spritecollide(
            player,
            coin_sprites,
            False
        )

        for coin in coins_collided:
            print(f"COLLISION at {coin.rect.x}, {coin.rect.y}")

        # --- Draw items
        screen.fill(WHITE)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()
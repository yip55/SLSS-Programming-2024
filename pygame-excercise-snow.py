import pygame as pg

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


class Snowflake(pg.sprite.Sprite):
    # create constructor 
    #   image, rect 
    def __init__(self, size: int):
        super().__init__()
        # creating a "blank" image 
        self.image = pg.Surface((size, size))

        # draw an circle on the blank image 
        pg.draw.circle(
            self.image,
            WHITE,
            (size // 2, size // 2), # draw in the middle of the blank image
            size // 2
        )

        self.rect = self.image.get_rect()
        # spaw in the middle of the screen
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2
def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # add one snowflake to the sprite group
    all_sprites.add(Snowflake(12))

    pg.display.set_caption("<Snow Falling>")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()
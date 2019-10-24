import pygame
from boundry import Boundry
from mario import Mario
import game_functions
import sys
from pygame.sprite import Group
from levels import Levels

# clock = pygame.time.Clock()


def run_mario():
    pygame.init()

    gf = game_functions

    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("SUPER MARIO BRUHS")
    # screen.fill([0, 255, 0])


    ground = Boundry(0, 450, 7571, 500, screen)
    # plat1 = Boundry(0, 100, 100, 25, screen)
    # plat2 = Boundry(100, 200, 100, 25, screen)
    # plat3 = Boundry(200, 300, 100, 25, screen)


    ground.blitme()
    # plat1.blitme()
    pygame.display.flip()

    boundries = Group()

    boundries.add(ground)
    # boundries.add(plat1)
    # boundries.add(plat2)
    # boundries.add(plat3)


    mario = Mario(0, 450, screen, boundries)
    #mario.blitme()

    # Create all the levels
    level = Levels(mario)

    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(mario)

    clock = pygame.time.Clock()

    while True:
        gf.check_events(mario)
        mario.update()
        #gf.update_screen(screen, boundries, mario)

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        #levels.update()
        # If the player gets near the right side, shift the world left (-x)
        if mario.rect.right >= 250:
            diff = mario.rect.right - 250
            mario.rect.right = 250
            level.shift_world(-diff)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        level.draw(screen)
        active_sprite_list.draw(screen)


        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

run_mario()


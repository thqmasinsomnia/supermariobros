import pygame
from boundry import Boundry
from mario import Mario
import game_functions
import sys
from pygame.sprite import Group
from levels import Levels
from goomba import Goomba
from green_koopa import Green_Koopa
from blocks import Blocks


# clock = pygame.time.Clock()


def run_mario():
    pygame.init()

    gf = game_functions


    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("SUPER MARIO BRUHS")
    # screen.fill([0, 255, 0])

    ground = Boundry(0, 450, 7571, 200, screen, True)
    # plat1 = Boundry(0, 100, 100, 25, screen, False)
    # plat2 = Boundry(100, 200, 100, 25, screen, False)
    # plat3 = Boundry(200, 300, 100, 25, screen, False)



    ground.blitme()

    #pygame.display.flip()

    plats = Group()

    plats.add(ground)
    # plats.add(plat1)
    # plats.add(plat2)
    # plats.add(plat3)


    mario = Mario(100, 100, screen, plats)

    block = Blocks(screen, 256, 236, 32, 32, True, mario)

    block.blitme()
    blocks = Group()

    goomba1 = Goomba(500, 0, screen, plats, mario)
    goomba2 = Goomba(100, 300, screen, plats, mario)

    block = Blocks(screen, 156, 236, 32, 32, True, mario)
    blocks = Group()

    blocks.add(block)

    block.blitme()

    goombas = Group()
    green_koopas = Group()
    koop1 = Green_Koopa(200, 300, screen, plats, mario, goombas, green_koopas)

    plats.add(ground)
    # plats.add(plat1)
    # plats.add(plat2)
    # plats.add(plat3)

    blocks.add(block)

    mario = Mario(100, 100, screen, plats)

    goomba1 = Goomba(500, 0, screen, plats, mario)
    goomba2 = Goomba(100, 300, screen, plats, mario)



    goombas = Group()
    green_koopas = Group()
    #koop1 = Green_Koopa(200, 300, screen, plats, mario, goombas)


    goombas.add(goomba2)
    green_koopas.add(koop1)

    mario = Mario(0, 450, screen, plats)
    #mario.blitme()

    # Create all the levels
    level = Levels(mario)

    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(mario)

    clock = pygame.time.Clock()
  #  mario.blitme()


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

        for goomba in goombas:
            goomba.update()

        for koopa in green_koopas:
            koopa.update()

        for block in blocks:
            block.update()

        gf.update_screen(screen, plats, mario, goombas, green_koopas, blocks)


run_mario()


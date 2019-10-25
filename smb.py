import pygame
from boundry import Boundry
from mario import Mario
import game_functions
import sys
from pygame.sprite import Group
from levels import Levels
from goomba import Goomba
from green_koopa import Green_Koopa
from flying_koopa import Flying_Koopa

# clock = pygame.time.Clock()


def run_mario():
    pygame.init()

    gf = game_functions


    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("SUPER MARIO BRUHS")
    # screen.fill([0, 255, 0])
    plats = Group()
    ground = Boundry(0, 450, 2469, 200, screen, True)
    ground2 = Boundry(2534, 450, 536, 200, screen, True)
    ground3 = Boundry(3178, 450, 2285, 200, screen, True)
    ground4 = Boundry(5536, 450, 2034, 200, screen, True)

    stairset1 = Boundry(4784, 408, 144, 36, screen, True)
    stairset2 = Boundry(4827, 375, 101, 36, screen, True)
    stairset3 = Boundry(4856, 338, 72, 36, screen, True)
    stairset4 = Boundry(4892, 303, 36, 36, screen, True)

    # plat1 = Boundry(0, 100, 100, 25, screen, False)
    # plat2 = Boundry(100, 200, 100, 25, screen, False)
    # plat3 = Boundry(200, 300, 100, 25, screen, False)
    # plats.add(plat1)
    # plats.add(plat2)
    # plats.add(plat3)

    plats.add(ground)
    plats.add(ground2)
    plats.add(ground3)
    plats.add(ground4)

    plats.add(stairset1)
    plats.add(stairset2)
    plats.add(stairset3)
    plats.add(stairset4)



    #pygame.display.flip()




    mario = Mario(100, 100, screen, plats)

    goomba1 = Goomba(500, 0, screen, plats, mario)
    goomba2 = Goomba(200, 400, screen, plats, mario)



    goombas = Group()
    green_koopas = Group()
    fly_koop = Group()
    koop1 = Green_Koopa(500, 300, screen, plats, mario, goombas)
    fly1 = Flying_Koopa(200, 300, screen, plats, mario, goombas)

    goombas.add(goomba2)
    green_koopas.add(koop1)
    fly_koop.add(fly1)

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

        for plat in plats:
            plat.blitme()

        for koop in fly_koop:
            koop.update()

        gf.update_screen(screen, plats, mario, goombas, green_koopas, fly_koop)


run_mario()


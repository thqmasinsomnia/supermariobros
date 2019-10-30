import pygame
from boundry import Boundry
from mario import Mario
import game_functions
import sys
from pygame.sprite import Group
from levels import Levels
from goomba import Goomba
from green_koopa import Green_Koopa
from red_koopa import Red_Koopa
from flying_koopa import Flying_Koopa
from red_flying_koopa import Red_Flying_Koopa
from coin import Coin
from flag import Flag
from main_menu import MainMenu
from game_hub import GameHub


def run_mario():
    pygame.init()
    gf = game_functions
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("SUPER MARIO BRUHS")

    """Main Menu"""
    main_start = MainMenu(screen)
    while main_start:
        main_start.show_menu()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_start = False

    plats = Group()
    ground = Boundry(0, 450, 2469, 200, screen, True)
    ground2 = Boundry(2534, 450, 536, 200, screen, True)
    ground3 = Boundry(3178, 450, 2285, 200, screen, True)
    ground4 = Boundry(5536, 450, 2034, 200, screen, True)

    flag1 = Flag(200, 200, 32, 32)
    flags = Group()
    flags.add(flag1)

    stairset1 = Boundry(4784, 408, 144, 36, screen, True)
    stairset2 = Boundry(4827, 375, 101, 36, screen, True)
    stairset3 = Boundry(4856, 338, 72, 36, screen, True)
    stairset4 = Boundry(4892, 303, 36, 36, screen, True)

    plat1 = Boundry(0, 100, 100, 25, screen, False)
    # plat2 = Boundry(100, 200, 100, 25, screen, False)
    # plat3 = Boundry(200, 300, 100, 25, screen, False)
    plats.add(plat1)
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




    # mario = Mario(0, 400, screen, plats, flags)
    mario = Mario(0, 400, screen, plats)

    goomba1 = Goomba(500, 0, screen, plats, mario)
    goomba2 = Goomba(200, 400, screen, plats, mario)



    goombas = Group()

    koops = Group()

    koop1 = Green_Koopa(1000, 300, screen, plats, mario, goombas, koops)
    fly1 = Flying_Koopa(200, 300, screen, plats, mario, goombas)
    redfly1 = Red_Flying_Koopa(300, 400, screen, plats, mario, goombas)
    koop2 = Red_Koopa(700, 300, screen, plats, mario, goombas)



    koops.add(koop1)
    koops.add(koop2)
    koops.add(fly1)
    koops.add(redfly1)

    goombas.add(goomba2)


    #mario.blitme()

    # Create all the levels
    level = Levels(mario)

    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(mario)

    #mario.blitme()

    coin1 = Coin(200, 300, screen, plats, mario)
    coins = Group()
    coins.add(coin1)

    clock = pygame.time.Clock()

    game_ui = GameHub(screen)   # holds game text for coins, time, etc

    while True:
        gf.check_events(mario)
        mario.update()


        #gf.update_screen(screen, boundries, mario)

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        level.update()
        #If the player gets near the right side, shift the world left (-x)
        if mario.rect.right >= 300:
            print("Mario rect.right: ", mario.rect.right)
            diff = mario.rect.right - 300
            mario.rect.right = 300
            level.shift_world(-diff)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        level.draw(screen)
        active_sprite_list.draw(screen)
        game_ui.show_ui()   # show game text; time, coins, lives, etc

        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        #pygame.display.flip()

        for goomba in goombas:
            goomba.update()

        for plat in plats:
            plat.blitme()

        for koop in koops:
            koop.update()

        for coin in coins:
            coin.update()

        gf.update_screen(screen, plats, mario, goombas, koops, coins)

        pygame.display.flip()
        print("MARIO SCORE: " + str(mario.score))
run_mario()


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
from blocks import Blocks
from main_menu import MainMenu
from game_hub import GameHub
from mushroom import Mushroom
from pipe import Pipe


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

    # flag1 = Flag(200, 200, 32, 32)
    # flags = Group()
    # flags.add(flag1)

    stairset1 = Boundry(4784, 408, 144, 36, screen, True)
    stairset2 = Boundry(4827, 375, 101, 36, screen, True)
    stairset3 = Boundry(4856, 338, 72, 36, screen, True)
    stairset4 = Boundry(4892, 303, 36, 36, screen, True)



    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("SUPER MARIO BRUHS")
    # screen.fill([0, 255, 0])


    #ground = Boundry(0, 450, 7571, 200, screen, True)
    # plat1 = Boundry(0, 100, 100, 25, screen, False)
    # plat2 = Boundry(100, 200, 100, 25, screen, False)
    # plat3 = Boundry(200, 300, 100, 25, screen, False)



    plats.add(ground)
    plats.add(ground2)
    plats.add(ground3)
    plats.add(ground4)








    mario = Mario(0, 100, screen, plats)




    goomba1 = Goomba(500, 0, screen, plats, mario)
    goomba2 = Goomba(200, 400, screen, plats, mario)



    block = Blocks(screen, 256, 236, 32, 32, True, mario)

    block.blitme()
    blocks = Group()
    blocks.add(block)

    goomba1 = Goomba(500, 0, screen, plats, mario)
    goomba2 = Goomba(100, 300, screen, plats, mario)

    goombas = Group()
    green_koopas = Group()
    koop1 = Green_Koopa(200, 300, screen, plats, mario, goombas, green_koopas)

    plats.add(ground)
    # plats.add(plat1)
    # plats.add(plat2)
    # plats.add(plat3)

    koops = Group()
    koop1 = Green_Koopa(500, 300, screen, plats, mario, goombas, koops)
    fly1 = Flying_Koopa(200, 300, screen, plats, mario, goombas)
    redfly1 = Red_Flying_Koopa(300, 400, screen, plats, mario, goombas)
    koop2 = Red_Koopa(0, 0, screen, plats, mario, goombas)


    # koops.add(koop1)
    # koops.add(koop2)
    # koops.add(fly1)
    # koops.add(redfly1)

    # goombas.add(goomba2)

    goomba1 = Goomba(500, 0, screen, plats, mario)
    goomba2 = Goomba(100, 300, screen, plats, mario)


    goombas = Group()
    green_koopas = Group()
    #koop1 = Green_Koopa(200, 300, screen, plats, mario, goombas)


    #goombas.add(goomba2)
    green_koopas.add(koop1)


    level = Levels(goombas, koops, plats, blocks, mario)


    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(mario)


    #mario.blitme()

    coin1 = Coin(200, 300, screen, plats, mario)
    coins = Group()

    coins.add(coin1)

    clock = pygame.time.Clock()


    clock = pygame.time.Clock()

    game_ui = GameHub(screen, mario)   # holds game text for coins, time, etc

    big = Mushroom(400, 300, screen, plats, "one_up", mario)

    mushrooms = Group()

    mushrooms.add(big)

    # Create the pipes
    pipe0 = Pipe('short', 100, screen)
    pipe1 = Pipe('short', 1035, screen)
    pipe2  = Pipe('medium', 1393, screen)
    pipe3 = Pipe('long', 1678, screen)
    pipe4 = Pipe('long', 2071, screen)
    pipe5 = Pipe('short', 5857, screen)
    pipe6 = Pipe('short', 6427, screen)

    pipelist = [pipe1, pipe2, pipe3, pipe4, pipe5, pipe6]

    while True:
        gf.check_events(mario)
        mario.update()

        pipe1.blitme()

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

        level.draw(screen, blocks)

        level.draw(screen, pipe1)

        active_sprite_list.draw(screen)
        game_ui.show_ui(mario)   # show game text; time, coins, lives, etc
        clock.tick(60)

        # Go ahead and update the screen with what we've draw.
        pygame.display.flip()

        for goomba in goombas:
            goomba.update()
        for plat in plats:
            plat.blitme()
        for koop in koops:
            koop.update()
        for coin in coins:
            coin.update()
        for mush in mushrooms:
            mush.update()
        for block in blocks:
            block.update()

        gf.update_screen(screen, plats, mario, goombas, koops, coins, mushrooms, blocks, pipelist)
        pygame.display.flip()

run_mario()

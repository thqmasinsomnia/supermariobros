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
    plats2 = Group()
    ground = Boundry(0, 450, 2469, 200, screen, True)
    ground2 = Boundry(2534, 450, 536, 200, screen, True)
    ground3 = Boundry(3178, 450, 2285, 200, screen, True)
    ground4 = Boundry(5536, 450, 2034, 200, screen, True)
    pipe1 = Boundry(1000, 375, 70, 200, screen, False)

    # flag1 = Flag(200, 200, 32, 32)
    # flags = Group()
    # flags.add(flag1)

    stairset1 = Boundry(4784, 408, 144, 36, screen, False)
    stairset2 = Boundry(4827, 375, 101, 36, screen, False)
    stairset3 = Boundry(4856, 338, 72, 36, screen, False)
    stairset4 = Boundry(4892, 303, 36, 36, screen, False)

    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("SUPER MARIO BRUHS")
    # screen.fill([0, 255, 0])

    # ground = Boundry(0, 450, 7571, 200, screen, True)
    # plat1 = Boundry(0, 100, 100, 25, screen, False)
    # plat2 = Boundry(100, 200, 100, 25, screen, False)
    # plat3 = Boundry(200, 300, 100, 25, screen, False)

    plats.add(ground)
    plats.add(ground2)
    plats.add(ground3)
    plats.add(ground4)
    plats.add(pipe1)
    plats.add(stairset1)
    plats.add(stairset2)
    plats.add(stairset3)
    plats.add(stairset4)


    mario = Mario(0, 100, screen, plats)



    block = Blocks(screen, 256, 236, 32, 32, False, mario)

    block.blitme()
    blocks = Group()
    blocks.add(block)



    plats.add(ground)
    # plats.add(plat1)
    # plats.add(plat2)
    # plats.add(plat3)

    koops = Group()
    goombas = Group()

    goomba1 = Goomba(500, 400, screen, plats, mario)
    goomba2 = Goomba(200, 400, screen, plats, mario)
    goombas.add(goomba1)
    goombas.add(goomba2)

    green1 = Green_Koopa(342, 400, screen, plats, mario, goombas)
    koops.add(green1)
    flygreen1 = Flying_Koopa(500, 400, screen, plats, mario, goombas)
    koops.add(flygreen1)
    flyred1 = Red_Flying_Koopa(200, 400, screen, plats, mario, goombas)
    koops.add(flyred1)
    red1 = Red_Koopa(200, 400, screen, plats, mario, goombas)
    koops.add(red1)



    level = Levels(goombas, koops, plats2, blocks, mario)

    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(mario)

    # mario.blitme()

    coin1 = Coin(200, 300, screen, plats, mario)
    coins = Group()

    coins.add(coin1)

    clock = pygame.time.Clock()

    clock = pygame.time.Clock()

    game_ui = GameHub(screen, mario)  # holds game text for coins, time, etc

    big = Mushroom(400, 300, screen, plats, "big", mario)

    mushrooms = Group()

    mushrooms.add(big)

    # Create the pipes
    pipe0 = Pipe('short', 100, screen, mario)
    pipe1 = Pipe('short', 1035, screen, mario)
    pipe2 = Pipe('medium', 1393, screen, mario)
    pipe3 = Pipe('long', 1678, screen, mario)
    pipe4 = Pipe('long', 2071, screen, mario)
    pipe5 = Pipe('short', 5857, screen, mario)
    pipe6 = Pipe('short', 6427, screen, mario)

    pipelist = Group()




    while True:
        gf.check_events(mario)
        mario.update()

        pipe1.blitme()

        # gf.update_screen(screen, boundries, mario)

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        level.update()
        # If the player gets near the right side, shift the world left (-x)
        if mario.rect.right >= 300:
            print("Mario rect.right: ", mario.rect.right)
            diff = mario.rect.right - 300
            mario.rect.right = 300
            level.shift_world(-diff)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        level.draw(screen, blocks)

        level.draw(screen, pipe1)

        active_sprite_list.draw(screen)
        game_ui.show_ui(mario)  # show game text; time, coins, lives, etc
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

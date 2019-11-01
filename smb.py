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
from flower import Flower
from star import Star

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

    q_block1 = Blocks(screen, 256, 300, 32, 32, True, mario)
    block1 = Blocks(screen, 369, 300, 32, 32, False, mario)
    q_block2 = Blocks(screen, 401, 300, 32, 32, True, mario)
    block2 = Blocks(screen, 433, 300, 32, 32, False, mario)
    q_block3 = Blocks(screen, 465, 300, 32, 32, True, mario)
    block3 = Blocks(screen, 497, 300, 32, 32, False, mario)
    q_block4 = Blocks(screen, 433, 187, 32, 32, True, mario)
    q_block5 = Blocks(screen, 2348, 300, 32, 32, True, mario)
    block4 = Blocks(screen, 2800, 300, 32, 32, False, mario)
    q_block6 = Blocks(screen, 2832, 300, 32, 32, True, mario)
    block5 = Blocks(screen, 2864, 300, 32, 32, False, mario)
    block6 = Blocks(screen, 2897, 187, 32, 32, False, mario)
    block7 = Blocks(screen, 2929, 187, 32, 32, False, mario)
    block8 = Blocks(screen, 2961, 187, 32, 32, False, mario)
    block9 = Blocks(screen, 2993, 187, 32, 32, False, mario)
    block10 = Blocks(screen, 3025, 187, 32, 32, False, mario)
    block11 = Blocks(screen, 3057, 187, 32, 32, False, mario)
    block12 = Blocks(screen, 3089, 187, 32, 32, False, mario)
    block13 = Blocks(screen, 3187, 187, 32, 32, False, mario)
    block14 = Blocks(screen, 3219, 187, 32, 32, False, mario)
    block15 = Blocks(screen, 3251, 187, 32, 32, False, mario)
    q_block7 = Blocks(screen, 3283, 187, 32, 32, True, mario)
    block16 = Blocks(screen, 3283, 300, 32, 32, False, mario)
    block17 = Blocks(screen, 3443, 300, 32, 32, False, mario)
    q_block8 = Blocks(screen, 3475, 300, 32, 32, True, mario)
    q_block9 = Blocks(screen, 3605, 300, 32, 32, True, mario)
    q_block10 = Blocks(screen, 3671, 300, 32, 32, True, mario)
    q_block11 = Blocks(screen, 3671, 187, 32, 32, True, mario)
    q_block12 = Blocks(screen, 3736, 300, 32, 32, True, mario)
    block18 = Blocks(screen, 3898, 300, 32, 32, False, mario)
    block19 = Blocks(screen, 3964, 187, 32, 32, False, mario)
    block20 = Blocks(screen, 3996, 187, 32, 32, False, mario)
    block21 = Blocks(screen, 4028, 187, 32, 32, False, mario)
    block22 = Blocks(screen, 4238, 187, 32, 32, False, mario)
    q_block13 = Blocks(screen, 4270, 187, 32, 32, True, mario)
    q_block14 = Blocks(screen, 4302, 187, 32, 32, True, mario)
    block23 = Blocks(screen, 4334, 187, 32, 32, False, mario)
    block24 = Blocks(screen, 4270, 300, 32, 32, False, mario)
    block25 = Blocks(screen, 4302, 300, 32, 32, False, mario)
    block26 = Blocks(screen, 5986, 300, 32, 32, False, mario)
    block27 = Blocks(screen, 6018, 300, 32, 32, False, mario)
    q_block15 = Blocks(screen, 6050, 300, 32, 32, True, mario)
    block28 = Blocks(screen, 6082, 300, 32, 32, False, mario)

    blocks = Group()

    blocks.add(q_block1)
    blocks.add(block1)
    blocks.add(q_block2)
    blocks.add(block2)
    blocks.add(q_block3)
    blocks.add(block3)
    blocks.add(q_block4)
    blocks.add(q_block5)
    blocks.add(block4)
    blocks.add(q_block6)
    blocks.add(block5)
    blocks.add(block6)
    blocks.add(block7)
    blocks.add(block8)
    blocks.add(block9)
    blocks.add(block10)
    blocks.add(block11)
    blocks.add(block12)
    blocks.add(block13)
    blocks.add(block14)
    blocks.add(block15)
    blocks.add(q_block7)
    blocks.add(block16)
    blocks.add(block17)
    blocks.add(q_block8)
    blocks.add(q_block9)
    blocks.add(q_block10)
    blocks.add(q_block11)
    blocks.add(q_block12)
    blocks.add(block18)
    blocks.add(block19)
    blocks.add(block20)
    blocks.add(block21)
    blocks.add(block22)
    blocks.add(q_block13)
    blocks.add(q_block14)
    blocks.add(block23)
    blocks.add(block24)
    blocks.add(block25)
    blocks.add(block26)
    blocks.add(block27)
    blocks.add(q_block15)
    blocks.add(block28)



    plats.add(ground)
    # plats.add(plat1)
    # plats.add(plat2)
    # plats.add(plat3)

    koops = Group()
    goombas = Group()


    goomba1 = Goomba(500, 400, screen, plats, mario)
    goombas.add(goomba1)
    goomba2 = Goomba(200, 400, screen, plats, mario)
    goombas.add(goomba2)

    goomba3 = Goomba(1000, 400, screen, plats, mario)
    goombas.add(goomba3)
    goomba4 = Goomba(3000, 400, screen, plats, mario)
    goombas.add(goomba4)

    flowers = Group()

    flower1 = Flower(200, 420, screen, plats, mario)

    flowers.add(flower1)

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
    one_up = Mushroom(500, 200, screen, plats, "one_up", mario)

    mushrooms = Group()

    mushrooms.add(big)
    mushrooms.add(one_up)

    stars = Group()
    star1 = Star(300, 200, screen, plats, mario)
    stars.add(star1)

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
        for flower in flowers:
            flower.update()
        for star in stars:
            star.update()


        gf.update_screen(screen, plats, mario, goombas, koops, coins, mushrooms, blocks, pipelist, flowers, stars)
        pygame.display.flip()


run_mario()

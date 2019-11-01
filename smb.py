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


    mario = Mario(100, 400, screen, plats)

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

    goomba1 = Goomba(500, 0, screen, plats, mario)
    goomba2 = Goomba(100, 300, screen, plats, mario)

    goombas = Group()
    green_koopas = Group()
    koop1 = Green_Koopa(200, 300, screen, plats, mario, goombas, green_koopas)

    plats.add(ground)
    # plats.add(plat1)
    # plats.add(plat2)
    # plats.add(plat3)

    goomba1 = Goomba(500, 0, screen, plats, mario)
    goomba2 = Goomba(100, 300, screen, plats, mario)

    goombas = Group()
    green_koopas = Group()
    #koop1 = Green_Koopa(200, 300, screen, plats, mario, goombas)


    # goombas.add(goomba2)
    # green_koopas.add(koop1)


    # Create all the levels
    level = Levels(mario, blocks)

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
        level.draw(screen, blocks)
        active_sprite_list.draw(screen)


        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


        # goombas.update()
        # green_koopas.update()
        # blocks.update()

        for goomba in goombas:
            goomba.update()

        for koopa in green_koopas:
            koopa.update()

        for block in blocks:
            block.update()

        gf.update_screen(screen, plats, mario, goombas, green_koopas, blocks)


run_mario()


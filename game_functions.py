import sys
import pygame


def check_events(mario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mario)


def check_keydown_events(event, mario):
    if event.key == pygame.K_RIGHT:
        mario.moving_right = True
    elif event.key == pygame.K_LEFT:
        mario.moving_left = True
    elif event.key == pygame.K_SPACE:
        mario.jump()
    elif event.key == pygame.K_t:
        mario.mario_state()
    elif event.key == pygame.K_i:
        mario.is_star = True
    elif event.key == pygame.K_DOWN:
        if not mario.injump:
            mario.crouch = True


def check_keyup_events(event, mario):
    # if event.key == pygame.K_RIGHT:
    #     mario.moving_right = False
    # elif event.key == pygame.K_LEFT:
    #     mario.moving_left = False

    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
        mario.stop_right()
    elif event.key == pygame.K_LEFT:
        mario.moving_left = False
        mario.stop_left()
    elif event.key == pygame.K_DOWN:
        mario.crouch = False
        if mario.is_big:
            mario.image = pygame.image.load('resources/graphics/marioimgs/mario1.png')


    # if event.type == pygame.KEYUP:
    #     if event.key == pygame.K_LEFT and mario.change_x < 0:
    #         mario.stop()
    #     if event.key == pygame.K_RIGHT and mario.change_x > 0:
    #         mario.stop()



def  update_screen(screen, boundries, mario, goombas, koopas, pipelist):
   # screen.fill([0, 255, 0])
    mario.blitme()
    # for pipe in pipelist:
    #     pipe.blitme()
    # pipelist.blitme()

    for bound in boundries:
        bound.blitme()
    for bound in mario.big_bd:
        bound.blitme()
    for goomba in goombas:
        goomba.mario_collision()
        goomba.blitme()
    for koopa in koopas:
        koopa.mario_collision()
        koopa.goomba_collisions()
        koopa.blitme()
    pygame.display.flip()

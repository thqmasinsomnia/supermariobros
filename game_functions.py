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


def check_keyup_events(event, mario):
    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
    elif event.key == pygame.K_LEFT:
        mario.moving_left = False


def  update_screen(screen, boundries, mario):
    screen.fill([0, 255, 0])
    mario.blitme()
    for bound in boundries:
        bound.blitme()
    pygame.display.flip()
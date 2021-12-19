import controls
import pygame
from pygame.sprite import Group

from main_character import character
from platform import Platform
from g_over import game_over_screen


def run():
    """ Запуск игры """
    pygame.init()
    max_score = controls.max_score()
    wight_screen = 400
    heigth_screen = 600
    screen = pygame.display.set_mode((wight_screen, heigth_screen))
    pygame.display.set_caption('Pixel Pig Jump')
    bg_image = pygame.image.load('Resource/bg.png').convert_alpha()
    bg_scroll = 0
    clock = pygame.time.Clock()
    FPS = 60
    main_character = character(screen)
    platforms = Group()
    platform = Platform(200, 595)
    platforms.add(platform)
    g_o = False
    font_b = pygame.font.SysFont('Calibri', 24)
    score = 0
    while True:
        clock.tick(FPS)
        if not g_o:
            pause = controls.events(main_character)
            if pause == 1:
                controls.pause_game(screen, font_b)
            scroll = main_character.update_character()
            platform = controls.create_platforms(platforms, platform)
            bg_scroll += scroll
            if bg_scroll >= 600:
                bg_scroll = 0
            controls.in_platform(platforms, main_character)
            if scroll > 0:
                score += scroll // 10
            if main_character.rect.top > 600:
                g_o = True
            controls.update(bg_image, screen, main_character, platforms, scroll, bg_scroll, score, font_b)
        elif g_o:
            game_over_screen(screen, score, font_b, max_score)
            key = pygame.key.get_pressed()
            max_score1 = controls.overwriting_max_score(score, max_score)
            if key[pygame.K_SPACE]:
                g_o = False
                max_score = max_score1
                score = 0
                main_character = character(screen)
                platforms.empty()
                platforms = Group()
                platform = Platform(200, 595)
                platforms.add(platform)
            controls.events(main_character)


run()

from random import randint

import pygame
import sys
from background_scroll import bg

from platform import Platform
from g_over import draw_text


def events(main_character):
    """Обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Вправо
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                main_character.mright = True
            # Влево
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                main_character.mleft = True
        elif event.type == pygame.KEYUP:
            # Вправо
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                main_character.mright = False
            # Влево
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                main_character.mleft = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return 1


def update(bg_image, screen, main_character, platforms, scroll, bg_scroll, score, font_b):
    """Обновление экрана"""
    main_character.output()  # главный персонаж
    platforms.update(scroll, score)  # обновленние платформ
    platforms.draw(screen)  # отрисовка платформ
    draw_text(screen, 'SCORE: ' + str(score), font_b, (0, 0, 0), 0, 10)  # Отрисовка счета
    pygame.display.update()
    bg(screen, bg_image, bg_scroll)  # Отрисовка фона


def max_score():
    """ Рекорд игрока """
    score = open('bestresult.txt', 'w+').readline()
    if score == '':
        score = 0
    return int(score)


def create_platforms(platforms, platform):
    """ Создание платформ """
    if len(platforms) < 10:
        p_x = randint(0, 400 - 57)
        p_y = (platform.rect.y - randint(70, 115))
        platform = Platform(p_x, p_y)
        platforms.add(platform)
    return platform


# Взято у проекта прошлого года PvP_game
def pause_game(screen, font_b):
    """Функция, которая ставит игру на паузу при нажатии кнопки ESC."""
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_text(screen, 'PAUSE', font_b, (0, 0, 0), 170, 250)
        draw_text(screen, 'PRESS ENTER', font_b, (0, 0, 0), 140, 300)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()


###

def in_platform(platforms, main_character):
    """ Коллизия платформы и персонажа """
    for platform in platforms:
        if platform.rect.colliderect(main_character.rect.x, main_character.rect.y + main_character.centery,
                                     main_character.width, main_character.height):
            if main_character.rect.bottom < platform.rect.centery:
                if main_character.jump_vel > 0:
                    main_character.rect.bottom = platform.rect.top
                    main_character.jump_vel = -20

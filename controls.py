from random import randint

import pygame
import sys
from background_scroll import bg

from platform import Platform
from g_over import draw_text


def events(main_character):
    """Обработка событий
    :param main_character: главный персонаж
    :return: None
    """
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
    """Обновление экрана
    :param bg_image: переменная, отвечающая за фоновое изображение
    :param screen: переменная, которая отражает экран вывода
    :param main_character: переменная, которая отвечающая за главного героя
    :param platforms: переменная, которая отвечает за группу платформ
    :param scroll: переменная, которая отвечает за перемещение по y
    :param bg_scroll: переменная, которая отвечает за перемещение фона
    :param score: переменная, которая отражает очки игрока
    :param font_b: переменная, которая отвечает за шрифт
    :return: None
    """
    main_character.output()  # главный персонаж
    platforms.update(scroll, score)  # обновленние платформ
    platforms.draw(screen)  # отрисовка платформ
    draw_text(screen, 'SCORE: ' + str(score), font_b, (0, 0, 0), 0, 10)  # Отрисовка счета
    pygame.display.update()
    bg(screen, bg_image, bg_scroll)  # Отрисовка фона


def max_score():
    """ Рекорд игрока
    :return: очки игрока из файла
    """
    try:
        file = open('bestresult.txt', 'r')
        score = file.readline()
        if not score.isdigit():
            score = 0
        file.close()
    except Exception:
        score = 0
    return int(score)


def overwriting_max_score(score, max_score):
    """ Рекорд игрока
    :param score: переменная, которая отражает текущие очки персонажа
    :param max_score: переменная, которая отражает максимальные очки персонажа
    :return: рекорд игрока
    """
    if score > max_score:
        max_score = score
        file = open('bestresult.txt', 'w+')
        file.write(str(max_score))
        file.close()
    return max_score


def create_platforms(platforms, platform):
    """ Создание платформ
    :param platforms: переменная, отвечающая за группу платформ, находящихся на экране
    :param platform: переменная, отвечающая за последнюю платформу
    :return: последнюю платформу
    """
    if len(platforms) < 10:
        p_x = randint(0, 400 - 57)
        p_y = (platform.rect.y - randint(70, 115))
        platform = Platform(p_x, p_y)
        platforms.add(platform)
    return platform


# Взято у проекта прошлого года PvP_game
def pause_game(screen, font_b):
    """Функция, которая ставит игру на паузу при нажатии кнопки ESC
    :param screen: переменная, которая отражает экран вывода
    :param font_b: переменная, которая отвечает за шрифт
    :return: None
    """
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
    """ Коллизия платформы и персонажа
    :param platforms: переменная, отвечающая за группу платформ, находящихся на экране
    :param main_character: переменная, которая отвечающая за главного героя
    :return: None
    """
    for platform in platforms:
        if platform.rect.colliderect(main_character.rect.x, main_character.rect.y + main_character.centery,
                                     main_character.width, main_character.height):
            if main_character.rect.bottom < platform.rect.centery:
                if main_character.jump_vel > 0:
                    main_character.rect.bottom = platform.rect.top
                    main_character.jump_vel = -20

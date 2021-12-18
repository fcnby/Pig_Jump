import random

import pygame


class Platform(pygame.sprite.Sprite):
    """инициализация одной платформы"""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Resource/platform.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (58, 17))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.motion = random.choice([0, 1])
        self.direction = random.choice([-1, 1])
        self.counter = 0

    def update(self, scroll, score):
        """обновление платформы
        :param scroll: переменная, которая отвечает за перемещение по y
        :param score: переменная, которая отражает текущие очки персонажа
        :return: None
        """
        self.rect.y += scroll
        if self.motion == 1 and score > 50:
            self.rect.x += self.direction
            self.counter += 1
        if self.counter >= 150 or self.rect.left < 0 or self.rect.right > 400:
            self.direction *= -1
            self.counter = 0
        if self.rect.top > 600:
            self.kill()

import pygame


class character:

    def __init__(self, screen):
        """ инициализация главного героя"""

        self.screen = screen
        self.image = pygame.image.load('Resource/main character.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.bottom = self.rect.bottom
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        self.centery = float(0)
        self.centerx = float(0)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.jump_vel = 0
        self.gravity = 1
        self.flip = False

    def output(self):
        """Отрисовка главного героя"""
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def update_character(self):
        """Обновление позиции героя """
        scroll = 0
        self.centerx = 0
        self.centery = 0
        if self.mright and self.rect.right < self.screen_rect.right:
            self.centerx = - 15
            self.flip = False
        if self.mleft and self.rect.left > 0:
            self.centerx = + 15
            self.flip = True

        # Постонный прыжок
        self.jump_vel += self.gravity
        self.centery += self.jump_vel

        # проверка на скролл
        if self.rect.top <= 200:
            if self.jump_vel < 0:
                scroll = -self.centery

        self.rect.centery += self.centery + scroll
        self.rect.centerx -= self.centerx

        return scroll

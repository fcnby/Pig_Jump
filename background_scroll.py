def bg(screen, bg, scroll):
    """ Обновление фонового изображения """
    screen.blit(bg, (0, 0 + scroll))
    screen.blit(bg, (0, -600 + scroll))

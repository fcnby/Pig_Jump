def bg(screen, bg, scroll):
    """ Обновление фонового изображения
    :param screen: переменная, которая отражает экран вывода
    :param bg: переменная, отвечающая за фоновое изображение
    :param scroll: переменная, которая отвечает за перемещение по y
    :return: None
    """
    screen.blit(bg, (0, 0 + scroll))
    screen.blit(bg, (0, -600 + scroll))

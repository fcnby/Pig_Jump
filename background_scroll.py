
def bg(screen, bg, scroll):
    screen.blit(bg, (0, 0 + scroll))
    screen.blit(bg, (0, -600 + scroll))

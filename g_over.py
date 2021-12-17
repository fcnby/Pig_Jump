import pygame


def draw_text(screen, text, font, text_col, x, y):
    """Отрисовки текста"""
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def game_over_screen(screen, score, font_b, max_score):
    """ Отрисовка текста для экрана проигрыша """
    pygame.display.update()
    draw_text(screen, 'GAME OVER', font_b, (0, 0, 0), 130, 200)
    if score > max_score:
        draw_text(screen, 'YOU HAVE A NEW RECORD: ' + str(score), font_b, (0, 0, 0), 70, 250)
        draw_text(screen, 'PRESS SPACE TO PLAY AGAIN', font_b, (0, 0, 0), 70, 300)
    else:
        draw_text(screen, 'SCORE: ' + str(score), font_b, (0, 0, 0), 130, 250)
        draw_text(screen, 'YOUR RECORD: ' + str(max_score), font_b, (0, 0, 0), 110, 300)
        draw_text(screen, 'PRESS SPACE TO PLAY AGAIN', font_b, (0, 0, 0), 70, 350)

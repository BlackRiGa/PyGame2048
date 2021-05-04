import pygame
import sys

from logics import *


def draw_interface(score):
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont('STXingu', 70)
    font_score = pygame.font.SysFont('sims', 48)
    text_score = font_score.render("Score: ", True, COLOR_TEXT)
    text_score_value = font_score.render(f"{score}", True, COLOR_TEXT)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (175, 35))
    pretty_print(mas)
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * SIZE_BLOCKS + (column + 1) * MARGIN
            h = row * SIZE_BLOCKS + (row + 1) * MARGIN + SIZE_BLOCKS
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCKS, SIZE_BLOCKS))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCKS - font_w) / 2
                text_y = h + (SIZE_BLOCKS - font_h) / 2
                screen.blit(text, (text_x, text_y))


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
COLOR_TEXT = (255, 127, 0)
COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (128, 0, 128),
    8: (255, 255, 0),
    16: (0, 0, 128),
    32: (255, 0, 235),
    64: (70, 130, 180),
    128: (128, 128, 0),
    256: (0, 0, 255),
    512: (128, 0, 128),
    1024: (95, 158, 160),
    2048: (85, 107, 47)
}
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
BLOCKS = 4
SIZE_BLOCKS = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCKS + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + 110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)
score = 0
USERNAME = None
mas[1][2] = 2
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
def draw_intro():
    img2048 = pygame.image.load('2048.jpg')
    font = pygame.font.SysFont('STXingu', 70)
    text_welcome = font.render("Welcome! ", True, WHITE)
    name = 'Введите имя:'
    is_find_name = False
    while not is_find_name:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif even.type == pygame.KEYDOWN:
                if even.unicode.isalpha():
                    if name == 'Введите имя:':
                        name = even.unicode
                    else:
                        name += even.unicode
                elif even.key == pygame.K_BACKSPACE:
                    name = name[: - 1]
                elif even.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break

        screen.fill(BLACK)
        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        screen.blit(text_welcome, (230, 80))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)
draw_intro()
draw_interface(score)
pygame.display.update()
while is_zero_in_mas(mas) or can_move(mas):
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif even.type == pygame.KEYDOWN:
            delta = 0
            if even.key == pygame.K_LEFT:
                mas, delta = move_left(mas)
            if even.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)
            if even.key == pygame.K_UP:
                mas, delta = move_up(mas)
            if even.key == pygame.K_DOWN:
                mas, delta = move_down(mas)
            score += delta
            empty = get_empty_list(mas)
            random.shuffle(empty)
            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            mas = insert_2_or_4(mas, x, y)
            print(f'Мы заполнили элемент с номером:', random_num)
            draw_interface(score)
            pygame.display.update()
    print(USERNAME)
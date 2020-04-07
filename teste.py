import pygame
from pygame.locals import *

r = 40  # razão

pygame.init()
screen = pygame.display.set_mode((15 * r, 15 * r))
pygame.display.set_caption('Nonogram')
screen.fill((40, 40, 40))

linha_vertical = pygame.Surface((15 * r, 1))
linha_vertical.fill((50, 50, 50))

linha_horizontal = pygame.Surface((1, 15 * r))
linha_horizontal.fill((50, 50, 50))

for x in range(1, 15):
    if x % 5 == 0:
        linha_vertical.fill((100, 100, 100))
    else:
        linha_vertical.fill((50, 50, 50))
    screen.blit(linha_vertical, (0, x * r))

for x in range(1, 15):
    if x % 5 == 0:
        linha_horizontal.fill((100, 100, 100))
    else:
        linha_horizontal.fill((50, 50, 50))
    screen.blit(linha_horizontal, (x * r, 0))

indicador = pygame.Surface((40, 40))
indicador.set_alpha(128)
indicador.fill((255, 255, 255))
screen.blit(indicador, (0, 0))


def indicador(x, y):
    pygame.draw.rect(screen, (255, 255, 255), [x, y, r, r], 1)


# indicador(20, 20)
# indicador(40, 40)

while 1:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
    pygame.display.update()

import pygame
from functions import load_image


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Fair Final')
    lvl1_bg = load_image('lvl1.jpg')
    lvl1_bg = pygame.transform.scale(lvl1_bg, (pygame.display.get_window_size()))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        lvl1_bg = pygame.transform.scale(lvl1_bg, (pygame.display.get_window_size()))
        screen.blit(lvl1_bg, (0, 0))
        pygame.display.flip()

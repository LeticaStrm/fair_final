import sys
import pygame
import math
import time
from functions import load_image
from classes import *


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    bg = pygame.transform.scale(load_image('menu_bg.jpg'), (500, 500))
    pygame.display.set_caption('Fair Final')
    screen.blit(bg, (0, 0))
    head_font = pygame.font.SysFont('arialmt', 76, True)
    button_font = pygame.font.SysFont('arialmt', 43, True)
    header_text = head_font.render('Fair Final', True, (255, 255, 255))
    start_button_text = button_font.render('Начать', True, (255, 255, 255))
    screen.blit(header_text, (100, 50))
    screen.blit(start_button_text, (200, 175))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if 175 < x < 340 and 160 < y < 230:
                    running = False
        pygame.display.flip()

    start_time = time.time()
    circles_count = 0
    circles_record = '--'
    time_record = '--:-'
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Fair Final')
    lvl1_bg = load_image('lvl2.png')
    lvl1_bg = pygame.transform.scale(lvl1_bg, (pygame.display.get_window_size()))
    x, y = screen.get_size()
    font = pygame.font.SysFont('arialmt', int((0.0753891050583658 * x) // 1))
    lil_font = pygame.font.SysFont('arialmt', int((0.0364785992217899 * x) // 1))
    car = Car('RedStrip.png', (0.046875 * x, 0.0694 * y), (0.234375 * x, 0.805555555555555 * y), x)
    all_cars = pygame.sprite.Group()
    all_cars.add(car)
    all_barriers = pygame.sprite.Group()
    barriers = [Barrier(0, 0, x, 0.025 * y),
                Barrier(0.985 * x, 0, 0.015 * x, y),
                Barrier(0, 0, 0.02 * x, y),
                Barrier(0, 0.94 * y, x, 0.02 * y),
                Barrier(0.144 * x, 0.24 * y, 0.618 * x, 0.005 * y),
                Barrier(0, 0.46 * y, 0.34 * x, 0.01 * y),
                Barrier(0.15 * x, 0.73 * y, 0.3203125 * x, 0.005 * y),
                Barrier(0.48 * x, 0.243055555555555 * y, 0.005 * x, 0.513888888888888 * y),
                Barrier(0.7421875 * x, 0.42 * y, 0.234375 * x, 0.005 * y),
                Barrier(0.48 * x, 0.75 * y, 0.3515625 * x, 0.005 * y),
                Barrier(0.82421875 * x, 0.625 * y, 0.0078125 * x, 0.138888888888888 * y),
                Barrier(0.62109375 * x, 0.5794444444444444 * y, 0.005 * x, 0.01 * y),
                Barrier(0.63671875 * x, 0.5586111111111111 * y, 0.005 * x, 0.01 * y),
                Barrier(0.65234375 * x, 0.537777777777777 * y, 0.005 * x, 0.01 * y),
                Barrier(0.66796875 * x, 0.5169444444444444 * y, 0.005 * x, 0.01 * y),
                Barrier(0.68359375 * x, 0.4961111111111111 * y, 0.005 * x, 0.01 * y),
                Barrier(0.69921875 * x, 0.475277777777777 * y, 0.005 * x, 0.01 * y),
                Barrier(0.71484375 * x, 0.4544444444444444 * y, 0.005 * x, 0.01 * y),
                Barrier(0.73046875 * x, 0.4336111111111111 * y, 0.005 * x, 0.01 * y)]
    all_barriers.add(*barriers)
    all_checkpoints = pygame.sprite.Group()
    checkers_counter = 0
    checkers = [CheckPoint(0.37109375 * x, 0.4861111111111111 * y, 0.078125 * x, 0.013888888888888 * y),
                CheckPoint(0.8203125 * x, 0.243055555555555 * y, 0.078125 * x, 0.013888888888888 * y),
                CheckPoint(0.521484375 * x, 0.763888888888888 * y, 0.0078125 * x, 0.138888888888888 * y),
                CheckPoint(0.21484375 * x, 0.7857142857142857 * y, 0.00390625 * x, 0.1388888888888889 * y)]
    all_checkpoints.add(*checkers)
    print(screen.get_size())
    clock = pygame.time.Clock()
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not hasattr(event, 'key'):
                continue
            down = event.type == pygame.KEYDOWN
            if event.key == pygame.K_RIGHT:
                car.right = down * -0.0015625 * x
            elif event.key == pygame.K_LEFT:
                car.left = down * 0.0015625 * x
            elif event.key == pygame.K_UP:
                car.up = down * -0.0001953125 * x
            elif event.key == pygame.K_DOWN:
                car.down = down * 0.0001953125 * x
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_ESCAPE:
                running = False
        lvl1_bg = pygame.transform.scale(lvl1_bg, (pygame.display.get_window_size()))
        screen.blit(lvl1_bg, (0, 0))
        all_cars.update()
        all_cars.draw(screen)
        all_barriers.draw(screen)
        all_checkpoints.draw(screen)
        if pygame.sprite.spritecollideany(car, all_barriers):
            car.rect.x, car.rect.y = car.start_position
            car.speed = 0
            clock.tick(1)
            circles_count = 0
            start_time = time.time()
        if pygame.sprite.collide_rect(car, checkers[checkers_counter // 1]):
            checkers_counter += 1
            if checkers_counter >= len(checkers):
                checkers_counter = 0
                circles_count += 1
                if circles_record == '--' or circles_count > int(circles_record):
                    circles_record = circles_count
                if time_record == '--:-' or float(time_record) > float(time.time() - start_time):
                    time_record = str(time.time() - start_time)[:-14]
                start_time = time.time()
        circles_text = font.render(str(circles_count), True, (255, 255, 255))
        screen.blit(circles_text, (0.02734375 * x, 0.0208333333333333 * y))
        time_text = font.render(str(time.time() - start_time)[:-14], True, (255, 255, 255))
        screen.blit(time_text, (0.859375 * x, 0.0208333333333333 * y))
        c_record_text = lil_font.render(f'Лучший результат: {str(circles_record)}', True, (150, 150, 150))
        screen.blit(c_record_text, (0.09765625 * x, 0.02986111111111 * y))
        t_record_text = lil_font.render(f'Лучшее время: {str(time_record)}', True, (150, 150, 150))
        screen.blit(t_record_text, (0.5859375 * x, 0.02986111111111 * y))
        clock.tick(60)
        pygame.display.flip()

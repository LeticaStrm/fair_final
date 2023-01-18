import pygame
from functions import load_image
import math


class Car(pygame.sprite.Sprite):
    def __init__(self, image, size, position, x_screen):
        super().__init__()
        self.orig_image = load_image(image)
        self.image = pygame.transform.scale(self.orig_image, size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.start_position = position
        self.max_speed = 0.001953125 * x_screen
        self.min_speed = -0.00390625 * x_screen
        self.direction = 0
        self.speed = 0
        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.speed += self.up + self.down
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < self.min_speed:
            self.speed = self.min_speed
        if self.speed < -0.05:
            self.speed += 0.05
        if self.speed > 0.05:
            self.speed -= 0.05
        self.direction += self.right + self.left
        r = self.direction * math.pi / 180
        self.rect.x += self.speed * math.sin(r)
        self.rect.y += self.speed * math.cos(r)
        self.image = pygame.transform.rotate(self.orig_image, self.direction)


class Barrier(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.orig_image = load_image('empty.png')
        #self.orig_image = pygame.Surface((20, 10), pygame.SRCALPHA)
        #self.orig_image.fill((255, 0, 0))
        self.image = pygame.transform.scale(self.orig_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)


class CheckPoint(Barrier):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        #self.image.fill((0, 255, 0))

import random
import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, ENEMY_TYPE, PLAYER_TYPE, SCREEN_HEIGHT

class Bullet(Sprite):
    SPEED = 20
    SPEEDP = 20
    BULLETS = {ENEMY_TYPE:BULLET_ENEMY,PLAYER_TYPE:BULLET}

    def __init__(self, spaceship):
        self.owner = spaceship.type
        self.image = pygame.transform.scale(self.BULLETS[self.owner],(10,30))
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center

    def update(self, bullets):
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)
        if self.owner == PLAYER_TYPE:
            self.rect.y -= self.SPEEDP
            if self.rect.y <= 0:
                bullets.remove(self)

    def draw(self,screen):
        if self.owner == ENEMY_TYPE:
            screen.blit(self.image, self.rect)
        if self.owner == PLAYER_TYPE:
            screen.blit(self.image, self.rect)

    def powerUP(self):
        self.SPEEDP = 30

    def reset(self):
        self.SPEEDP=20


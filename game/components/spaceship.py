import random
import pygame
from pygame.sprite import Sprite

from game.utils.constants import PLAYER_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH//2)-30
    Y_POS = 500 
    SPACESHIP_HEIGHT = 60 
    SPACESHIP_WIDTH = 50
    def __init__(self):
        self.type = PLAYER_TYPE
        self.image = pygame.transform.scale(SPACESHIP,(self.SPACESHIP_HEIGHT, self.SPACESHIP_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input,game):
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_rigth()
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()
        if user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()
        if user_input[pygame.K_SPACE]:
            game.bullet_manager.add_bullet(self)


    def move_left(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH-self.SPACESHIP_WIDTH

    def move_rigth(self):
        self.rect.x += 10
        if self.rect.left > SCREEN_WIDTH:
            self.rect.x = 0

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10

    def move_up(self):
        if self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.y -= 10             

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
        if self.rect.left < 0: 
            screen.blit(self.image,(self.rect.x + SCREEN_WIDTH ,self.rect.y))
        if self.rect.right > SCREEN_WIDTH:
            screen.blit(self.image,(self.rect.x - SCREEN_WIDTH, self.rect.y))


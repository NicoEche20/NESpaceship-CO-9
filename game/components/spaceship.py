import random
import pygame
from pygame.sprite import Sprite

from game.utils.constants import PLAYER_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, SPACESHIP, DEFAULT_TYPE

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH//2)-30
    Y_POS = 500 
    SPACESHIP_HEIGHT = 60 
    SPACESHIP_WIDTH = 50
    SPEED=10
    def __init__(self):
        self.type = PLAYER_TYPE
        self.image = pygame.transform.scale(SPACESHIP,(self.SPACESHIP_HEIGHT, self.SPACESHIP_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.power_up_type = DEFAULT_TYPE
        self.power_up_time_up = 0
    

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
        self.rect.x -= self.SPEED
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH-self.SPACESHIP_WIDTH

    def move_rigth(self):
        self.rect.x += self.SPEED
        if self.rect.left > SCREEN_WIDTH:
            self.rect.x = 0

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.SPEED

    def move_up(self):
        if self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SPEED             

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
        if self.rect.left < 0: 
            screen.blit(self.image,(self.rect.x + SCREEN_WIDTH ,self.rect.y))
        if self.rect.right > SCREEN_WIDTH:
            screen.blit(self.image,(self.rect.x - SCREEN_WIDTH, self.rect.y))

    def reset(self):
        self.rect.x=self.X_POS = (SCREEN_WIDTH//2)-30
        self.rect.y=self.Y_POS = 500
        self.speed = 10
        self.power_up_time_up=0

    def on_pick_power_up(self,time_up, type, image):
        self.power_up_time_up = time_up
        self.power_up_type = type
        if self.power_up_type == SHIELD_TYPE:
            self.image = pygame.transform.scale(image,(self.SPACESHIP_HEIGHT, self.SPACESHIP_WIDTH))
        else:
            self.SPEED = 20
      

    def draw_power_up(self,game):
        if self.power_up_type != DEFAULT_TYPE:
            time_left=round((self.power_up_time_up- pygame.time.get_ticks()) /1000,2)
            if time_left >=0:
                game.menu.draw(game.screen, f"{self.power_up_type.capitalize()} is enabled for {time_left} seconds",y=30, color= (255,255,255))
            else:
                self.power_up_type=DEFAULT_TYPE
                self.image = pygame.transform.scale(SPACESHIP,(self.SPACESHIP_HEIGHT, self.SPACESHIP_WIDTH))
                self.SPEED = 10

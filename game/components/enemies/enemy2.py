import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2


class Enemy2(Enemy):
    ENEMY_HEIGHT= 80
    SPEED_Y = 4
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_2,(self.ENEMY_HEIGHT,self.ENEMY_WIDTH))



    
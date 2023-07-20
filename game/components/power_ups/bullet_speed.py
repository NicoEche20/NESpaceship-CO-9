import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import BULLET, BULLETS_TYPE, SPACESHIP


class BulletSpeed(PowerUp):
    def __init__(self):
        bulletp=pygame.transform.scale(BULLET,(65,65))
        super().__init__(bulletp, BULLETS_TYPE, SPACESHIP)
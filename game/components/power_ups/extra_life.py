import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEART, SPACESHIP, HEART_TYPE


class Heart(PowerUp):
    
    def __init__(self):
        heart=pygame.transform.scale(HEART,(50,50))
        super().__init__(heart, HEART_TYPE,SPACESHIP)
        
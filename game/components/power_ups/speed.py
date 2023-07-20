import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SPACESHIP, SPEED_TYPE


class Speed(PowerUp):
    
    def __init__(self):
        speed=pygame.transform.scale(SPACESHIP,(50,50))
        super().__init__(speed, SPEED_TYPE,SPACESHIP)
        
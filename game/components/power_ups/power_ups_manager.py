import random
import pygame
from game.components.power_ups.bullet_speed import BulletSpeed
from game.components.power_ups.extra_life import Heart
from game.components.power_ups.shield import Shield
from game.components.power_ups.speed import Speed


class PowerUpManager:

    def __init__(self):
        self.power_ups=[]
        self.when_appears=0

    def generate_power_up(self):
        current_time=pygame.time.get_ticks()
        if not self.power_ups and current_time >= self.when_appears:
            self.when_appears += random.randint(10000,15000)
            #self.power_up=Heart
            self.power_up=random.choice([Shield,BulletSpeed,Speed,Heart])
            self.power_ups.append(self.power_up())        

    def update(self, game):
        self.generate_power_up()
        for power_up in self.power_ups:
            power_up.update(game.game_speed,self.power_ups)
            if power_up.rect.colliderect(game.player.rect):
                start_time=pygame.time.get_ticks()
                duration=random.randint(3,5)
                power_up_time_up =start_time + (duration*1000)
                if self.power_up==Shield or self.power_up==Speed:
                    game.player.on_pick_power_up(power_up_time_up,power_up.type, power_up.spaceship_image)
                elif self.power_up==BulletSpeed or self.power_up==Heart:
                    game.bullet_manager.on_pick_power_up(power_up_time_up,power_up.type)
                self.power_ups.remove(power_up)
                #elif self.power_up==Speed or self.power_up==Heart:
                 #   game.player.on_pick_power_up(power_up_time_up,power_up.type, power_up.spaceship_image)
                 #   self.power_ups.remove(power_up)
                #elif self.power_up==Heart:
                 #   game.bullet_manager.on_pick_power_up(power_up_time_up,power_up.type)
                  #  self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups=[]
        now=pygame.time.get_ticks()
        self.when_appears = now + random.randint(10000,15000)
    
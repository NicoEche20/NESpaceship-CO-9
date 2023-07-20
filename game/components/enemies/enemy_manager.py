import random

import pygame
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy2 import Enemy2
from game.utils.constants import HEART_TYPE, SHIELD_TYPE


class EnemyManager:
    def __init__(self):
        self.enemies=[]

    def update(self, game):
        if not self.enemies:
            enemy_choice=random.choice([Enemy,Enemy2])
            self.enemies.append(enemy_choice())
        
        for enemy in self.enemies:
            enemy.update(self.enemies, game.bullet_manager)
            if enemy.rect.colliderect(game.player.rect):
                if game.player.power_up_type != SHIELD_TYPE:
                    self.enemies.remove(enemy)
                    game.playing = False
                    game.death_count.update()
                    pygame.time.delay(500)
                    break

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def reset(self):
        self.enemies = []
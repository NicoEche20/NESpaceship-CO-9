import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy2 import Enemy2


class EnemyManager:
    def __init__(self):
        self.enemies=[]

    def update(self, game):
        if not self.enemies:
            enemy_choice=random.choice([Enemy,Enemy2])
            self.enemies.append(enemy_choice())
        
        for enemy in self.enemies:
            enemy.update(self.enemies, game.bullet_manager)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
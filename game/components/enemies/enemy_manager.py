import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy2 import Enemy2


class EnemyManager:
    def __init__(self):
        self.enemies=[]

    def update(self):
        if not self.enemies:
            x=random.choice([1,2])
            if x==1:
                self.enemies.append(Enemy())
            else:
                self.enemies.append(Enemy2())
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
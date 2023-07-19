import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE
class BulletManager:
    def __init__(self):
        self.enemy_bullets = []
        self.player_bullets = []
        
    def update(self, game, enemies):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
            if enemy_bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(enemy_bullet)
                game.playing = False
                game.death_count += 1
                pygame.time.delay(1000)
                break

        for player_bullet in self.player_bullets:
            player_bullet.update(self.player_bullets)
            for enemy in enemies:
                if player_bullet.rect.colliderect(enemy.rect):
                    self.player_bullets.remove(player_bullet)
                    game.score += 1
                    enemies.remove(enemy)

    def draw(self, screen):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(screen)
        for player_bullet in self.player_bullets:
            player_bullet.draw(screen)

    def add_bullet(self,spaceship):
        if spaceship.type == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(Bullet(spaceship))
        if spaceship.type == PLAYER_TYPE and len(self.player_bullets)<=10:
            self.player_bullets.append(Bullet(spaceship))

import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLETS_TYPE, DEFAULT_TYPE, ENEMY_TYPE, HEART_TYPE, PLAYER_TYPE, SHIELD_TYPE
class BulletManager:
    COLIDE_TRUE= False
    def __init__(self):
        self.enemy_bullets = []
        self.player_bullets = []
        self.power_up_type = DEFAULT_TYPE
        self.power_up_time_up = 0

    def update(self, game, enemies):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
            if enemy_bullet.rect.colliderect(game.player.rect):
                if game.player.power_up_type != SHIELD_TYPE:
                    if self.power_up_type != HEART_TYPE:
                        self.enemy_bullets.remove(enemy_bullet)
                        game.playing = False
                        game.death_count.update()
                        pygame.time.delay(500)
                        break
                    else:
                        self.COLIDE_TRUE=True
                        self.enemy_bullets.remove(enemy_bullet)

        for player_bullet in self.player_bullets:
            player_bullet.update(self.player_bullets)
            for enemy in enemies:
                if player_bullet.rect.colliderect(enemy.rect):
                    self.player_bullets.remove(player_bullet)
                    game.score.update()
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

    def on_pick_power_up(self,time_up, type):
        self.power_up_time_up = time_up
        self.power_up_type = type

    
    def draw_power_up(self,game):
        if self.power_up_type != DEFAULT_TYPE:
            time_left=round((self.power_up_time_up-pygame.time.get_ticks()) /1000,2)
            if time_left >=0:
                self.power_up_select()
                if self.power_up_type == BULLETS_TYPE:
                    game.menu.draw(game.screen, f"{self.power_up_type.capitalize()} is enabled for {time_left} seconds",y=30, color= (255,255,255))
                else:
                    game.menu.draw(game.screen, f"You have an extra life enabled" ,y=30, color= (255,255,255))
            else:
                self.reset_power_up()        
    
    def power_up_select(self):
        if self.power_up_type == BULLETS_TYPE:
            for player_bullet in self.player_bullets:
                player_bullet.powerUP()
        else:
            self.power_up_time_up=10000000
            if self.COLIDE_TRUE == True:
                self.power_up_time_up=0 


    def reset(self):
        self.enemy_bullets = []
        self.player_bullets = []
        self.reset_power_up()
        for player_bullet in self.player_bullets:
            player_bullet.reset()
    
    def reset_power_up(self):
        self.COLIDE_TRUE=False
        self.power_up_type=DEFAULT_TYPE
        for player_bullet in self.player_bullets:
            player_bullet.reset()
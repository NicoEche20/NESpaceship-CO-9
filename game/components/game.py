import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.count import Counter
from game.components.power_ups.power_ups_manager import PowerUpManager
from game.components.spaceship import Spaceship
from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship() 
        self.bullet_manager = BulletManager()
        self.enemy_manager = EnemyManager()
        self.power_up_manager = PowerUpManager()
        self.menu = Menu()
        self.score = Counter("Score")
        self.death_count = Counter("Death Counter")
        self.max_score = Counter("Highest Score")


    def run(self):
        self.menu.Music()
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def play(self):
        pygame.mixer.music.load("game/assets/Music/menu_soundtrack.mp3")
        pygame.mixer.music.play(-1)
        self.reset()
        self.playing=True
        self.enemy_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.update_max_score()
        pygame.mixer.music.pause()
        self.menu.Music()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input= pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self, self.enemy_manager.enemies)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.player.draw_power_up(self)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.bullet_manager.draw_power_up(self)
        self.power_up_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed     

    def show_menu(self):
        self.menu.draw_wp(self.screen)
        death_message = f"You have {self.death_count.count} death" 
        if self.death_count.count == 0:
            self.menu.draw(self.screen,"Press ENTER to start...")
        elif self.player.pause()==True:
            print(self.player.pause())
            self.on_pause
            self.menu.draw(self.screen,"Press ENTER to continue...")
        else:
            if self.death_count.count > 1: 
                death_message+="s"
            self.menu.draw(self.screen,"Press ENTER to restart...")
            self.menu.draw(self.screen,death_message,y=350)
            self.menu.draw(self.screen,f"Your score in this run is {self.score.count}",y=400)
            self.menu.draw(self.screen,f"The maximum score in the game is {self.max_score.count}",y=450)
        
        self.menu.draw_icon(self.screen)
        self.menu.events(self.on_close, self.play)
        pygame.display.flip()

    def update_max_score(self):
        if self.score.count > self.max_score.count:
            self.max_score.update(self.score.count)

    def on_close(self):
        self.playing = False
        self.running = False

    def on_pause(self):
        self.playing = False
        self.running = True

    def reset(self):
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        self.player.reset()
        self.score.reset()
        self.power_up_manager.reset()
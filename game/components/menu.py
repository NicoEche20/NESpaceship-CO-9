import pygame

from game.utils.constants import FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, GALAXY

HALF_SCREEN_HEIGHT =SCREEN_HEIGHT//2
HALF_SCREEN_WIDTH =SCREEN_WIDTH//2

class Menu:
    def __init__(self):
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.icon = pygame.transform.scale(ICON, (120,80))
        self.image = pygame.transform.scale(GALAXY, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.icon_rect = self.icon.get_rect()
        self.image_rect= self.image.get_rect()
        self.icon_rect.center = (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT-100)
        

    def events(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    on_start()


    def draw_icon(self, screen):
        screen.blit(self.icon, self.icon_rect)

    def draw_wp(self,screen):
        screen.blit(self.image,self.image_rect)

    def draw(self, screen,  message, y=HALF_SCREEN_HEIGHT, color= (0,0,0)):
        text= self.font.render(message,True, color)
        text_rect=text.get_rect()
        text_rect.center=(HALF_SCREEN_WIDTH, y)
        screen.blit(text, text_rect)

    def Music(self):
        pygame.mixer.music.load("game/assets/Music/playing_soundtrack.mp3")
        pygame.mixer.music.play(-1)
    

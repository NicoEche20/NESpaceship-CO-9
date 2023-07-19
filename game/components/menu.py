import pygame

from game.utils.constants import FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT =SCREEN_HEIGHT//2
    HALF_SCREEN_WIDTH =SCREEN_WIDTH//2

    def __init__(self, message):
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.icon = pygame.transform.scale(ICON, (120,80))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT-100)
        self.update_message(message,"" ,"" ,"")
        

    def events(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.KEYDOWN:
                on_start()

    def draw(self, screen):
        screen.fill((120, 20, 140))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.icon, self.icon_rect)
        screen.blit(self.text1, self.text1_rect)
        screen.blit(self.text2, self.text2_rect)
        screen.blit(self.text3, self.text3_rect)
        pygame.display.flip()

    def update_message(self, message,message1,message2, message3):
        self.message = message
        self.message1 = message1
        self.message2 = message2
        self.message3 = message3
        self.text = self.font.render(self.message, True, (0,0,0))
        self.text1 = self.font.render(self.message1, True, (0,0,0))
        self.text2 = self.font.render(self.message2, True, (0,0,0))
        self.text3 = self.font.render(self.message3, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT) 
        self.text1_rect = self.text.get_rect()
        self.text1_rect.center = (self.HALF_SCREEN_WIDTH - 60, self.HALF_SCREEN_HEIGHT + 50)
        self.text2_rect = self.text.get_rect()
        self.text2_rect.center = (self.HALF_SCREEN_WIDTH - 130 , self.HALF_SCREEN_HEIGHT + 100)
        self.text3_rect = self.text.get_rect()
        self.text3_rect.center = (self.HALF_SCREEN_WIDTH - 200, self.HALF_SCREEN_HEIGHT +150) 
    
   
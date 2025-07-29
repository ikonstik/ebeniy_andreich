import pygame
from pygame.sprite import Sprite
from random import randint

class Bottle(Sprite):
    """Класс для одной бутылки"""
    
    def __init__(self, ea_settings, screen):
        super(Bottle, self).__init__()
        self.screen = screen
        self.ea_settings = ea_settings
        
        # Загрузка изображения бутылки и назначение атрибута rect
        self.image = pygame.image.load('images/bottle.png')
        self.rect = self.image.get_rect()
        
        # Каждая бутылка появляется в произвольном месте
        self.rect.centerx = randint(10, self.ea_settings.screen_width - 10)
        self.rect.centery = randint(10, self.ea_settings.screen_height - 10)
        
        # Сохранение точной позиции бутылки
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def blitme(self):
        """Выводит бутылку в текущем положении"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """Перемещает бутылку вниз"""
        self.y += self.ea_settings.bottle_fall_speed
        self.rect.y = self.y
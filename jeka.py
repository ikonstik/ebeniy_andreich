import pygame

class Jeka():
    
    def __init__(self, ea_settings, screen):
        """Инициализирует жеку и задает начальную позицию"""
        self.screen = screen
        self.ea_settings = ea_settings
        
        # Загрузка жеки и создание его прямоугольника
        self.image = pygame.image.load('images/jeka.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Жека появляется в центре экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        # Сохранение вещественной координаты центра жеки
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Обновляет позицию жеки с учетом флагов"""
        # Обновляется атрибут center
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ea_settings.jeka_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ea_settings.jeka_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ea_settings.jeka_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ea_settings.jeka_speed_factor
            
        # Обновление атрибута rect на основании centerx, centery
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    def blitme(self):
        """Рисует жеку в текущей позиции"""
        self.screen.blit(self.image, self.rect)
class Settings():
    """Класс для хранения настроек игры Ebeniy_Andreich"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        # Настройки экрана
        self.screen_width = 1366
        self.screen_height = 768
        self.r = 255
        self.g = 255
        self.b = 255
        self.bg_color = (self.r, self.g, self.b)
        
        # Настройки Жеки
        self.jeka_speed_factor = 2.5
        
        # Настройки бутылки
        self.bottle_fall_speed = 0.5
        self.number_bottles = 8
        self.bottles_needed = 40
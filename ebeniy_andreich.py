import pygame
from pygame.sprite import Group
from settings import Settings
from jeka import Jeka
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_func as gf

def run_game():
    # Инициализирует pygame, settings и объект экрана
    pygame.init()
    ea_settings = Settings()
    screen = pygame.display.set_mode((ea_settings.screen_width,
                                     ea_settings.screen_height))
    pygame.display.set_caption('Ebeniy Andreich')
    
    # Создание кнопки
    play_button = Button(ea_settings, screen, "Заступить в наряд?")
    
    # Создание экземпляра для хранения игровой статистики
    stats = GameStats(ea_settings)
    sb = Scoreboard(ea_settings, screen, stats)
    
    # Создание жеки и  группы бутылок
    jeka = Jeka(ea_settings, screen)
    bottles = Group()
    
    
    
    while True:
        gf.check_events(ea_settings, stats, screen, jeka, bottles, play_button)
        jeka.update()
        if stats.game_active:
            gf.create_bottles(ea_settings, screen, bottles)
            gf.update_bottles(ea_settings, stats, sb, bottles, jeka)
        gf.update_screen(ea_settings, screen, stats, sb, jeka, bottles, play_button)
        
        
run_game()
import sys
import pygame

from bottle import Bottle

def update_screen(ea_settings, screen, stats, sb, jeka, bottles, play_button):
    """Обновляет изображение на экране и отображает новый экран"""
    
    # При каждом проходе цикла прорисовывается экран
    if 0 <= stats.total_bottles < 10:
        screen.fill((255, 255, 255))
    elif 10 <= stats.total_bottles < 20:
        screen.fill((155, 155, 255))
    elif 20 <= stats.total_bottles < 30:
        screen.fill((55, 55, 255))
    else:
        screen.fill((0, 0, 255))
    bottles.draw(screen)
    jeka.blitme()
    sb.show_score()
    
    # Кнопка отображается когда игра неактивна
    if not stats.game_active:
        play_button.draw_button()
        
    # Отображение последнего прорисованного экрана
    pygame.display.flip()
    
def check_keydown_events(event, jeka):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        jeka.moving_right = True
    elif event.key == pygame.K_LEFT:
        jeka.moving_left = True
    elif event.key == pygame.K_UP:
        jeka.moving_up = True
    elif event.key == pygame.K_DOWN:
        jeka.moving_down = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
        
def check_keyup_events(event, jeka):
    """Реагирует на отпускание клавиш"""
    if event.key == pygame.K_RIGHT:
        jeka.moving_right = False
    elif event.key == pygame.K_LEFT:
        jeka.moving_left = False
    elif event.key == pygame.K_UP:
        jeka.moving_up = False
    elif event.key == pygame.K_DOWN:
        jeka.moving_down = False
        
def check_events(ea_settings, stats, screen, jeka, bottles, play_button):
    """Обрабатывает нажатие клавиш"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, jeka)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, jeka)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ea_settings, screen, stats, play_button, jeka, bottles, mouse_x, mouse_y)
            
def check_play_button(ea_settings, screen, stats, play_button, jeka, bottles, mouse_x, mouse_y):
    """Запускает новую игру при нажатии на кнопку"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Скрыть курсор
        pygame.mouse.set_visible(False)
        # Сброс статистики
        stats.reset_stats()
        stats.game_active = True
    
def create_bottles(ea_settings, screen, bottles):
    """Создает необходимое количество бутылок"""
    while len(bottles) < ea_settings.number_bottles:
        bottle = Bottle(ea_settings, screen)
        bottles.add(bottle)
        
def update_bottles(ea_settings, stats, sb, bottles, jeka):
    """Перемещиет бутылки вниз"""
    if stats.total_bottles < 40:
        bottles.update()
        for bottle in bottles:
            if jeka.rect.collidepoint(bottle.rect.center):
                bottles.remove(bottle)
                stats.total_bottles += 1
                sb.prep_score(stats)
                
            if bottle.rect.bottom >= ea_settings.screen_height:
                bottles.remove(bottle)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
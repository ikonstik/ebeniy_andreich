class GameStats():
  """Статистика игры"""
  def __init__(self, ea_settings):
    self.ea_settings = ea_settings
    self.total_bottles = 0
    self.reset_stats()
    
    # Игра запускается в нактивном состоянии
    self.game_active = False
    
  def reset_stats(self):
    """Инициализация статистики"""
    self.total_bottles = 0
    self.score = 0
class Settings():
    """存储外星人的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (233,233,233)

        #设置飞船的速度
        self.ship_speed_factor = 1.5
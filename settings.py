class Settings():
    """存储外星人的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 860
        self.screen_height = 780
        self.bg_color = (233,233,233)
        #外星人移动速度
        self.alien_speed_factor = 4
        self.fleet_drop_speed = 10
        #fleet_direction为1的时候表示向右移动，为-1的时候向左移动
        self.fleet_direction = 1

        #设置飞船的速度
        self.ship_speed_factor = 40
        
        #子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        #限制子弹出现的屏幕的个数
        self.bullets_allowed = 100

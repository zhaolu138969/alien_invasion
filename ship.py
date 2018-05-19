import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置初始化为止"""
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新的飞船放在屏幕的底部中央为止
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船时属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标识
        self.moving_right = False
        self.moving_left = False
        self.moveing_up = False
        self.moveing_down = False

    def update(self):
        """根据移动标志调整飞行的位置"""
        #更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #测试验证飞船向上移动
        if self.moveing_up and self.rect.up <  self.screen_rect.up:
            self.center  += self.ai_settings.ship_speed_factor

        #测试飞行向下移动
        if self.moveing_down and self.rect.down  >  self.screen_rect.down:
            self.center  -= self.ai_settings.ship_speed_factor

        #根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
    # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    #定义用户按键按到键盘上和下键按键时触发
    elif event.key == pygame.KEYUP:
        ship.moving_up = True
    elif event.key == pygame.KEYDOWN:
        ship.moveing_down = True


    #使用快捷键Q结束游戏
    elif event.key == pygame.K_q:
        sys.exit()




def fire_bullet(ai_settings, screen, ship, bullets):
    """"如果没有达到限制，就发射一颗子弹"""
    #创建一个子弹，并将加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    #定义用户松开上下按键时触发
    elif event.key == pygame.KEYUP:
        ship.moving_up = False
    elif event.key == pygame.KEYDOWN:
        ship.moveing_down = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标的事件"""

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)




def update_screen(ai_settings,screen,ship, aliens, bullets):
    """"更新屏幕上的图像，并切到到新屏幕"""
    screen.fill(ai_settings.bg_color)

    #在飞船和外星人后面重新绘制所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #屏幕出现外星人，调用
    aliens.draw(screen)

    # 让最近的绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()

    # 删除已消除的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_setting, ship_height, alien_height):
    """计算屏幕可容纳多少行的外星人"""
    available_space_y = (ai_setting.screen_width - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 *  alien_height))
    return number_rows


#疑点
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.width * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship,  aliens):
    #创建一个外星人，并计算一行可容纳多少个外星人
    #外星人间距为外星人的宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #创建外星人群
    for row_number in range(number_rows):
        #创建第一行的外星人
        for alien_number in range(number_aliens_x):
           create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_width -  (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows



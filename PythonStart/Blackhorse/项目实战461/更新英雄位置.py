import time
import pygame
from plane_sprites import *
# 游戏的初始化
from 黑马.项目实战461.plane_sprites import GameSprite

pygame.init()
# 创建游戏的窗口
# display.set_mode()创建的对象是一个内存中的屏幕书u对象
# 可以理解成是油画的画布
# screen.blit 方法可以在画布上绘制很多图像
screen = pygame.display.set_mode((433, 650))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load(".\\images\\background.png")
# 2.blit绘制图像
screen.blit(bg, (0, 0))
# 3.update 更新屏幕显示
pygame.display.update()

# 绘制英雄的图像
hero = pygame.image.load(".\\images\\hero.gif")
screen.blit(hero, (160, 500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(160, 500, 100, 124)

# 创建敌机的精灵
enemy = GameSprite(".\\images\\enemy1.png")
enemy1 = GameSprite(".\\images\\enemy1.png",2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)


# 游戏循环
while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)
    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()
    # 捕获事件
    event_list = pygame.event.get()

    # 2.修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y <= -124:
        hero_rect.y = 650
    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update -让组中所有的精灵更新位置
    enemy_group.update()
    # draw  - 在screen上绘制所有的精灵
    enemy_group.draw(screen)
    # 4.调用update方法更新显示
    pygame.display.update()




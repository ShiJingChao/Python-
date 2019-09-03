import time

import pygame

# 游戏的初始化
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
# pygame.display.update()

# 绘制英雄的图像
hero = pygame.image.load(".\\images\\hero.gif")
screen.blit(hero, (160, 500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 游戏循环
while True:
    clock.tick(60)
    time.sleep(10)
    pygame.quit()
    pass





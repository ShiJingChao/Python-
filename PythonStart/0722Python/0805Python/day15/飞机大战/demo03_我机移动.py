"""
    我机移动
"""

import pygame, time

screen = pygame.display.set_mode((480, 650))

bg = pygame.image.load("../feiji/background.png")  # 加载背景图片
hero = pygame.image.load("../feiji/hero1.png")  # 加载我方飞机



x = 190
y = 526
while True:

    x += 1
    y -= 1
    
    screen.blit(bg, (0, 0))  # 窗口显示背景图片
    screen.blit(hero, (x, y))  # 窗口显示我方飞机
    pygame.display.update()  # 更新

    time.sleep(0.05)



"""
    我方飞机
"""
import pygame, time

screen = pygame.display.set_mode((480, 650))

bg = pygame.image.load("../feiji/background.png")  # 加载背景图片
hero = pygame.image.load("../feiji/hero1.png")  # 加载我方飞机

screen.blit(bg, (0, 0))  # 窗口显示背景图片
screen.blit(hero, (190, 526))  # 窗口显示我方飞机

while True:

    pygame.display.update()  # 更新





"""
我方飞机

"""
import pygame,time

screen = pygame.display.set_mode((433,650))
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))   # 窗口显示背景图片
pygame.display.update()
# 加载我方飞机
pygame.display.update()
hero = pygame.image.load("./images/hero1.png")
screen.blit(hero,(160,500))
pygame.display.update()

# 窗口显示我方飞机


time.sleep(10)

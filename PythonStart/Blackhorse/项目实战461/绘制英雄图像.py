import time

import pygame

pygame.init()
# 创建游戏的窗口
screen = pygame.display.set_mode((433, 650))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load(".\\images\\background.png")
# 2.blit绘制图像
screen.blit(bg, (0, 0))
# 3.update 更新屏幕显示
pygame.display.update()

# 绘制英雄的图像
hero = pygame.image.load(".\\images\\boy.png")
screen.blit(hero, (160, 500))
pygame.display.update()

while True:
    time.sleep(10)
    pygame.quit()

# 理解 图像并实现图像绘制
# 第一步加载到磁盘
# 要在屏幕上看到某一个图像，需要三个步骤：
# 1.使用 pygame.image.load()    加载图像的数据
# 2.使用游戏屏幕对象，调用blit方法将图像绘制到指定位置
# 3.调用 pygame.display.update（）方法更新整个屏幕显示

# 提示：要想在屏幕上看到绘制的结果，就一定要调用pygame.display.update()方法

import time

import pygame

pygame.init()
# 创建游戏的窗口
screen = pygame.display.set_mode((433, 650))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load(".\\images\\background.png")
# 2.blit绘制图像
screen.blit(bg,(0,0))
# 3.update 更新屏幕显示
pygame.display.update()

while True:
    time.sleep(10)
    pygame.quit()

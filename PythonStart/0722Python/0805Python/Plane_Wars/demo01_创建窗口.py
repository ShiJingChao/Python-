"""
创建窗口
    pygame.display 与显示相关的

"""
import pygame,time

# 创建窗口对象，参数是个元组（窗口的大小）
screen = pygame.display.set_mode((480,852))

# 获取图片对象
bg_img = pygame.image.load("./images/background.png")
# 窗口中显示背景图片
screen.blit(bg_img, (0, 0))
# 更新
pygame.display.update()
time.sleep(3)
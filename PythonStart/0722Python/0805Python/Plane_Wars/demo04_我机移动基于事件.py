"""
    pygame.display -->跟显示相关的设置由它完成
    pygame.locals -->pygame中设置的所有常量

"""
import pygame,time
from pygame.locals import *
screen = pygame.display.set_mode((433,650))
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))   # 窗口显示背景图片
pygame.display.update()
# 加载我方飞机
pygame.display.update()
hero = pygame.image.load("./images/hero1.png")
pygame.display.update()

# 窗口显示我方飞机
# x = 160
def my_plane():
    x = 160
    while True:
        screen.blit(bg, (0, 0))  # 窗口显示背景图片

        # 不停地接收用户的事件

        for event in pygame.event.get():    # 遍历获取用户的每一个事件对象
            if event.type == QUIT:  # 右上角的叉号
                exit()
            elif event.type == KEYDOWN:  # 键盘事件
                if event.key == K_LEFT or event.key == K_a:  # 接收到了向左移动的事件
                    x -= 5
                elif event.key == K_RIGHT or event.key == K_d:
                    x += 5
                elif event.key == K_SPACE:
                    pass

        screen.blit(hero, (x, 526))  # 窗口显示我方飞机
        pygame.display.update()  # 更新
        time.sleep(0.05)

my_plane()
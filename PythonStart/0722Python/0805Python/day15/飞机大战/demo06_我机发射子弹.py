"""
    pygame.display --> 跟显示相关的设置由它完成
    pygame.locals --> pygame中设置的所有常量

"""
import pygame, time
from pygame.locals import *


# 我方战机
class HeroPlane:
    def __init__(self, screen):  # 显示的窗口
        self.x = 190
        self.y = 526
        self.img = pygame.image.load("../feiji/hero1.png")
        self.screen = screen  # 窗口属性
        self.bullet_list = []  # 装着所有我方战机发射出去的子弹对象

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def display(self):  # 显示到窗口的方法
        self.screen.blit(self.img, (self.x, self.y))

        # self.bullet_list 所有我方飞机的子弹
        for bullet in self.bullet_list:
            bullet.display()  # 显示子弹对象
            bullet.move_up()  # 每次显示我方飞机时, 都让我方子弹显示并移动

    def shoot(self):  # 发射子弹的方法
        # 创建子弹对象
        b = Bullet(self.x, self.y, self.screen)
        self.bullet_list.append(b)


# 我方子弹类
class Bullet:
    def __init__(self, x, y, screen):   # 参数: 窗口对象 参数x,y代表我方飞机的坐标, 根据我方飞机的坐标计算子弹的坐标
        self.x = x + 39
        self.y = y - 22
        self.img = pygame.image.load("../feiji/bullet.png")
        self.screen = screen

    def move_up(self):
        self.y -= 10

    def display(self):  # 显示的方法
        self.screen.blit(self.img, (self.x, self.y))


# 控制飞机移动的事件方法
def control_even(hero):  # 参数:  hero 为我方飞机对象

    # 不停地接收用户的事件: pygame.event.get()返回值是个列表
    for event in pygame.event.get():  # 遍历获取用户的每一个事件对象
        if event.type == QUIT:   # 右上角的叉号
            exit()
        elif event.type == KEYDOWN:  # 键盘事件
            if event.key == K_LEFT or event.key == K_a:  # 接收向左的键盘事件
                hero.move_left()
            elif event.key == K_RIGHT or event.key == K_d:  # 接收向右的键盘事件
                hero.move_right()
            elif event.key == K_SPACE:
                hero.shoot()
                print("----piupiupiu----")


def main():
    screen = pygame.display.set_mode((480, 650))

    bg = pygame.image.load("../feiji/background.png")  # 加载背景图片
    hero = HeroPlane(screen)  # 创建我机对象

    while True:
        screen.blit(bg, (0, 0))  # 窗口显示背景图片

        control_even(hero)  # 调用控制飞机移动的方法

        hero.display()  # 调用方法显示我机
        pygame.display.update()  # 更新

        time.sleep(0.05)


if __name__ == "__main__":
    main()






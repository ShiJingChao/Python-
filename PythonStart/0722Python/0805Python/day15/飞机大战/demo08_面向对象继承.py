import pygame, time, random
from pygame.locals import *


class BasePlane:
    def __init__(self, x, y, img_path, screen):  # 显示的窗口
        self.x = x
        self.y = y
        self.img = pygame.image.load(img_path)
        self.screen = screen  # 窗口属性
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.img, (self.x, self.y))
        bullet_list_copy = self.bullet_list.copy()

        for bullet in bullet_list_copy:
            if bullet.is_border():
                self.bullet_list.remove(bullet)
            else:
                bullet.display()
                bullet.move()


class HeroPlane(BasePlane):
    def __init__(self, screen):
        super().__init__(190, 526, "../feiji/hero1.png", screen)

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def shoot(self):  # 发射子弹的方法
        # 创建子弹对象
        b = HeroBullet(self.x + 39, self.y - 22, "../feiji/bullet.png", self.screen)
        self.bullet_list.append(b)


class EnemyPlane(BasePlane):
    def __init__(self, screen):
        super().__init__(0, 0, '../feiji/enemy0.png', screen)
        self.direction = "right"

    def move(self):  # 敌机移动
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self.x >= 480 - 51:
            self.direction = "left"
        elif self.x <= 0:
            self.direction = "right"

    def shoot(self):
        num = random.randint(1, 100)
        if num > 97:
            b = EnemyBullet(self.x + 21, self.y + 39, "../feiji/bullet1.png", self.screen)
            self.bullet_list.append(b)


class BaseBullet:
    def __init__(self, x, y, img_path, screen):
        self.x = x
        self.y = y
        self.img = pygame.image.load(img_path)
        self.screen = screen

    def move(self):
        pass

    def display(self):
        self.screen.blit(self.img, (self.x, self.y))

    def is_border(self):
        pass


class HeroBullet(BaseBullet):
    def move(self):
        self.y -= 10

    def is_border(self):  # 判断是否超出边界
        if self.y <= -22:
            return True
        else:
            return False


class EnemyBullet(BaseBullet):
    def move(self):
        self.y += 10

    def is_border(self):  # 判断是否超出边界
        if self.y >= 650 + 21:
            return True
        else:
            return False


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
    enemy = EnemyPlane(screen)  # 创建敌机对象

    while True:
        screen.blit(bg, (0, 0))  # 窗口显示背景图片

        control_even(hero)  # 调用控制飞机移动的方法

        hero.display()  # 调用方法显示我机
        enemy.display()  # 显示敌机
        enemy.shoot()  # 敌机发射子弹
        enemy.move()  # 敌机自动移动

        pygame.display.update()  # 更新
        time.sleep(0.05)


if __name__ == "__main__":
    main()




"""
    击中飞机：
        子弹类：
        飞机类：
        1.地方子弹击中我方飞机（我方飞机类）
            def init(self,bullet_list)  # bullet_list 敌方子弹列表
                for x in bullet()
                .....判断坐标..........
                击中   break：  爆炸

        2.我方子弹击中敌方飞机（敌方飞机类） # 我
ef hit(self,bullet_list)
                for x in bullet()
                .....判断坐标..........
                击中   break：  爆炸
        *判断漏一个飞机是否被计划总，如果该飞机被击中，让次飞机爆炸


        我方飞机，地方飞机
"""



import pygame,time,random
from pygame.locals import *

class BasePlane:
    # 我方战机
    def __init__(self,x,y,img_path, screen):  # 显示的窗口
        self.x = x
        self.y = y
        self.img = pygame.image.load(img_path)
        self.screen = screen  # 窗口属性
        self.bullet_list = []  # 装着所有我方战机发射出去的子弹对象
        self.is_over = False
    def display(self):
        self.screen.blit(self.img,(self.x,self.y))
        bullet_list_copy = self.bullet_list.copy()

        for bullet in bullet_list_copy:
            if bullet.is_border():
                self.bullet_list.remove(bullet)
            else:
                bullet.display()
                bullet.move()
    def is_hit(self,bullet_list):   # 对方子弹列表
        # 1.判断每颗子弹是否与当前飞机的坐标重复
        for bullet in bullet_list:
            # 2.判断坐标
            if (self.x-bullet.img.get_width()<= bullet.x<=self.x+self.img.get_width()) \
                and (self.y-bullet.img.get_height() <= bullet.y <=self.y + self.img.get_height()):
                self.is_over = True  # 如果被击中, 更改属性值

class HeroPlane(BasePlane):
    def __init__(self,screen):
        super().__init__(160,500,"./images/蔡徐坤1.png",screen)

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def shoot(self):  # 发射子弹的方法
        # 创建子弹对象
        b = HeroBullet(self.x+230, self.y-22,"./images/篮球.png", self.screen)
        self.bullet_list.append(b)


class EnemyPlane(BasePlane):
    def __init__(self,screen):
        super().__init__(0,0,"./images/篮球架.jpg",screen)
        self.direction = "right"

    def move(self): # 敌机移动
        if self.direction == "right":
            self.x +=5
        elif self.direction == "left":
            self.x -= 5
        if self.x >= 382:
            self.direction = "left"
        elif self.x <= 0:
            self.direction = "right"
    def shoot(self):
        num = random.randint(1,100)
        if num >95:
            b = EnemyBullet(self.x+21,self.y+39,"./images/bullet1.png",self.screen)
            self.bullet_list.append(b)

class BaseBullet:
    def __init__(self,x,y,img_path,screen):
        self.x = x
        self.y = y
        self.img = pygame.image.load(img_path)
        self.screen = screen

    def move(self):
        pass
    def display(self):
        self.screen.blit(self.img,(self.x,self.y))

    def is_border(self):
        pass

class HeroBullet(BaseBullet):
    def move(self):
        self.y -= 10

    def is_border(self):
        if self.y <= -46:   # 我方是否超出边界
            return True
        else:
            return False


class EnemyBullet(BaseBullet):
    def move(self):
        self.y += 10

    def is_border(self):
        if self.y <= 650+46:   # 我方是否超出边界
            return True
        else:
            return False



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

    bg = pygame.image.load("./images/background.png")  # 加载背景图片
    hero = HeroPlane(screen)  # 创建我机对象
    enemy = EnemyPlane(screen)  # 创建敌机对象

    a = 0
    b = 0
    while True:
        screen.blit(bg, (0, 0))  # 窗口显示背景图片

        control_even(hero)  # 调用控制飞机移动的方法

        hero.display()  # 调用方法显示我机
        hero.is_hit(enemy.bullet_list)  # 判断我方飞机是否被击中, 如果被击中, 更改is_over属性值

        if hero.is_over:  # 判断我方飞机是否被击中
            if a <= 10:
                hero.img = pygame.image.load(r".\images\hero_blowup_n1.png")
            elif a <= 20:
                hero.img = pygame.image.load(r".\images\hero_blowup_n2.png")
            elif a <= 30:
                hero.img = pygame.image.load(r".\images\hero_blowup_n3.png")
            elif a <= 40:
                hero.img = pygame.image.load(r".\images\hero_blowup_n4.png")
            elif a == 50:
                break
            a += 1

        enemy.display()  # 显示敌机
        enemy.shoot()  # 敌机发射子弹
        enemy.move()  # 敌机自动移动
        enemy.is_hit(hero.bullet_list)  # 判断敌方飞机是否被击中, 传参为我方飞机子弹列表

        if enemy.is_over:  # 用记录击中状态的属性判断敌机是否被击中
            if b <= 10:
                enemy.img = pygame.image.load(r'.\images\enemy0_down1.png')
            elif b <= 20:
                enemy.img = pygame.image.load(r'.\images\enemy0_down2.png')
            elif b <= 30:
                enemy.img = pygame.image.load(r'.\images\enemy0_down3.png')
            elif b < 35:
                enemy.img = pygame.image.load(r'.\images\enemy0_down4.png')
            elif b == 35:
                enemy = EnemyPlane(screen)  # 如果敌机被打死了, 创建一个新的敌机对象, 继续战斗
                b = -1
            b += 1
        pygame.display.update()  # 更新
        time.sleep(0.05)


if __name__ == "__main__":
    main()
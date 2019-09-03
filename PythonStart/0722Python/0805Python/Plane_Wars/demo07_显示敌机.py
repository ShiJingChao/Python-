"""
    pygame.display -->跟显示相关的设置由它完成
    pygame.locals -->pygame中设置的所有常量

"""
import pygame, time,random
from pygame.locals import *
# 地方战机
class Father_Bullet:
    def __init__(self,screen):
        self.screen = screen

class EnemyPlane:
    def __init__(self,screen):
        self.x = 0
        self.y = 0
        self.img = pygame.image.load("./images/篮球架.jpg")
        self.screen = screen
        self.bullet_list = []   # 敌机的子弹列表
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

    def display(self):  # 敌机显示
        self.screen.blit(self.img,(self.x,self.y))
        bullet_list_copy = self.bullet_list.copy()  # 复制子弹列表

        for bullet in bullet_list_copy:
            if bullet.is_border():
                self.bullet_list.remove(bullet)
            else:
                bullet.display()
                bullet.move_down()

    def shoot(self):
        num = random.randint(1,100)
        if num >95:
            b = EnemyBullet(self.x,self.y,self.screen)
            self.bullet_list.append(b)

class EnemyBullet(Father_Bullet):
    def __init__(self,x,y,screen):
        self.x = x+21
        self.y = y+39
        self.img = pygame.image.load("./images/bullet1.png")
        super().__init__(screen)

    def move_down(self):
        self.y += 10


    def display(self):  # 显示的方法
        self.screen.blit(self.img,(self.x,self.y))


    def is_border(self):    # 判断敌方子弹是否超出边界
        if self.y >= 650 + 46:
            return True
        else:
            return False


# 我方战机
class HeroPlane:
    def __init__(self, screen):  # 显示的窗口
        self.x = 160
        self.y = 500
        self.img = pygame.image.load("./images/蔡徐坤1.png")
        self.screen = screen  # 窗口属性
        self.bullet_list = []  # 装着所有我方战机发射出去的子弹对象

    def move_lift(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def display(self):  # 显示到窗口的方法
        self.screen.blit(self.img, (self.x, self.y))
        bullet_list_copy = self.bullet_list.copy()

        # self.bullet_list 所有我方飞机的子弹
        for bullet in bullet_list_copy:
            if bullet.is_border():
                self.bullet_list.remove(bullet)
            else:
                bullet.display()    # 显示子弹对象
                bullet.move_up()    # 每次显示我方飞机时，都让我放子弹显示并移动

    def shoot(self):    # 发射子弹的方法
        # 创建子弹对象
        b = Bullet(self.x,self.y,self.screen)
        self.bullet_list.append(b)


# 我方子弹类
class Bullet(Father_Bullet):
    def __init__(self,x,y,screen):  # 参数窗口对象 参数x，y代表我方飞机的坐标，根据我方飞机的坐标计算子弹坐标
        self.x = x + 230
        self.y = y - 22
        self.img = pygame.image.load("./images/篮球.png")
        self.screen = screen

    def move_up(self):
        self.y -= 10

    def display(self):  # 显示的方法
        self.screen.blit(self.img,(self.x,self.y))


    def is_border(self):    # 判断我方子弹是否超出边界
        if self.y <= -46:   # 我方是否超出边界
            return True
        else:
            return False

# 控制飞机移动的事件方法
def control_even(hero):  # 参数：hero为我方飞机对象

    # 不停地接收用户的事件：pygame.event.get()返回值是个列表
    for event in pygame.event.get():  # 遍历获取用户的每一个事件对象
        if event.type == QUIT:  # 右上角的叉号
            exit()
        elif event.type == KEYDOWN:  # 键盘事件
            if event.key == K_LEFT or event.key == K_a:  # 接收到了向左移动的事件
                hero.move_lift()
            elif event.key == K_RIGHT or event.key == K_d:
                hero.move_right()
            elif event.key == K_SPACE:
                hero.shoot()


def main():
    screen = pygame.display.set_mode((433, 650))
    bg = pygame.image.load("./images/background.png")

    hero = HeroPlane(screen)  # 创建我机对象
    enemy = EnemyPlane(screen)  # 创建敌机对象
    while True:
        screen.blit(bg, (0, 0))  # 窗口显示背景图片

        # 不停地接收用户的事件
        control_even(hero)

        hero.display()  # 调用方法 显示我机
        enemy.display() # 显示敌机
        enemy.shoot()   # 敌机发射子弹
        enemy.move()    # 敌机自动移动
        pygame.display.update()  # 更新
        # time.sleep(0.05)


if __name__ == "__main__":
    main()

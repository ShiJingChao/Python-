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

    def display(self):
        self.screen.blit(self.img,(self.x,self.y))
        bullet_list_copy = self.bullet_list.copy()

        for bullet in bullet_list_copy:
            if bullet.is_border():
                self.bullet_list.remove(bullet)
            else:
                bullet.display()
                bullet.move()


class Heroplane(BasePlane):
    def __init__(self,screen):
        super().__init__(160,500,"./images/蔡徐坤1.png",screen)

    def move_lift(self):
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

"""
    三大特征: 封装继承和多态;

    继承: 父类, 子类;

        1. 子类 可以继承 父类的 公有属性和方法;
        2. 子类 可以重写父类的方法;
        3. 子类 可以拓展父类的已有的方法
"""


class BasePlane:
    def __init__(self, img, screen):
        self.x = 190
        self.y = 280
        self.img = img
        self.screen = screen

    # def eat(self):
    #     print("吃饱了就行")


class Enemy(BasePlane):
    def __init__(self, img, screen):
        super().__init__(img, screen)
        self.direction = "right"


    # def eat(self):  # 条件:与父类方法名一样; 父类方法在子类重写;
    #     print("细嚼慢咽的吃饭...")

    # def eat(self):
        # 吃饱了
        # super().eat()  # 调用父类的方法
        # 饭后百步走
        # print("饭后百步走")




class Hero(BasePlane):
    def __init__(self, img, screen):
        super().__init__(img, screen)


hero = Hero("", "")





# d = Doctor()
# d.eat()



















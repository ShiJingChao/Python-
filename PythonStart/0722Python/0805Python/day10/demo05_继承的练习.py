"""
    1. 创建动物类作为父类, name,age,eat(),sleep()
    2. 创建猫类作为动物类的子类
            新增属性:color
            新增方法:catch_mouse()
            重写方法:eat()
    3. 创建狗类作为动物类的子类
            新增方法:look_door()
"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃吃吃吃吃饭饭...")

    def sleep(self):
        print("我吃饱就睡,睡醒了也不来上课, 反正我住在食堂....")


class Cat(Animal):

    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    def catch_mouse(self):  # 新增方法:catch_mouse()
        print("抓老鼠呀抓老鼠...")

    def eat(self):
        print("猫吃鱼...猫吃老鼠....")


class Dog(Animal):
    def look_door(self):  # 新增方法
        print("我是一只看门狗~~~~")


c1 = Cat("灰白条纹", "加菲", 80)
c1.catch_mouse()
c1.eat()
c1.sleep()

print(c1.color)
print(c1.name)
print(c1.age)

d1 = Dog("旺财", 100)  # 创建对象, 自动init方法
d1.look_door()
print(d1.name, d1.age)

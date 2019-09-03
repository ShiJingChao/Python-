"""
有三种动物：狗、猫、猪，
	父类：动物、
	子类：狗、猫、猪
	动物的属性：动物的名字
	动物的方法是eat（就是打印自己的名字）

有一个饲养员：饲养员
	饲养员的方法：feed_animal(需要饲养的动物)
 		函数的实现是（其实就是调用动物的eat方法）

"""


class Feeder:  # 饲养员类
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal_obj):  # 参数:动物对象
        animal_obj.eat()


class Animal:  # 动物类
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 动物吃..." % self.name)


class Pig(Animal):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


f = Feeder('郝勇')

d = Dog("旺财")
c = Cat("招财")
p = Pig("发财")

f.feed_animal(d)
f.feed_animal(c)
f.feed_animal(p)

print("----------------------")

class A:
    def show_self(self):
        print("我是A类对象")

class B:
    def show_self(self):
        print("我是B类对象")


a = A()
b = B()

def func(obj):
    obj.show_self()

func(a)
func(b)






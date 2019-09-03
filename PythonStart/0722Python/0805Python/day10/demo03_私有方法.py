"""
    私有方法:
        __方法名, 类中能够使用, 类外不能使用
        但是,可以通过公有方法访问到类的私有方法;

    私有方法, 私有属性:
        起到保护核心代码的作用;

    * 通过__dict__属性查看所有属性值(包括私有)

    python中关于私有,是通过改名实现的,所以在类外访问私有,可以通过对象._类名__私有名实现,
    但是强烈不建议这样做;
"""


class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    # 实现了某个具体的功能,
    def __secret(self):
        print("我偷偷告诉你一个秘密,我藏有私房钱...")

    # 提供公有方法作为接口
    def get_secret(self):
        self.__secret()  # 类中调用该方法


p1 = Person("小贱")
# p1.__secret()  AttributeError: 'Person' object has no attribute '__secret'

p1.get_secret()  # 我偷偷告诉你一个秘密,我藏有私房钱...

print(p1.__dict__)  # {'name': '小贱', '_Person__age': 18}
# print(p1.__age)
print(p1._Person__age)  # 18


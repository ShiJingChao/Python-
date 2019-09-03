"""
    私有:
        只能在类中使用, 类外不能使用
        语法: 在私有属性或者私有方法前, 加双下划线, __变量名, 就表示私有的

    私有属性:
        __属性名, 只能在本类中使用;
        类外不能使用, 但是可以通过公有方法, 修改或者获取私有属性的值;
"""

class Girl:
    def __init__(self, name):
        self.name = name
        self.__age = 18  # 私有属性

    def show_me(self):  # 通过公有方法获取私有属性值
        print("我的名字:{}, 我偷偷的告诉你我的年龄:{}".format(self.name, self.__age))

    def set_age(self, age):  # 通过公有方法修改私有属性的值, 参数为修改后的值
        self.__age = age
        print("我偷偷告诉你一声,我的年龄改变了,现在是:{}".format(self.__age))


g1 = Girl("李小花")
print(g1.name)
# print(g1.__age)  AttributeError: 'Girl' object has no attribute '__age'

g1.show_me()

# 1. 在类中定义一个公有方法set_age, 用于更改私有属性__age的值;
g1.set_age(8)  # 我偷偷告诉你一声,我的年龄改变了,现在是:8
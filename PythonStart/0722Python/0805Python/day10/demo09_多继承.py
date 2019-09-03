"""
    python中支持多继承: 多个父类
        子类可以同时拥有多个父类功能;

    python2
        c3算法 , 深度优先

    python3
        c3算法, 广度优先

    注意点: 如果使用多继承(一个子类同时继承自多个父类), 保证父类中没有相同名字的方法;
    method resolution order

    可以根据 类.__mro__属性查看 当前类的父类的排序
    也可以根据 类.mro() 查看当前类的父类的排序
"""


class A:
    def func1(self):
        print("A")


class B:
    def func1(self):
        print("B")


class C:
    def func1(self):
        print("C")


class D(A, B, C):
    pass


d = D()
d.func1()
print(D.__mro__)
print(D.mro())


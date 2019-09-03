"""
    装饰器:
        闭包的应用;

        对于已经实现定义好了的函数功能, 在不改变原函数的情况下, 给他新增功能;
        python函数式编程, 变量, 参数, 返回值...;

        @classmethod
        @staticmethod
"""


def outer(func):  # 外层函数的参数: 函数 --> 指的就是要装饰的函数

    def inner():
        print("此处代码, 就是被装饰的函数执行之前执行的代码")
        func()
        print("此处代码, 就是被装饰的函数执行之后执行的代码")
    return inner


@outer
def func():
    print("---中秋节---")


func()

# 写个装饰器, 计算函数执行的时间
import time


def get_time(func):  # 装饰器--> 装饰的是函数

    def inner():
        before = time.time()  # 函数执行之前的时间戳
        func()
        after = time.time()  # 函数执行结束之后的时间戳
        print("----->", after - before)  # 返回值为时间戳的差值
    return inner


@get_time
def get_num():
    for x in range(100):
        print(x)


get_num()



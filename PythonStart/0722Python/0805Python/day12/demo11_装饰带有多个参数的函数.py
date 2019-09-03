"""
    装饰带有多个参数的函数
"""


def outer(func):

    def inner(*args, **kwargs):
        print("调用之前装饰-----")
        func(*args, **kwargs)
        print("调用之后装饰-----")
    return inner


@outer
def get_num(*args, **kwargs):
    print(args)
    print(kwargs)


get_num(1,2,3,4, 李雪="镁铝", 年龄=18)
# 被装饰后的函数--> inner(1,2,3,4, 李雪="镁铝", 年龄=18)


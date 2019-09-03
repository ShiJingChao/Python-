"""
    装饰带有参数的函数
"""


def outer(func):

    def inner(x):  # 形参: 被装饰的函数的形参
        print("调用之前,装饰的....")
        func(x)
        print("调用之后,装饰的....")
    return inner


@outer
def get_num(a):
    print(a * 10)


get_num(2)  # 被装饰后的函数 --> inner(2)

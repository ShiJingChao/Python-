"""
    查看被装饰函数的文档注释

    1. 需要导入 from functools import wraps
    2. 装饰内层函数 @wraps(被装饰的函数)
"""
from functools import wraps


def outer(func):

    @wraps(func)  # 解决不能查看文档注释的问题
    def inner():

        func()

    return inner


@outer
def func():
    """
    func函数
    :return: 无
    """
    print("我是一个被装饰的函数....")


print(func.__doc__)  # None



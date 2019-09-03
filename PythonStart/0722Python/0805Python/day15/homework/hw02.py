"""
2、编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数"的异常
"""


def func(a, b):
    if a >= b:
        print("{}-{}={}".format(a, b, a-b))
    else:
        e = Exception("被减数不能小于减数")
        raise e


func(1, 100)








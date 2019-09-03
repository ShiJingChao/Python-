"""
    装饰一个带返回值的函数
"""


def outer(func):

    def inner():
        print("----调用前装饰-----")
        res = func() # 此时接收原函数的返回值
        print("------调用后装饰------")
        return res

    return inner


@outer
def say():
    print("我是一个say函数, 我就说说说说说....")

say()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
@outer
def say2():
    return "我是一个say22222"


res = say2()
# 被装饰的函数say2()--> 调用的是装饰器的inner()函数 -->  res = inner()
print(res)



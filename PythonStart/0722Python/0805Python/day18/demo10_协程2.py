"""
    generator: 生成器对象;

        1. 生成器表达式
        2. 生成器函数
            关键字 yield
                        1. 返回一个值
                        2. 暂停


        g.send(参数)
            1. 获取数据
            2. 将参数值传递给上一次yield暂停的位置
"""


# 1. 协程最简单的一个效果, 就是控制函数的阶段执行, 节约线程或者进程的资源
def func():
    print("1")
    print("2")
    r = yield  # r 由生成器对象传进来的值 r = 666
    print("a")
    print("b")
    print("c")
    rr = yield r  # rr 由生成器对象传递进来的值 rr=100
    print("3")
    yield rr  # 100


g = func()  # 通过生成器函数 获取一个生成器对象

next(g)  # None

res1 = g.send(666)  # 1.获取数据  2.将值传递给yield上一次暂停的位置
print(res1)  # 666

res2 = g.send(100)  # 1. 获取数据 2. 将值传递给yield上一次暂停的位置
print(res2)

# print("----->", g.__next__())  # 获取生成器中的数据
# print("----->", g.__next__())
# print("----->", next(g))
#
# print("----->", g.__next__())  # StopIteration






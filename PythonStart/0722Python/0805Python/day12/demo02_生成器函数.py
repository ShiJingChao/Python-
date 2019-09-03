"""
    生成器函数:
        关键字: yield 的作用:
            1. 返回一个数据; 如果yield后边啥也没有, 返回数据为None;
            2. 遇到yield获取一条数据, 同时暂停函数的执行, 直到下一次获取数据时,从暂停的位置继续往下执行;

        1. 生成器函数用来生成一个生成器对象;
        2. 生成器函数中的代码在获取对象数据时,才会被执行;

        获取数据的第4种方式
        send(值):  1. 获取生成器数据的一种方式
                   2. 给上一次生成器函数中yield的位置传递一个值

                   [注]: 第一次获取生成器数据时, 不能使用send()方法获取;

"""


def func1():
    print("你好, 我是一个生成器")
    yield   # return 返回值


g = func1()
print(g)  # <generator object func1 at 0x000000000260A948>
print(type(g))  # <class 'generator'>

# 获取生成器对象数据的三种方式: 1, next(对象); 2,for..in 对象; 3. 对象.__next__()
print(next(g))  # None


def func2():
    print("啦啦啦,我是一个生成器~~")
    yield 666666


# step1: 获取生成器对象
g2 = func2()

# step2: 获取数据
print(g2.__next__())
"""
啦啦啦,我是一个生成器~~
666666
"""

# print(g2.__next__())  # StopIteration


def func3():
    print("猜猜吧,我是谁~~~")
    yield "伤齿龙"
    print("我的头上有三只角")
    yield "三角龙"


g3 = func3()

print(g3.__next__())
"""
猜猜吧,我是谁~~~
伤齿龙
"""
print(g3.__next__())  # 三角龙
"""
我的头上有三只角
三角龙
"""


def func4():
    for x in range(10):
        yield "猜猜吧我是第%d只龙" % x


g4 = func4()

print(next(g4))  # 猜猜吧我是第0只龙
print(next(g4))
print(next(g4))
print(next(g4))


def func5():
    print("我是第5个生成器函数....")
    dragon = yield "请给我一只食肉龙"
    print("啦啦啦啦啦啦")
    yield dragon


g5 = func5()
# next(g5)  # "请给我一只食肉龙"
print(g5.__next__())  # 1. 获取一个生成器的数据(请给我一只食肉龙)
# TypeError: can't send non-None value to a just-started generator

print(g5.send("霸王龙"))  # 2. 给生成器函数上一个yield的位置传递一个数据(霸王龙)

# print(next(g5))  # 再次获取数据, (霸王龙)
# print(g5.send("abc"))







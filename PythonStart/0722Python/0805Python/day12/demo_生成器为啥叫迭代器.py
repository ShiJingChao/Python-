"""
    可迭代对象: 实现了__iter__方法的对象就是可迭代对象;
    迭代器: 实现了__iter__方法和__next__方法的对象就是迭代器;

        迭代器 是 可迭代对象;
        生成器 是 可迭代对象;
        生成器 是 迭代器;

        __iter__()方法的返回值是 迭代器;
        可迭代对象.__iter__(), 就会生成一个 迭代器;
    ---------------------

    生成器:
        1. 生成器表达式;
        2. 生成器函数; 函数中使用了关键字 yield ;
"""

g = (x for x in range(10))

print(dir(g))


def func():
    yield "我如此热爱的语言python"


g1 = func()  # <generator object func at 0x000000000212A548>
print(g1)

print(g1.__next__())



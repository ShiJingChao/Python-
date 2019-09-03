"""
     yield from 循环遍历容器中的每个元素;
"""


def func1():
    for x in "无齿翼龙":
        yield x
    for y in ["霸王龙", "棘龙", "万启龙"]:
        yield y


g1 = func1()
print(g1.__next__())  # 无
print(g1.__next__())  # 齿
print(g1.__next__())  # 翼
print(g1.__next__())  # 龙
print(g1.__next__())  # 霸王龙
print(g1.__next__())  # 棘龙
print(g1.__next__())  # 万启龙


def func2():
    yield from "无齿翼龙"
    yield from ["霸王龙", "棘龙", "万启龙"]


g2 = func2()
print(g2.__next__())
print(g2.__next__())
print(g2.__next__())
print(g2.__next__())
print(g2.__next__())
print(g2.__next__())
print(g2.__next__())



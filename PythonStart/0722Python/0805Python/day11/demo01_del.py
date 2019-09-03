"""
    魔术方法:
        就是类中的方法(预定义的方法), 魔术方法在某个特定的时机会被自动的调用;

    __del__():
        销毁对象之前, 被自动的调用;
"""


# class A:
#     pass
#
# a = A()  # 1. 开辟内存 2. 自动调用init方法
# print(a)  # <__main__.A object at 0x0000000001E0CA08>


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("%s 被销毁了..." % self.name)


p1 = Person("特朗普")
p2 = Person("港独")

del p1  # 删除特朗普  特朗普 被销毁了...

# 程序执行完毕, 所有内存都会被释放, 所有变量都会被销毁, 所以, p1,p2 的__del__()方法都会被执行
while True:
    pass


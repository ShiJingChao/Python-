"""
    __repr__(): print(对象) 打印对象时会被调用

        __str__(): print(对象) 打印对象时会被调用
                print(对象): 默认情况下打印结果是, 对象的内存地址;
                重写__str__()方法, 给这个方法一个字符串返回值, 返回的是啥, print(对象)打印的结果就是啥

    * 1. TypeError: __repr__ returned non-string (type NoneType)
     以上两个函数都必须有返回值, 且返回值类型为str类型;

    * 2. 打印对象时, 如果使用%s占位符, 默认调用的是__str__()方法
                     如果使用%r占位符, 默认调用的是__repr__()方法

    * 3. 有repr, 没有str时; %s, %r 都可调用repr方法;  (所以,我们称repr是str的备胎)
         没有repr, 有str是;  %s 调用的是str的方法;  %r 打印的是对象的地址(默认的);

    print(repr(对象))  默认调用__repr__()方法
    print(str(对象))  默认调用__str__()方法
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "我是str..."

    def __repr__(self):
        return "我是repr..."


p1 = Person("棘龙")
# print(p1)  # <__main__.Person object at 0x00000000025EF888>
# print("你猜猜我打印的是谁? %s" % p1)  # 你猜猜我打印的是谁? 我是str...
# print("你猜猜我打印的是谁? %r" % p1)  # 你猜猜我打印的是谁? 我是repr...

# 只有repr方法:
# print("你猜猜我打印的是谁? %s" % p1)  # 你猜猜我打印的是谁? 我是repr...
# print("你猜猜我打印的是谁? %r" % p1)  # 你猜猜我打印的是谁? 我是repr...

# 只有str方法
print("你猜猜我打印的是谁? %s" % p1)  # 你猜猜我打印的是谁? 我是str...
print("你猜猜我打印的是谁? %r" % p1)  # <__main__.Person object at 0x0000000001EA95C8>

print(repr(p1))
print(str(p1))



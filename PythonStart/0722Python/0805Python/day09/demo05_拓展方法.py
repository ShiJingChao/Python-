"""
    __init__:
        创建对象的时候,自动调用该方法;

    __str__:
        默认返回的是对象在内存中的地址;
        * print(对象)时, 自动调用;

        如果想让print(对象)时,打印输出其他内容;
            * 需要在类中重写 __str__方法:
            * 必须要有返回值, 并且返回值的类型是字符串类型;

"""


def get_sum(a, b):
    return a + b


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "啦啦啦 我是卖报的李小花"


print(sorted)  # <built-in function sorted>
print(type)  # <class 'type'>

p1 = Person("李小花")
print(p1)  # <__main__.Person object at 0x00000000021B9548>  啦啦啦 我是卖报的李小花
print(get_sum)  # <function get_sum at 0x00000000021B70D8>



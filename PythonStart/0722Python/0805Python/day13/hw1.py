"""
1.写个迭代器,传入一个数字,生成斐波那契数列;
	例如传入5,生成斐波那契的前5个数字;
"""


# 迭代器类
class Feibo:

    def __init__(self, count):  # 初始化实例变量(对象的属性)
        self.count = count  # 参数count: 迭代器对象生成的斐波那契数列的数字个数
        self.a = 1
        self.b = 1
        self.current = 1  # 用来计数,计算迭代器已迭代的数据个数

    def __iter__(self):  # 返回值必须是个迭代器
        return self

    def __next__(self):  # 获取数据
        # 1, 1, 2, 3, 5, 8, 13, 21,....
        # a, b
        #    a  b
        #       a  b
        if self.current <= self.count:
            t = self.a  # t = 1
            self.a, self.b = self.b, self.a + self.b  # a=2, b=3
            self.current += 1
            return t
        else:
            raise StopIteration


f = Feibo(5)  # 创建迭代器对象中1, 1, 2, 3, 5
print(f.__next__())  # 1
print(f.__next__())  # 1
print(f.__next__())  # 2
print(f.__next__())  # 3
print(f.__next__())  # 5

print(f.__next__())  # StopIteration





"""
    可迭代对象:
        对象实现了 __iter__()方法;
        可迭代对象调用__iter__()方法, 返回一个迭代器对象;

    迭代器对象:
        实现了__iter__()和__next__()方法的对象;
        __next__()依次获取数据的;
"""


# 写一个迭代器的类, 用来获取1,2,3,4,5,...,10, 这样的数据;
class Num:
    def __init__(self):
        self.num = 0

    def __iter__(self):  # 返回值: iterator 迭代器对象
        return self

    def __next__(self):
        if self.num > 9:
            raise StopIteration
        self.num += 1
        return self.num


n1 = Num()
print(n1.__next__())  # 获取一个数据: 1
print(n1.__next__())  # 获取一个数据: 2
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())

print("------")
# print(n1.__next__())  StopIteration

n2 = Num()
for x in n2:
    print(x)

# step1: 调用对象的__iter__()方法获取一个迭代器对象
# step2: 调用迭代器对象的__next__()方法依次获取数据
# step3: 遇到StopIteration停止迭代

# 写个迭代器, 传入一个范围(起始值, 终止值), 依次获取
# 这个范围中的素数


class PrimeNumber:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # 方法: 判断一个数是不是素数
    def isPrimeNumber(self, num):  # 参数: 你要判断是不是素数的那个数
        for x in range(2, num):
            if num % x == 0:
                return False  # 返回, 函数停止执行
        return True

    def __iter__(self):   # 返回个迭代器对象: generator(迭代器)--> __iter__(), __next__()
        for x in range(self.start, self.end+1):
            if self.isPrimeNumber(x):
                yield x

    # yield --> 生成器函数(返回值:生成器) --> 迭代器 --> __iter__()方法返回个迭代器

print("---------------------")
n3 = PrimeNumber(3, 20)
for x in n3:
    print(x)
    
# step1: 调用__iter__()获取迭代器 --> 生成器
# step2: 调用__next__()获取数据
# step3: StopIteration停止迭代

n4 = PrimeNumber(3, 20)
g4 = n4.__iter__()
print(g4.__next__())






"""
    需求: 使用生成器实现一个功能:
            1. 传递数据, 计算所有传递的数据的总和; --> 平均值
"""


def func1():
    sum_num = 0  # 用来记录所有数字的和, 初始值0
    count = 0
    avg = 0  # 用来记录所有数字的平均值, 初始值0
    while True:
        num = yield (sum_num, avg)
        count += 1  # 每输入一个数据, 计数+1
        sum_num += num  # 每输入一个数据, 和累加
        avg = sum_num / count


g1 = func1()

print(g1.__next__())  # 总和为0
print(g1.send(5))  # 获取总和5
print(g1.send(10))  # 获取总和15
print(g1.send(100))  # 获取总和115


# 写一个生成器, 生成斐波那契数列;
# 1, 1, 2, 3, 5, 8, 13, 21, ...
# a  b->2
#    a  b->3
def func2():
    a = 1  # 所求数的前两个数
    b = 1  # 所求数的前一个数
    while True:
        yield a  # 1, 1, 2, 3, 5,...
        a, b = b, a + b


g2 = func2()
print(g2.__next__())
print(g2.__next__())
print(g2.__next__())
print(g2.__next__())
print(g2.__next__())
print(g2.__next__())
print(g2.__next__())






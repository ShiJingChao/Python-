"""
    迭代:
        访问容器中元素的一种方式, 类似于遍历, 可以将某个数据集合中的元素一个挨着一个的取出来;

    1. 可迭代对象 Iterable
            一个实现了__iter__()方法的对象就是一个可迭代对象;
            (如果一个对象可以使用for进行循环遍历, 那么这个对象就是可迭代对象;)
            (1) 数据类型中: list, set, dict, str, tuple, range, map, filter
            (2) 生成器: generator

        * __iter__()方法调用之后, 返回一个迭代器对象iterator

        判断对象是否可迭代:
            from collections.abc import Iterable
            isinstance(对象, Iterable)

    2. 迭代器 Iterator
        如果一个对象实现了__iter__()方法, 并且实现了__next__()方法, 那么这个对象就是一个迭代器对象;

    3. for in 的底层原理
        for in 对象:
            step1: 调用对象的__iter__()方法, 生成一个iterator迭代器;
            step2: 调用迭代器对象的__next__()方法, 依次获取每个数据;
            step3: for in 在遇到 StopIteration 时, 停止迭代;

"""
from collections.abc import Iterable

g = (x for x in range(3))  # True
print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance(g, Iterable))  # True

# 1. set, list, dict, 都是可迭代对象; dir()
res_set = dir({1, 2, 3})
res_list = dir([1, 2, 3])
res_dict = dir({"key": "value"})
# print(res_set)
# print(res_list)
# print(res_dict)

# 2. 取交集, 查看三种对象共同拥有的方法
res = set(res_set) & set(res_list) & set(res_dict)
print(res)  # '__iter__'

# 3. 通过取交集查得,以上三种对象都有 __iter__方法
print("---------------------")
print([].__iter__())  # 实例方法的调用 此处为调用处 <list_iterator object at 0x00000000026C99C8>

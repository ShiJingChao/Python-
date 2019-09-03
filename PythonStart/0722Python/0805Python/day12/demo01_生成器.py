"""
    生成器: generator

        按照规则去生成一定的数据;

        列表推导式: 根据表达式去生成满足条件的数据; 快速的生成一个列表;
                列表 = [ 表达式 for item in 容器 if 条件]
                字典推导式, 集合推倒式;

             产生数据的时机不一样:
                列表推导式: 一次性生成所有满足条件的数据;
                生成器: 你要一个数据, 我生成出来给你一个;

    1. 生成器表达式:
            生成器对象 = (表达式 for item in 容器)
            生成器对象 = (表达式 for item in 容器 if 条件)
            生成器对象 = (表达式 for item in 容器 for item2 in 容器2)

    2. 通过生成器对象获取数据:
        1. next(g)
        2. for in 依次获取生成器对象中的每个数据
        3. g.__next__()

"""
# 生成1-10的数据的生成器
g = (x for x in range(1, 11))
print(type(g))  # <class 'generator'>
print(g)  # <generator object <genexpr> at 0x00000000007EA948>

print(next(g))  # 1 获取g对象的数据
print(next(g))  # 2
print(next(g))  # 3
print(next(g))  # 4

for x in g:
    print(x)   # 5, 6, 7, 8, 9, 10


# print(next(g))  # StopIteration

# 创建一个生成器对象, 包含1-10之间的所有偶数
g1 = (x for x in range(1, 11) if x % 2 == 0)

print(g1)  # <generator object <genexpr> at 0x000000000260A948>
print(type(g1))  # <class 'generator'>

print(g1.__next__())  # 2
print(g1.__next__())  # 4
print(g1.__next__())  # 6
print(g1.__next__())  # 8
print(g1.__next__())  # 10

print(g1.__next__())  # StopIteration



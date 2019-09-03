"""
    序列的解包:
        x, y, c = "abc"
"""
list1 = ['a', 'ab', 'abc']

# 1. 常规解包
x, y, z = list1
print(x, y, z)  # a ab abc

# 2. 使用*
# x, y = list1  # ValueError: too many values to unpack (expected 2)

x, *y = list1  # ['a', 'ab', 'abc']
print(x)  # a
print(y)  # ['ab', 'abc']

*x, y = list1
print(x)  # ['a', 'ab']
print(y)  # 'abc'

*x, y = ['李雪',]
print(x)  # []
print(y)  # '李雪'

x, *y = [100,]
print(x)  # 100
print(y)  # []

print("================")
s = '陈情令'
# *m, n
*m, n = s
print(m)  # ['陈', '情']
print(n)  # 令
print('--------------')
# n, *m
m, *n = s
print(m)  # 陈
print(n)  # ['情', '令']
print('--------------')
s1 = '羡'
# *m, n
*m, n = s1
print(m)  # []
print(n)  # 羡
print('--------------')
# m, *n
m, *n = s1
print(m)  # 羡
print(n)  # []
print('--------------')
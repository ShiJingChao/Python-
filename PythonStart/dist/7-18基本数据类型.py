# For循环
# for i in range(5):
#     print(i, end=' ')
# for i in range(3, 9):
#     print(i)
# for i in range(10, 20, 2):
#     print(i, end=' ')
# for i in range(18, 8, -3):
#     print(i, end=' ')

# 列表
# a = []
# b = [1, 2]
# print(type(a), a)
# print(type(b), b)

# a = [1, 'a', 'b', 'c']
# x = len(a)
# print('长度', x)
# print(a[0], a[1], a[2])
# a = [1, 'a', 'b', 'c']
# i = 0
# while i < len(a):
#     print('第', i + 1, '个值是：', a[i])
#     i += 1

# a = [1, 2]
# b = [3, 4, 5]
# c = a + b
# print(c)
# d = a * 3
# print(d)
# x = a[1] + b[2]
# print(x)
#


# a = ['a', 'b', 2, 3]
# for i in range(len(a)):
#     print(a[i], end=' ')


# 切片

# a = ['a', 'b', 'c', 1, 2, 3, 4, 5, 6, 7]
# b = a[2:5]  # 根据索引
# print(b)
# c = a[2:8:2]
# print(c)
# d = a[2:]
# print(d)
# e = a[:3]  # 不包含索引为3的数据
# print(e)

# b = a[-1]
# print(b)

# a = ['a', 'b', 'c', 1, 2, 3, 4, 5, 6, 7]
# for i in range(-1, -len(a) - 1, -1):
#     print(a[i], end=' ')

# *a, b = [1, 2, 3]
# print(a, b)


# 列表的方法列表的方法列表的方法列表的方法列表的方法

# a = [1, 2, 3, 4, 5]
# a.append(9)
# print(a)

# stus = ['孙悟空', '猪八戒', '沙僧']
# stus.append('唐僧')	#在列表最后加上“唐僧”
# print(stus)
# a = [1, 2, 3, 4, 5]
# b = [3, 4]
# a.extend(b)
# c = [5, 6]
# print(a)
#

# a = [1, 2, 3]
# b = a
# a.append(4)		# a和b所指的地址一样，改变a，b也变
# print(a)
# print(b)

# a = [1, 2, 3, 4, 5]
# a.insert(2, 'a')
# print(a)
# stus = ['孙悟空', '猪八戒', '沙僧']
# stus.insert(2, '唐僧')		# 2 为下标索引位置
# print(stus)

# a = [1, 2, 3, 4, 5]
# b = a.pop()
# print(b)
# b = a.pop(2)
# print(a, b)

# a = [1, 2, 3, 4, 5]
# a.remove(3)
# print(a)

# a = [1, 2, 3, 4, 5]
# del a[2]
# print(a)

# c = [1, 2, 3, 4]
# for i in range(len(c)):
#     del c[0]
# print(c)

# a[3] = 99
# print(a)

# a = [1, 2, 3, 4, 5]
# a.reverse()
# print(a)

# a = [3, 2, 1, 5, 7, 3, 8]
# a.sort()
# print(a)

# a = [3, 2, 1, 5, 7, 3, 8]
# b = sorted(a)
# print(b)

# a = [3, 2, 1, 5, 7, 3, 8]
# a.sort(reverse=True)
# print(a)

# a = 3
# b = 4
# t = a
# a = b
# b = t
# print(a, b)


# a = [3, 2, 1, 5, 7, 3, 8]
# b = a.count(3)
# print("3的个数：", b)
#
# a = [3, 2, 1, 5, 7, 3, 8]
# x = a.index(2)  # 返回第一次出现3的索引
# print(x)

# a = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
# for x in a:
#     for y in x:
#         print(y, end=',')
#     print()

# print(a[1][2], a[2][1])

# a = [1, 2, 3]
# b = a
# a.append(4)
# print(a)
# print(b)

# a = 3
# b = 3
# print(id(a))
# print(id(b))
# a = 'abc'
# b = 'abc'
# print(id(a))    # 两个的内存地址一样，那么所指向的数据为同一个
# print(id(b))

# a = 3
# b = 3
# print(a == b)
# print(a is b)
#
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# import copy
# a = [1, 2, 3, [4, 5], 6]
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
# a.append(7)
# a[3].append(99)
# print(a, id(a))
# print(b, id(b))
# print(c, id(c))
# print(d, id(d))

# 元组元组元组元组元组元组元组元组元组元组元组元组元组元组元组元组元组


# a = (1, 2, 3)
# print(a, type(a))
# print(a[0])
# a[0] = 9  # 报错，元组不可修改TypeError: 'tuple' object does not support item assignment


# a = (1, 2, 3, 4)
# b = (1, 2)
# i = 0
# while i < len(a):
#     print(a[i], end=' ')
#     i += 1

# a = (1, 2, 3, 4)
# print(a[2::1])  # 运行结果：(3, 4)

# c = a + b
# print(c)
# d = a * 2
# print(d)
# 运行结果
# (1, 2, 3, 4, 1, 2)
# (1, 2, 3, 4, 1, 2, 3, 4)

# a, b, c = (1, 2, 3)
# print(a)
# print(b, c)
# 运行会报错
# a, *b = (1, 2, 3)
# print(a)
# print(b)
# 运行结果
# 1
# [2, 3]

# a = (1, 2, 3, [4, 5])
# a[3].append(9)
# print(a)
# 运行结果   元组不可修改，但是元组中的列表可以修改
# (1, 2, 3, [4, 5, 9])

# a = (1, 2, 3)
# b = tuple(a)
# print(b)
# c = list(b)
# print(c)    #强制类型转换，把元组b转换为列表
# 运行结果
# (1, 2, 3)
# [1, 2, 3]

# a = ('a', 'b', 'c', 'e')
# b = a.index('b', 1, 2)  # index  索引  1,2为索引范围，范围内不存在会报错
# print(b)

# a = (('张三', 19), ('李四', 20), ('王五', 30))

# for x in a:
#     print(x)

# a = ('a', 'b', 'c', 'e')
# for x in enumerate(a):  # 加上索引值
#     print(x)
# 运行结果
# (0, ('张三', 19))
# (1, ('李四', 20))
# (2, ('王五', 30))


# 练习练习练习练习练习练习
# a = (1, 2, 3, 4, 5, 6)
# he = 0
# i = 0
# while i < len(a):
#     he += a[i]
#     i += 1
# print(he)

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14)
# gs = 0  # 个数
# for x in a:
#     if x % 7 == 0 or x % 10 == 7:
#         gs += 1
#         print(x, '是')
# print(gs)


# a = (1,)
# b = (1)
# c = 1, 2
# print(type(a))
# print(type(b))
# print(type(c))


# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14)
# # js = 0  # 奇数
# # os = 0  # 偶数
# # i = 0
# # while i < len(a):
# #     if a[i] % 2 == 0:
# #         os += 1
# #     else:
# #         js += 1
# #     i += 1
# # print(os, js)

# 找出元组中最大最小值以及他们的下标

# for方法

# a = (3, 2, 5, 1, 4, 9, 7)
# max = a[0]
# max_i = 0
# min = a[0]
# min_i = 0
# i = 0
# for i in a:
#     if i > max:
#         max = i
#         max_i = a.index(i)
#     if i < min:
#         min = i
#         min_i = a.index(i)
# print(max, max_i, '\n', min, min_i)

# while方法

# a = (3, 2, 5, 1, 4, 9, 7)
# max = a[0]
# max_i = 0
# min = a[0]
# min_i = 0
# i = 0
# while i < len(a):
#     if a[i] > max:
#         max = a[i]
#         max_i = i
#     elif a[i] < min:
#         min = a[i]
#         min_i = i
#     i += 1
# print(max, max_i)
# print(min, min_i)


# 把列表相加输出

# a = [1, 2, 3, 3, 2, 5]
# b = [11, 22, 8, 7, 5, 9]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i] + b[i])
#     i += 1
# print(c)


# a = [1, 2, 3, 4, 5, 6]
# t = a[0]
# i = 0
# while i < len(a) - 1:
#     a[i] = a[i + 1]
#     i += 1
# a[i] = t
# print(a)


# 上面运行的过程

# import time
#
# a = [1, 2, 3, 4, 5, 6]
# while True:
#     t = a[0]
#     i = 0
#     while i < len(a) - 1:
#         a[i] = a[i + 1]
#         i += 1
#     a[i] = t
#     print(a)
#     time.sleep(1)

# 倒序输出
# a = [1, 2, 3, 4, 5, 6]
# i = 0
# while i < len(a) // 2:
#     t = a[i]
#     a[i] = a[len(a) - 1 - i]
#     a[len(a) - 1 - i] = t
#     i += 1
# print(a)

# 同上
# i = 0
# j = len(a) - 1
# while i < j:
#     t = a[i]
#     a[i] = a[j]
#     a[j] = t
#     i += 1
#     j -= 1
# print(a)

# a = 3
# b = 4
# a, b = b, a
# print(a, b)

# 同上

# a = [1, 2, 3, 4, 5, 6]
# i = 0
# j = len(a) - 1
# while i < len(a) // 2:
#     a[i], a[j] = a[j], a[i]
#     i += 1
#     j -= 1
# print(a)

# a = [1, 2, 3, 4, 1, 2, 5, 1, 1, 2]
# b = [1, 2]
# i = 0
# k = 0
# while i < len(a) - 1:
#     if a[i] == b[0] and a[i + 1] == b[1]:
#         k += 1
#     i += 1
# print(k)

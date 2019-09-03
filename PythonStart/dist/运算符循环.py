# stu = True
# if not stu:
#     print('不是学生')
# else:
#     print('是学生')
# 运行结果为是学生

# a = 5
# b = a > 7 or 4
# print(b)
# 运行结果为4

# a = 5
# b = a > 3 or 4
# print(b)
# 运行结果为：True

# b = 10
# a = 7 if b > 10 else 8
# print(a)
# 运行结果为：8

# i = 1
# while i < 5:
#     print(i, '<5')
#     if i == 3:
#         break
#     i += 1
# else:
#     print(i, '不成立')
# 1<5
# 2<5
# 3<5

# 嵌套循环输出2~100之间的素数
# import math
# for i in range(2, 100):
#     a = int(math.sqrt(i))
#     for j in range(2, a + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# 输入一个数判断是否为素数
# sushu = int(input('请输入一个数：'))
# import math
#
# a = int(math.sqrt(sushu))
# i = 2
# while i < a + 1:
#     if sushu % i == 0:
#         print('不是素数')
#         break
#     i += 1
# else:
#     print('是素数')

# import math
#
# sushu = int(input('输入一个数：'))
# a = int(math.sqrt(sushu))
# for i in range(2, a + 1):
#     if sushu % i == 0:
#         print('不是素数')
#         break
# else:
#     print('是素数')

# 把2到100的素数放到数组里
# import math
#
# shuzu = []
# for i in range(2, 100):
#     a = int(math.sqrt(i))
#     for j in range(2, a + 1):
#         if i % j == 0:
#             break
#     else:
#         shuzu.append(i)
# print(shuzu)

import math

# shuzu = []
# i = 2
# while i < 100:
#     a = int(math.sqrt(i))
#     j = 2
#     while j < a + 1:
#         if i % j == 0:
#             break
#         j += 1
#     else:
#         shuzu.append(i)
#     i += 1
# print(shuzu)

# 打印5*5的星号
# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print('*', end='')
#         j += 1
#     i += 1
#     print()

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print('*', end='')
#         j += 1
#     print()
#     i += 1

# for i in range(6):
#     for j in range(i):
#         print('*', end='')
#     print()

# for i in range(5):
#     for j in range(5-i):
#         print('*',end='')
#     print()

# for i in range(5):
#     for j in range(i):
#         print(' ', end='')
#     for j in range(5-i):
#         print('*', end='')
#     print()

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, '*', i, '=', j * i, end='  ')
#     print()

# for i in range(1, 10):
#     j = 1
#     while j < i + 1:
#         print(j, '*', i, '=', j * i, end='  ')
#         j += 1
#     print()

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         if i == 1 or i == 5 or j == 1 or j == 5:
#             print('*', end='')
#         else:
#             print(' ', end='')
#         j += 1
#     i += 1
#     print()


# 字典
# a = {'name': '张三', 'age': '19', 'sex': '男'}
# print(a['name'])
# print(a['age'])
# print(a)

# a['score'] = 99
# print(a)
# a['age'] = 18
# print(a)

# 添加
# a.setdefault('age',22)
# print(a)
# a.setdefault('score',100)
# print(a)

# b = a.pop('age')
# print(b)
# print(a)

# a.clear()
# print(a)

# del a['age']
# print(a)
# print(a.keys())

# for k in a.keys():
#     print(k)
# for i in a.values():
#     print(i)

# for k, i in a.items():
#     print(k, i)

# print(len(a))

# if 'name' in a:
#     print('有')
# else:
#     print('无')

# if 'name' in a.keys():
#     print('有')
# if '张三' in a:   # 只对键起作用，无法找值
#     print('zai')

# a = {'name': '张三', 'age': '19', 'sex': '男'}
# b = []
# c = {}
# for k, v in a.items():
#     b.append((k, v))  # 把（'name','张三'）
    # ('age', '19')('sex', '男')作为元组存列表b中
# print(b)
# for i in b:
#     c[i[0]] = i[1]  #   i[0]就是（'name','张三'）的'name',('age', '19')的age，字典的赋值就是c[键]=值
# print(c)

# 可以把上面的第二段for循环代码换成下面的  一样

# for x, y in b:
#     c[x] = y
# print(c)

# a = {'name': '张三', 'age': '19', 'sex': '男', 'age': '20'}
# print(a)  # 键名相同，键值会被后面的代替

# a = {
#     '001': {'name': '张三', 'age': '19', 'sex': '女'},
#     '002': {'name': '张三', 'age': '19', 'sex': '男'},
#     '003': {'name': '张三', 'age': '19', 'sex': '女'},
#     '004': {'name': '张三', 'age': '19', 'sex': '女'}
# }

list1 = [99, 16, 34, -988, 0.123]
list1.sort(reverse=True)
print(list1)

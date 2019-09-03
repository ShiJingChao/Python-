# stu = True
# if not stu:
#     print('你不是学生')
# else:
#     print('你是学生')

# or前面的判断不成立，则值取决于后面

# a = 5
# b = a > 7 or 4
# print(b)  # 运行结果为4
#
# a = 5
# b = a > 3 or 4
# print(b)  # 运行结果为True
#
# b = 10
# a = 7 if b > 10 else 8
# print(a)    # 运行结果为 8

# i = 1
# while i < 5:
#     print(i, '<5')
#     if i == 3:
#         break  # break管控范围包含else，break跳出后不运行else语句
#     i += 1
# else:
#     print(i, '不成立')

# 作业3 嵌套循环输出2~100之间的素数
# import math
#
# for i in range(2, 100):
#     a = int(math.sqrt(i))
#     for j in range(2, a + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#
# sushu = int(input('请输入一个数：'))
# i = 2
# while i < sushu:
#     if sushu % i == 0:
#         break
#     i += 1
# if i == sushu:
#     print('是素数')
# else:
#     print('不是')
#
# sushu = int(input('请输入一个数：'))
# i = 2
# while i < sushu:
#     if sushu % i == 0:
#         print(sushu, '不是')
#         break
#     i += 1
# else:
#     print(sushu, '是')

# import math
#
# sushu = int(input('输入'))
# a = int(math.sqrt(sushu))
# for i in range(2, a + 1):
#     if sushu % a == 0:
#         print('不是质数')
#         break
# else:
#     print('是质数')

# # import math
# b = []
# for i in range(2, 100):
#     a = int(math.sqrt(i))
#     for j in range(2, a + 1):
#         if i % j == 0:
#             break
#     else:
#         b.append(i)
# print(b)

# a = []
# i = 2
# while i < 100:
#     j = 2
#     while j < i:
#         if i % j == 0:
#             break
#         j += 1
#     else:
#         a.append(i)
#     i += 1
# print(a)

# j = 1
# while j <= 5:
#     i = 1
#     while i <= 5:
#         print('*', end='')
#         i += 1
#     print()
#     j += 1

# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#     print()
# i = 0
# while i < 5:
#     j = 0
#     while j <= i:
#         print('*', end='')
#         j += 1
#     print()
#     i += 1
#
# for i in range(5):
#     for j in range(5 - i):
#         print('*', end='')
#     print()

# for i in range(5):
#     for j in range(i):
#         print(' ', end='')
#     for j in range(5 - i):
#         print('*', end='')
#     print()
#-------------------------------------------------
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(' ', end='')
#         j += 1
#     j = 1
#     while j <= 6 - i:
#         print("*", end='')
#         j += 1
#     print()
#     i += 1

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, "*", i, '=', j * i, end=' ')
#     print()

# for i in range(1, 10):
# #     j = 1
# #     while j <= i:
# #         print(j, '*', i, '=', j * i, end='  ')
# #         j += 1
# #     print()
# #     i += 1

# i = 1
# while i < 10:
#     for j in range(1, i + 1):
#         print(j, '*', i, '=', i * j, end=' ')
#     print()
#     i += 1


# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         if i == 1 or i == 5 or j == 1 or j == 5:
#             print('*', end='')
#         else:
#             print(' ', end='')
#         j += 1
#     print()
#     i += 1


# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or i == 5 or j == 1 or j == 5:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


# 字典#字典#字典#字典#字典#字典#字典#字典#字典#字典#字典#字典#字典#字典
# a = {'name': '张三', 'age': '19', 'sex': '男'}
# print(a['name'])
# print(a['age'])
# key 是不可修改的数据类型
# print(a)

# a['score'] = 99
# print(a)
# a['age'] = 18
# print(a)

# a.setdefault('age', 20)  # 只能添加，如果字典有相同的key，字典不会改变
# print(a)
# a.setdefault('score', 99)
# print(a)

# b = a.pop('name')
# print(b)
# print(a)

# b=a.popitem()
# print(b)
# print(a)
#
# a.clear()
# print(a)

# del a # 把a整个字典删除，无法输出
# del a['age']
# print(a)
# print(a.keys())
#
# for k in a.keys():  # 显示字典所有的键值
#     print(k)
# for i in a.values():  # 显示字典所有的value值
#     print(i)
# for j in a.items():  # 显示字典所有的键值对
#     print(j)
# for k, v in a.items():  # 拆分开键值对
#     print(k, v)

# print(len(a))

# a = {'name': '张三', 'age': '19', 'sex': '男'}
# b = {'name': '李四', 'score': 90}
# a.update(b)
# print(a)


# a = {'name': '张三', 'age': '19', 'sex': '男'}
# if 'name' in a:
#     print('有')
# if 'name' in a.keys():  #和上一个效果一样，但是如果name没有引号，上一个就有错
#     print('有')
# if 'score' not in a:    # 只对键 起作用，对值不起作用
#     print('没有')
# if '张三' in a:   # 不显示
#     print('zai')

# a = {'name': '张三', 'age': '19', 'sex': '男'}
# b = []
# c = {}
# for k, v in a.items():
#     b.append((k, v))
# print(b)
# for j in b:
#     c[j[0]] = j[1]
#     print(j[1])
# print(c)

# for x, y in b:
#     c[x] = y
# print(c)


# a = {'name': '张三', 'age': '19', 'sex': '男','age': '20'}
# print(a)    # age会被后面的覆盖

# a = {
#     '001': {'name': '张三', 'age': '19', 'sex': '女'},
#     '002': {'name': '张三', 'age': '19', 'sex': '男'},
#     '003': {'name': '张三', 'age': '19', 'sex': '女'},
#     '004': {'name': '张三', 'age': '19', 'sex': '女'}
# }

# for k, v in a.items():
#     print('num:', k, end=',')
#     for k1, v1 in v.items():
#         print(k1, ':', v1, end=',')
#     print()

# 同上
# for k in a.keys():
#     print('num', k, end=',')
#     for k1 in a[k].keys():
#         print(k1, ':', a[k][k1], end=',')
#     print()

# a = {
#     '001': {'name': '张三', 'age': '19', 'sex': '女'},
#     '002': {'name': '张三', 'age': '19', 'sex': '男'},
#     '003': {'name': '张三', 'age': '19', 'sex': '女'},
#     '004': {'name': '张三', 'age': '19', 'sex': '女'}
# }
# for k, v in a.items():
#     for k1, v1 in v.items():
#         if v1 == '男':
#             v.setdefault('salary', 1000)
#             break
# for k, v in a.items():
#     print(k, v)
#
#
#
# for k in a.keys():
#     if a[k]['sex'] == '男':
#         a[k]['salary'] = 1000
# print(a)
# for k, v in a.items():
#     print(k, v)

# 集合集合集合集合集合集合集合集合集合

# a = {1, 2, 3, 4, 3, 3, 3, 3}
# print(a, type(a))
# c = {}
# print(type(c))
# b = set()
# print(type(b))

#
# 集合是无序的，不支持索引（字典也是无序的，不支持索引）
# a.add(9)
# a.add(9)    # 重复添加只会添加一个。唯一的。
# print(a)
# print(a[0]) # 集合是无序的，不支持索引（字典也是无序的，不支持索引）

# b = [1, 2, 3]
# a = set(b)
# print(a)  # 运行结果：{1, 2, 3}
# c = '1234'
# d = set(c)
# print(d)  # 运行结果：{'1', '4', '3', '2'}

# a = {1, 2, 3, 4}
# for x in a:
#     print(x)

# a = {1, 2, 3, 4}
# a.update([1, 2, 5, 6])
# print(a)    # 运行结果：{1, 2, 3, 4, 5, 6}

# b = {'name': 'zhangsan', 'age': 18}
# a = set(b)
# print(a)    # 运行结果:{'age', 'name'} 字典转集合时，去掉key值

# a = {1, 2, 3, 4}
# b = a.pop()
# print(b)        # 运行结果：1
# print(a)        # 运行结果：{2, 3, 4}

# a = {1, 2, 3, 4}
# a.remove(2)
# print(a)    # 运行结果：{1, 3, 4}

# a = {1, 2, 3, 4}
# a.clear()
# print(a)  # 运行结果：set()

# a = {1, 2, 3, 4}
# # # del a
# # # print(a)    # 运行结果：NameError: name 'a' is not defined 彻底删除


# a = [1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 3, 3]
# for i in set(a):
#     print(i, '出现了', a.count(i), '次')

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = a.intersection(b)
# d = a & b  # & 与  || 或
# print(c)  # 运行结果：{3, 4}
# print(d)  # 运行结果：{3, 4}

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# e = a - b
# f = a.difference(b)
# g = b - a
# print(e)  # 运行结果：{1, 2}
# print(f)  # 运行结果：{1, 2}
# print(g)  # 运行结果：{5, 6}


# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# g = a ^ b
# f = a.symmetric_difference(b)
# print(g)
# print(f)

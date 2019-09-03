# dirt1 = {'name': '张三', 'age': 18, 'sex': '男', '班级': '15'}

# c = {}
# for k, v in dirt1.items():
#     c[v] = k

# count = 0
# for i in range(1, 101):
#     if i % 3 == 0 and i % 7 == 0:
#         continue
#     elif (i % 3 == 0 and i % 7 != 0) or (i % 3 != 0 and i % 7 == 0):
#         count += 1
# print(count)
from collections import deque

# prices = {
#     'GOOG': 700.4,
#     'ACME': 45.23,
#     'APLE': 112.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75,
#     'MSFT': 204.4
# }
#
# # value值大于200的子集。
# p1 = {key: value for key, value in prices.items() if value > 200}
# print(p1)
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1 & set2)
# print(set1 ^ set2)
# import copy
#
# lst = [1, 2, (3, 4, [5])]
# lst2 = copy.copy(lst)
# lst3 = copy.deepcopy(lst)
# lst[2][2].append(2)
# print(lst2)
# print(lst3)
# a = 5
# id1 = id(lst[2][2][0])
# id2 = id(lst2[2][2][0])
# id3 = id(lst3[2][2][0])
# print(id1)
# print(id2)
# print(id3)
# print(id(a))
# count = 0
# for i in range(1, 101):
#     if (i % 3 == 0 and i % 7 != 0) or (i % 3 != 0 and i % 7 == 0):
#         count += 1
#     elif i % 3 == 0 and i % 7 == 0:
#         continue
# print(count)

# dict1 = {'name': '小明', 'age': 18, 'weight': 180, 'score': 150}
# dict2 = {}
# for k, v in dict1.items():
#     dict2[v] = k
# print(dict2)
# xiaoming_dict = {'name': '小明',
#                  '1': 2,
#                  '3': 4}
#
# for k in xiaoming_dict:
#     print('%s-%s' % (k, xiaoming_dict[k]))




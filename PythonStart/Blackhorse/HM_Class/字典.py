# 使用多个键值对，存储描述一个物体的相关信息——描述更复杂的数据信息
# 将 多个字典放在一个列表中，再进行遍历
# card_list = [
#     {"name": "张三",
#      "qq": "123",
#      'phone': "110"},
#     {"name": "张si",
#      "qq": "1234",
#      'phone': "220"},
#
# ]
# for card_info in card_list:
#     print(card_info)

# 列表[] 元组() 字典{} 集合{}  嵌套 取数据
# 列表可以存储重复数据
# 元组和列表一样，就是不可修改
# 字典是无序的 列表和元组是有序的，集合是不重复序列
# 字典的键是不能重复的，如果出现重复的，后面的会替换掉前面的
# 集合是无序的，唯一的，不可修改的,可以盛放多个数据类型的一种类型,集合中的元素也必须是不可修改类型
# 集合的创建格式
# （1） 变量名= {元素1，元素2，元素3}
# （2） 变量名 = set(序列) 例如：变量名= set(元组，自动，字符串)
# （这里指的可修改是指对集合来说，例如：
# set = {'hha'}
# set.add('xii')
# print(set)
# print(type(set))
# set.update({'xii','heh'})   # 更新里如果有重复的内容，则不会添加
# print(set)
# 集合的创建 使用大括号{}或者set（）创建集合
# 字典的键值可以是任何不可变的对象
# 列表嵌套元组，字典，集合
# 元组是以逗号分隔的以小括号包围的不可修改的有序序列，可以当做不可修改的列表 可重复 支持合并
# 元组中可变数据类型中的元素可以改变,元组里可以存储任何类型数据
# turble = ([123], {"123": 321}, {123, 34}, (23, 32))
# turble[1]["123"] = 321
# print(turble)
# list = [{"name": "张si",
#          "qq": "1234",
#          'phone': "220"}, {111, 222, 333, 444}, (123, 234, 345), (123, 234, 345), [1, 2, 3, [4, 5, 6]]]
#
# turple = ("123", "231", "dsdas", "123", [1, 2, 3], {1, 2, 3}, {"123": 213}, False, (123, 235))
# zidian = {'001': [123,345,765],
#           '002': {'name': '张三', 'age': '19', 'sex': '男'},
#           '003': {'name': '张三', 'age': '19', 'sex': '女'},
#           '004': {'name': '张三', 'age': '19', 'sex': '女'}}
# # jihe = {{"123": 213}, {111, 222, 333}, (123, 456)}
# print(zidian)
# print(turple)
# a = list[4][3][1]
# b= list[2][1]
# c = list[0]
# print(a)
# print(b)
# print(c)
# print(list)
# print(turple)
# print(jihe)

# dict = {"k1": "v1", "k2": "v2", "k3": "v3"}
# 遍历字典所有的key值
# for i in dict.keys():
#     print(i)
# # 遍历字典所有的value值
# for j in dict.values():
#     print(j)
# 遍历字典所有的key值和value值
# a = []
# b = []
# for k, v in dict.items():
#     a.update(k)
#     b.update(k)
# print(a)
# print(b)
#
# 在字典里添加一个键值对，"k4":"v4"，输出添加后的字典
# dict["k4"] = "v4"
# print(dict)
# 或者
# dict.setdefault("k4","v4")
# print(dict)

# 请删除字典中键值对"k1":"v1",并输出删除后的结果

# del dict["k1"]
# print(dict)
# 或者
# dict.pop("k1")
# print(dict)
# 字典中没有remove 这个方法
# clear  不可以传参，所以用clear就是清空
# print("删除不存在的k5,不报错，返回值: ", dict.pop("k5", None))

# 现有dict2 = {"k1":"v11","a":"b"},
# 通过一行操作使dict2 = {"k1":"v1","k2":"v2","k3":"v3","a":"b"}
# dict2 = {"k1": "v11", "a": "b", "k1": "v12"}
# dict1 = {"k1":"v1","k2":"v2","k3":"v3","a":"b"}
# dict2.update(dict1)
# print(dict2)

lis = [["k", ["qwe", 20, {"k1": ["tt", 3, "1"]}, 89], "ab"]]
# 10.1、将列表中的数字变成字符串"100"(用两种方法)
# lis[0][1][1] = "100"
# lis[0][1][3] = "100"
# lis[0][1][2]["k1"] = ["tt", "100", "100"]
# print(lis)
# lis[0][1][2]["k1"][2] = 100
# print(lis)
# for i in lis[0][1][2].values():
#     if i == 1:


# print(lis[0][1][2].get("k1")[1].)
# print(lis)
# 10.2、将列表中的字符串"1"变成数字101(用两种方法)


# msg_list = [
#     {'id': 1, 'content': 'xxx', 'parent_id': None, },
#     {'id': 2, 'content': 'xxx', 'parent_id': None, },
#     {'id': 3, 'content': 'xxx', 'parent_id': None, },
#     {'id': 4, 'content': 'xxx', 'parent_id': 1, },
#     {'id': 5, 'content': 'xxx', 'parent_id': 4, },
#     {'id': 6, 'content': 'xxx', 'parent_id': 2, },
#     {'id': 7, 'content': 'xxx', 'parent_id': 5, },
#     {'id': 8, 'content': 'xxx', 'parent_id': 3, },
# ]

# 得到以下结果
# [<br>{'id': 1, 'content': 'xxx', 'parent_id': None, 'child': [{'id': 4, 'content': 'xxx', 'parent_id': 1, 'child': [{'id': 5, 'content': 'xxx', 'parent_id': 4, 'child': [{'id': 7, 'content': 'xxx', 'parent_id': 5, 'child': []}]}]}]},
# {'id': 2, 'content': 'xxx', 'parent_id': None, 'child': [{'id': 6, 'content': 'xxx', 'parent_id': 2, 'child': []}]},
# {'id': 3, 'content': 'xxx', 'parent_id': None, 'child': [{'id': 8, 'content': 'xxx', 'parent_id': 3, 'child': []}]},<br>]




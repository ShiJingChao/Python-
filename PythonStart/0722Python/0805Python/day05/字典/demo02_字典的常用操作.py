"""
    字典的常用操作:
        增:
            1. 通过添加键值对的方式
                字典名[key] = value
            2. setdefault(k, default)
                k : 键
                default : 默认值
                键不存在时, 将键值对添加到字典中;
                键存在时, 不做任何操作;
        删:
            .pop(key) 根据key值删除字典中的指定键值对
            .popitem() 随机删除字典中的某个键值对, 数据量较小的时候, 给我们的感觉是删除最后的
            .clear() 清空字典, ---> 变成一个空字典

            del 字典        删除字典
            del 字典[key]   删除字典中的指定键值对
        改:
            1. 通过键值对的方式
                字典名[key] = value
                        key存在时, 修改;
                        key不存在时, 添加;
            2. update()
                update(key=value)
                        key存在时, 修改覆盖
                        key不存在时, 添加
        查:
            1. 通过key获取value
                字典名[key]  如果key不存在, KeyError
                字典名.get(key)  如果key不存在, 返回一个None

            2. .keys()  一次性获取所有的key
            3. .values()  一次性获取所有的value
            4. .items()  一次性获取所有的键值对

"""
# 可以通过增加键值对的方式, 给字典添加数据
# 字典名[key] = value
d1 = {}
d1["姓名"] = "小黄花"
print(d1)  # {'姓名': '小黄花'}

# setdefault
d1.setdefault('color', 'yellow')
print(d1)  # {'姓名': '小黄花', 'color': 'yellow'}

d1.setdefault('姓名', '小黄')
print(d1)  # {'姓名': '小黄花', 'color': 'yellow'}

# 删除操作
d1.pop('color')  # 参数为key, 参数为必传参数
print(d1)  # {'姓名': '小黄花'}

d2 = {'name': "李小花", "age": 18, "sex": "女", "class": "python", "face": "beautiful"}
d2.popitem()  # 随机删除一个键值对
print(d2)

d2.popitem()
print(d2)

del d2['name']  # {'age': 18, 'sex': '女'}
print(d2)  # 也可以用来删除某一个键值对

# d2.clear()
# print(d2)  # {}

# del d2  # d2这个字典被删除了
# print(d2)  # NameError: name 'd2' is not defined

# 修改
# 字典[key] = value  --> 如果key不存在, 增加; 如果key存在, 修改;
d2['age'] = 81
print(d2)  # { 'age': 81, 'sex': '女'}

d2.update(sex='男')  # {'age': 81, 'sex': '男'}
print(d2)

d2.update(name="隔壁老王")  # {'age': 81, 'sex': '男', 'name': '隔壁老王'}
print(d2)

# 查找操作
# 1. 一次性获取字典中的所有的key
print(d2.keys())  # dict_keys(['age', 'sex', 'name'])

# 2. 一次性获取字典中的所有的value
print(d2.values())  # dict_values([81, '男', '隔壁老王'])

# 3. 一次性获取字典中的所有的键值
print(d2.items())  # dict_items([('age', 81), ('sex', '男'), ('name', '隔壁老王')])

# for.. in..

for v in d2.values():
    print(v)

print("-----------")

for k in d2.keys():
    print(k)

print("-----------")

for x in d2.items():
    k, v = x  # ('age', 81)

for k, v in d2.items():
    print(k ,v)

# 通过key获取value
# 格式 字典名[key]
print(d2['name'])  # 隔壁老王
# print(d2['abc'])  # KeyError: 'abc'

# get(key)
print(d2.get('name'))  # 隔壁老王
print(d2.get('abc'))  # None


# 获取字典的长度
print(len(d2))  # 3

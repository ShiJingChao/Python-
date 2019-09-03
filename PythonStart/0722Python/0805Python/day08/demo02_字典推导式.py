"""
    2. 字典推导式
        是列表推导式思想的延续, 语法结构差不多, 只不过最终产生的是字典而已

        语法结构:
            dict = { key表达式 : value表达式 for item in 容器}
            dict = { key表达式 : value表达式 for item in 容器 if 条件}
            dict = { key表达式 : value表达式 for item1 in 容器1 for item2 in 容器2}

"""
# 1. 字典, 将字典中的key,value进行互换
dict1 = {"name": "rose", "age": 17, "sex": "女"}
dict2 = {v: k for k, v in dict1.items()}
print(dict2)  #{'rose': 'name', 17: 'age', '女': 'sex'}

# 2. 使用字典推导式, 将list1中的元素作为key, 将list2中的元素作为value, 产生一个字典
list1 = ["施耐庵", "吴承恩", "曹雪芹", "罗贯中"]
list2 = ["水浒传", "西游记", "红楼梦", "三国演义"]
dict3 = {x: list2[list1.index(x)] for x in list1}
print(dict3)
dict4 = {list1[x]: list2[x] for x in range(len(list1))}
print(dict3)

# zip() 打包, 将多个可迭代对象(序列)中的相同索引值的元素, 放在一个元组里, 最终将所有的元组组成一个新的可迭代对象
dict5 = {k: v for k, v in zip(list1, list2)}  # [(施耐庵, 水浒传) (吴承恩,西游记) (曹雪芹,红楼梦) (罗贯中,三国演义)]
print(dict5)





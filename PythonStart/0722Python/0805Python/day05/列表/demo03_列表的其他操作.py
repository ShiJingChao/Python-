"""
    列表的其他操作
        增
            .append(obj) 末尾追加
            .insert(index, obj) 在指定位置添加元素
            .extend(iterable) 可迭代对象(序列), 将序列中的元素一次性的追加在列表的末尾
            +
            *
        删
            .pop(index) 删除指定索引值的元素
            .pop() 默认删除最后一个元素
            .remove(obj) 删除指定的元素
            .clear() 清空列表, ---> 空列表

            del python内置的关键字 功能是删除
                del list[index] 可以用来删除列表中的某个指定索引值的元素
                del list 也可以用来删除整个列表
                del str 也可以用来删除一个字符串
        改
            1. 通过索引值进行更改 --> 列表名[索引值] = 新值
            2. .reverse() : 反转这个列表, 将列表中的元素倒过来
            3. .sort(key, reverse=False)
                        key: 排序的规则
                        reverse: 默认为False  正序
                                可以修改为True  倒序
        查
            .count(obj) 查询元素在列表中出现的次数
            .index(obj) 查询元素从左开始第一次出现在列表中的索引值,查询不到报错
"""
# 列表的增加操作
list1 = ['潘安', '周星星', '兰陵王', '宋玉']

# 末尾追加
list1.append('杨长春')  # ['潘安', '周星星', '兰陵王', '宋玉', '杨长春']
print(list1)

# 插入, 参数1:插入位置的索引值 参数2:插入的元素
list1.insert(1, '老韩')
print(list1)

# 用于在列表的末尾一次性将另一个列表中的所有元素追加进去
list1.extend(['西施', '赵丽颖', 'Ella', '杨千烨'])
print(list1)  # ['潘安', '老韩', '周星星', '兰陵王', '宋玉', '杨长春', '西施', '赵丽颖', 'Ella', '杨千烨']

list1.extend('奥斯特洛夫斯基')
print(list1)  # ['潘安', '老韩', '周星星', '兰陵王', '宋玉', '杨长春', '西施', '赵丽颖', 'Ella', '杨千烨', '奥', '斯', '特', '洛', '夫', '斯', '基']

# + , *

# 删除
# 1. pop 删除指定索引值的元素, 默认删除最后一个元素
list1.pop(0)
print(list1)  # ['老韩', '周星星', '兰陵王', '宋玉', '杨长春', '西施', '赵丽颖', 'Ella', '杨千烨', '奥', '斯', '特', '洛', '夫', '斯', '基']

list1.pop()
print(list1) # ['老韩', '周星星', '兰陵王', '宋玉', '杨长春', '西施', '赵丽颖', 'Ella', '杨千烨', '奥', '斯', '特', '洛', '夫', '斯']

# 2. remove()  # 删除指定的元素
list1.remove('Ella')
print(list1)  # ['老韩', '周星星', '兰陵王', '宋玉', '杨长春', '西施', '赵丽颖', '杨千烨', '奥', '斯', '特', '洛', '夫', '斯']

# 3. clear 清空
# list1.clear()
# print(list1)  # []

# 4. del 删除, python内置的关键字
del list1[0]  # 删除列表中索引值为0的元素
print(list1)  # ['周星星', '兰陵王', '宋玉', '杨长春', '西施', '赵丽颖', '杨千烨', '奥', '斯', '特', '洛', '夫', '斯']

del list1
# print(list1)  # NameError: name 'list1' is not defined

# 修改
# 1. 通过索引值修改
list2 = ["红楼梦", "西游记", "三国演义", "水浒传"]
list2[2] = "罗贯中"
print(list2)  # ['红楼梦', '西游记', '罗贯中', '水浒传']

# 2.反转列表
list2.reverse()
print(list2)  # ['水浒传', '罗贯中', '西游记', '红楼梦']

# 3. 高阶函数
# 排序函数 sort()
list3 = [100, 45, 89, 36, -121, 45]
list3.sort()  # sort(key, reverse) key:用来规定排序的方式; reverse=False 默认正序
print(list3)  # [-121, 36, 45, 89, 100]

list3.sort(reverse=True)  # 更改reverse为True, 倒序
print(list3)  # [100, 89, 45, 45, 36, -121]

# 查
# count 查询元素在列表中出现的次数
res = list3.count(45)
print(res)

# index 从左开始查找元素在列表中第一次出现的索引值, 查找不到报错
res1 = list3.index(89)
print(res1)

res2 = list3.index(45)
print(res2)  # 2

res3 = list3.index(1000)  # ValueError: 1000 is not in list
print(res3)

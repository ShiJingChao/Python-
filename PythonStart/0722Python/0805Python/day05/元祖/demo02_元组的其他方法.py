"""
    元组的其他方法:
        删: 只能删除整个元组, 不能单独删除元组中的个别元素;
            del 元组
        查:
            index() 查找指定元素在元组中的索引值 start 取的到, end 取不到
            count() 计算指定元素在元组中出现的次数
"""
t1 = ('罗贯中', '施耐庵', '曹雪芹', '吴承恩', '吴承恩')

# index() 查找指定元素在元组中的索引值
# start 取的到, end 取不到
print(t1.index('施耐庵', 0, 3))
# print(t1.index('吴承恩', 0, 3))  # ValueError: tuple.index(x): x not in tuple

# count() 计算指定元素在元组中出现的次数
print(t1.count('吴承恩'))  # 2

# tuple()
list1 = ['a', 'b', 'c']

t2 = tuple(list1)
print(t2)  # ('a', 'b', 'c')

print(dir(tuple))




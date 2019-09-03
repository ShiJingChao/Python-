"""
    列表的嵌套
    list1 = [['a', 'b'], ['abc', 100], 'abc', 100, [0.9, 0.7]]
"""
list1 = [
    ['a', 'b'],
    ['abc', 100],
    [0.9, 0.7]
]
# 循环遍历出列表的每一个元素:
for x in list1:
    for y in x:
        print(y)

# isinstance(对象, 类型)  判断元素对象是否是某个类型的
print(' ----------------------------- ')
print(isinstance('abc', str))   # True
print(isinstance(100, float))  # False


list2 = [['a', 'b'], ['abc', 100], "abc", 100, [0.9, 0.7]]
for x in list2:
    if isinstance(x, list):  # x 是列表:
        for y in x:
            print(y)
    else:
        print(x)

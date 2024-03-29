"""
    number str list
    列表: python内置的基础数据类型
        容器;用于存储一组数据的有序序列;

        语法声明:
            [元素1, 元素2, 元素3, ...]

        特点:
            1. 列表是有序的;
            2. 列表中可以存储重复的数据;
            3. 列表中可以存储不同数据类型的数据;
            4. 列表是一个可变的数据类型;可以修改的;

        索引:
            下标;
            从左到右,0,1,2,...
            从右到左,-1,-2,...
            格式:
                列表名[索引值]

"""

list1 = ['杨紫', '罗云熙', '张晨', '郭阳', '郭阳']
print(list1)

list2 = ["郭阳", 22, '男', 100.0, True]
print(list2)  # ['郭阳', 22, '男', 100.0, True]
print(type(list2))  # <class 'list'>

print(list1[3])
print(list1[-1])

list1[-1] = '老韩'
print(list1)  # ['杨紫', '罗云熙', '张晨', '郭阳', '老韩']


"""
    集合: set
        python的基础数据类型之一;
        定义: 用于存储一组无序的不重复的数据;

        特点:
            1. 集合是无序的;
            2. 集合中的元素是不重复的, 唯一的;
            3. 集合中存储的数据必须是不可变的数据类型;
            4. 集合是可变的数据类型;

        语法:
            set1 = {1, 2, 3}  # int --> 不可变

        增加:
            add()
            update()  参数: 可迭代对象(容器)
                            将可迭代对象中和集合中不重复的元素添加到集合中
        删除:
            pop() 随机删除某个元素
            remove() 删除指定的元素
            clear() 清空集合
            del 集合名 删除整个集合

        集合的遍历: for in
"""
set1 = {1, 2, 3}
print(set1)
print(type(set1))  # <class 'set'>

# set2 = {}
# print(type(set2))   # <class 'dict'>
# 创建一个空集合变量
set2 = set({})
print(set2)
print(type(set2))  # <class 'set'>

list1 = [1, 2, 2, 3, 1]
# 给这个列表去除重复
set3 = set(list1)
print(set3)  # {1, 2, 3}

# 集合中存储的是不可变的数据类型
# set4 = {"abc", 0.2, [1, 2, 3]}
# print(set4)  # TypeError: unhashable type: 'list'

# 添加操作 add
set5 = {1, 2, 3}
set5.add(4)
print(set5)  # {1, 2, 3, 4}

# update()
set5.update({5, 6, 7, 8})
print(set5)  # {1, 2, 3, 4, 5, 6, 7, 8}

set5.update({1, 2, 3, 100})
print(set5)  # {1, 2, 3, 4, 5, 6, 7, 8, 100}

set5.pop()  # 随机删除一个数据
print(set5)

set5.remove(100)  # 删除指定元素
print(set5)  # {2, 3, 4, 5, 6, 7, 8}

set5.clear()
print(set5)  # set()

del set5
# print(set5)  # NameError: name 'set5' is not defined



"""
    3. 集合推导式:
        集合推导式和列表推导式很相似, 唯一的区别就是用{}代替[]

        语法结构:
            1. set = {表达式 for item in 容器}
            2. set = {表达式 for item in 容器 if 条件}
            3. set = {表达式 for item1 in 容器1 for item2 in 容器2}

        特点: 自动去重功能
"""
list1 = [9, 8, 7, -2, 2, -3, -7, 9]
# 使用集合推导式 推导出一个集合 集合中的元素是list1中元素的平方
set1 = {x ** 2 for x in list1}
print(set1)  # {64, 4, 9, 81, 49}




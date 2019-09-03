# 4 分析以下需求，并用代码实现：
# (1)生成10个1至100之间的随机整数(不能重复)，存入一个List集合
# (2)编写方法对List集合进行排序
# (3)然后利用迭代器遍历集合元素并输出
# (4)如：15 18 20 40 46 60 65 70 75 91
import random


def sort_list(list):
    b = [i for i in list]
    for i in range(1, len(b)):
        for j in range(0, len(b) - 1):
            if b[j] > b[i]:
                b[j], b[i] = b[i], b[j]
    return b


list = set()
for i in range(10):
    list.add(random.randint(1, 100))
print(list)
for i in sort_list(list):
    print(i, end="\t")

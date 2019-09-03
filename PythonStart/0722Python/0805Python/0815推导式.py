list = [j * i for i in range(1, 10) for j in range(1, i + 1)]
print(list)

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [j for i in list1 for j in i]
print(list2)

list3 = [i[0] for i in list1]
print(list3)
list4 = [list1[i][i] for i in range(0, len(list1))]
print(list4)

dict = {"name": "rose", "age": 17, "sex": "女"}
dict1 = {k: v for k in dict.values() for v in dict.keys()}
print(dict1)
list5 = ["施耐庵", "吴承恩", "曹雪芹", "罗贯中"]
list6 = ["水浒传", "西游记", "红楼梦", "三国演义"]
dict2 = {list5[i]:list6[i] for i in range(len(list6))}
print(dict2)
dict3 = {i:k for i,k in zip(list5,list6)}
print(dict3)

from random import randint
a=randint(1,10)
print(a)


g_num =100
g_list = []

def get_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum






# 列表推导式

# 1.创建一个函数，输入一个大于1的整数，返回一个列表，
# 包含所有能够整除该整数的因子（不包含1和它本身），并且从小到大排序。
# 如果这个数是素数，则返回“(integer) is prime”。
#   (1)使用普通函数
#   (2)使用列表推导式

# def num(n):
#     for i in range(2,n//2+1):
#         if n % i == 0:
#             list1 = [i for i in range(2, n // 2 + 1) if n % i == 0]
#             return list1
#     else:
#         return "%d is prime" % n
#
# print(num(10))

def fun(num):
    res1 = [i for i in range(2,num) if num % 2 == 0]
    return res1 if res1 else "%d is prime" % num

# 2.现在有一列表lst = [[1,2,3],[4,5,6],[7,8,9]]
# 要求使用列表推导式取出 1、4、7  和 1、5、9 元素，思考如何取出
# lst = [[1,2,3],[4,5,6],[7,8,9]]
# list1 = [i[0] for i in lst]
# list2 = [lst[i][i] for i in range(len(lst))]
# print(list1)
# print(list2)

# 1.创建一个列表，长度为10。数据是1-100的随机数。
from random import randint
# list = [randint(1,100) for i in range(10)]
# print(list)

# 2.创建一个列表，长度为10。数据是1-100内的随机偶数。
# list1 = [randint(2,101,2) for i in range(10)]
# print(list1)

# 3.打印当前的日期
import time

t=time.localtime()

# 4.打印当前的日期，按照指定的格式：
# 	格式:2017-11-27
# 	格式:2017-11-27 16:33:44
# 	格式:20:33:44
t1 = time.strftime("%Y-%m-%d",t)
t3 = time.strftime('%Y-%m-%d %H:%M:%S',t)
t4 = time.strftime('%H:%M:%S',t)
print(t1)
print(t3)
print(format(t4))

# 5.让当前的程序睡眠5秒钟，再运行后面的代码
# print("123")
# time.sleep(5)
# print("234")
# 6.拼接一个字符串，长度为4。其实就是随机生成验证码内容是26个小写字母和26个大写字母。以及0-9数字。
import random
strr = ""
for i in range(4):
    b = randint(0, 6)
    if b<=2:
        a = str(random.randint(0,9))
        strr+=a
    elif 2<b<=4:
        c = chr(random.randint(65,90))
        strr+=c
    elif 4<b<=6:
        d = chr(random.randint(97,122))
        strr+=d
print(strr)
#
# 7.创建一个列表，长度为10，数据是1-10的随机数。要求去重复。
set = {randint(1,10) for i in range(1,10)}
list1 = list(set)
print(list1)
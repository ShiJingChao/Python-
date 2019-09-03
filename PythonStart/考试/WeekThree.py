# #1. 这个程序的输出顺序是什么？
# def outter1(f):
#     def inner1():
#         print('--before inner1--')
#         f()
#         print('after inner1')
#     return inner1
# def outter2(f):
#     def inner2():
#         print('--before inner2--')
#         f()
#         print('after inner2')
#     return inner2
# @outter2
# @outter1
# def func():
#     print('--func--')
# func()

# --before inner2--
# --before inner1--
# --func--
# after inner1
# after inner2

# 2.py文件中只有如下代码,执行结束后的结果是：

# class Person:
#     def __init__(self):
#         print('--init--')
#     def __str__(self):
#         return '--str--'
#     def __del__(self):
#         print('--del--')
# def func():
#     per = Person()
#     print(per)
# func()
# print('--finish--')

# --init--
# --str--
# --del--
# --finish--

# def funA(desA):
#     print("It's funA")
#
#     print('---')
#     print(desA)
#     desA()
#     print('---')
#
#
# def funB(desB):
#     print("It's funB")
#
#
# @funB
# @funA
# def funC():
#     print("It's funC")

# 三、编程题：（总分7*8=56分）
# 1. 存在列表 a = [11, 22, 33], 如何向列表中添加（增）新元素 44？
# a = [11, 22, 33]
# a.append(44)
# print(a)
# 如何删除（删）列表中的元素 33？如何修改（改）列表中的元素 22 为 55？
# del a[2]
# print(a)
# 或者
# a.remove(33)
# print(a)
# a[1] = 55
# print(a)
# 2.使用列表推导式实现一个包含1-100包含100所有3的倍数的元素的列表？
# list = [i for i in range(1,101) if i %3 == 0]
# print(list)

# 3.已有列表 nums = [11, 22,11,33,11,44, 55,11],将列表中的11全部改为10？
# nums = [11, 22, 11, 33, 11, 44, 55, 11]
# for i in range(0, len(nums)):
#     if nums[i] == 11:
#         nums[i] = 10
# print(nums)
# 4.已有列表 nums = [11, 22,11,33,11,44, 55,11,11],将列表中的11全部删除？
# nums = [11, 22,11,33,11,44, 55,11,11]
# for i in nums:
#     if i == 11:
#         nums.remove(i)
# print(nums)
# 5.存在字典 info = {'name':'张三'},删除整个字典，如何清空整个字典？
# 删除整个字典：del info
# 清空整个字典：info.clear()
# 6.求300到320之间能被7或者9整除的数的个数

# count = 0
# for i in range(300, 320):
#     if i % 7 == 0 or i % 9 == 0:
#         count += 1
# print(count)

# 7. 输入一个年份，输出是否为闰年

# year = int(input("请输入年份："))
# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print("闰年")
# else:
#     print("平年")
#
# 四、实践题：（总分28分）
# 8.（总分12分）
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
# def func(n):
#     if n == 1 or n == 2:
#         return n
#     else:
#         return func(n - 1) + func(n - 2)


# print(func(5))

# 9.（总分16分）
# 会文数是指正读倒读都一样的整数 ，例如121,1221等，请设计程序，找出10000以内的回文素数（指既是回文数，又是素数）

# def fun1(i):
#     for j in range(2, i):
#         if i % j == 0:
#             return False
#     else:
#         return True
#
#
# def fun2(num):
#     if str(num) == str(num)[::-1]:
#         return True
#
#
# for i in range(2, 10001):
#     if fun1(i) and fun2(i):
#         print(i, end=" ")

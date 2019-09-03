"""
    __call__():
            功能: 让类的实例,具有类似有函数(方法)的功能; 让对象可以被调用, 调用时执行的就是__call__中的函数体;
            触发时机: 调用对象的时候;  对象()
"""


# class Person:
#     def __init__(self, name, sex, age, wife=None, husband=None):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.wife = wife
#         self.husband = husband
#
#     def __call__(self):  # 获取....
#         if self.sex == "男":
#             print(self.wife)
#         else:
#             print(self.husband)
#
#     def get_age(self):
#         print(self.age)
#
#
# p1 = Person("小二黑", "男", 18, "妻子")
# print(p1.name)
# p1.get_age()
# print("---------------------------------")
# p1()

# 定义一个类,使用call方法计算斐波那契数列的第n个元素的值;
# 1. 使用递归
class Feibo:
    # 1,1,2,3,5,8,13,21,...
    def __call__(self, n):  # 自己,本身,当前实例对象
        if n == 1 or n == 2:
            return 1
        else:
            return self(n-1) + self(n-2)


f = Feibo()
print(f(5))  # 调用当前对象
print(f(6))
print(f(7))
print(f(8))

# 2. 使用普通函数
# class FeiboTwo:
#     # 1,1,2,3,5,8,13,21,...
#     def __call__(self, n):
#         first = 1   # 第一个数字
#         second = 1  # 第二个数字
#         if n == 1 or n == 2:
#             return 1
#         for x in range(n-2):  # range(n), 循环遍历n次  n=4
#             # 第3, 4, 5, 6, ...n个数的值;
#             first, second = second, first + second
#             # 前1个数: second + first
#             # 前2个数: second
#         return second
#
#
# f2 = FeiboTwo()
# print(f2(5))
# print(f2(6))
# print(f2(7))
# print(f2(8))
#
#
# class FeiboThree:
#     def __call__(self, n):  # 前n个数字组成的斐波那契数列
#         a = 1  # 前2个数
#         b = 1  # 前1个数
#         lst = [1, 1]
#         if n == 1:
#             return [1, ]
#         elif n == 2:
#             return [1, 1]
#
#         for x in range(n-2):  # 循环的次数 range(1) = range(0, 1)
#             a, b = b, a + b
#             lst.append(b)
#
#         return lst
#
#
# f3 = FeiboThree()
# print(f3(3))
# print(f3(8))
#
#
#


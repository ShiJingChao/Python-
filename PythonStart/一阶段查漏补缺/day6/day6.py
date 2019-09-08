# class Student:
#     def __init__(self,name,age,chinese,math,english):
#         self.name = name
#         self.age = age
#         self.chinese = chinese
#         self.math = math
#         self.english = english
#     def get_name(self):
#         print(self.name)
#     def get_age(self):
#         return "{}的年龄：{}".format(self.name,self.age)
#     def get_course(self):
#         return max(self.chinese,self.math,self.english)
#
# s = Student("尿尿",1,89,100,85)
#
# s.get_name()
# print(s.get_age())
# print(s.get_course())
#
# class DictClass:
#     def __init__(self,dict1):
#         self.dict1 = dict1
#     def del_dict(self,k):
#         return "删除的是：%s"%self.dict1.pop(k)
#     def is_indict(self,n):
#         a = self.dict1.get(n,"not found")
#         return a
#     def lis(self):
#         a = []
#         for i in self.dict1.keys():
#             a.append(i)
#         return a
#     def update_dict(self):
#         b = []
#         for i in self.dict1.values():
#             b.append(i)
#         return b
# dd = {1:2,2:3,4:5,6:7}
# d = DictClass(dd)
# print(d.del_dict(1))
# print(d.is_indict(4))
# print(d.lis())
# print(d.update_dict())


# 装饰器
# def outer(f):
#     def inner(x,y):
#         return x+y
#     return inner
# @outer
# def func(x,y):
#     return 1
# print(func(3,4))



# 创建10个文件夹，每个文件夹下包含一个同名的文件
import os
for i in range(1,11):
    path = os.chdir("D:/")
    os.mkdir(str(i))
    with open('{}\{}.txt'.format(str(i), str(i)),'w'):
        pass



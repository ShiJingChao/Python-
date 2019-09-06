# D

# class Instrument:
#     def makesound(self,instrument = None):
#         print("可以发出声音")
#
# class Erhu(Instrument):
#     def makesound(self):
#         super().makesound()
#         print("可以发出二胡声")
# class Piano(Instrument):
#     def makesound(self):
#         print("可以发出钢琴声")
# class Violin(Instrument):
#     def makesound(self):
#         print("可以发出小提琴声")
#
# class Bandsman:
#     def play(self,instrument):
#         instrument.makesound()
# ehu = "二胡"
# p = "钢琴"
# v = "小提琴"
#
#
# b = Bandsman()
# b.play(Erhu())
# b.play(Piano())
# b.play(Violin())

# i.makesound(piano(p))
# i.makesound(violin(v))


# import random
# class Lottery:
#     def buy(self):
#         s = []
#         z_s = []
#         for i in range(7):
#             a = random.randint(1,33)
#             s.append(a)
#         for i in s:
#             print("您的彩票号码为：",i,end=" ")
#     def xitong(self):


# 多继承

# class Gongren:
#     def laodong(self):
#         print("出体力劳动")
# class Manong:
#     def laodong1(self):
#         print("灵活劳动")
#
# class Xuetu(Gongren,Manong):
#     def laodong(self):
#         super().laodong()
#         super().laodong1()
#         print("1")
# p = Xuetu()
# p.laodong()
# print(Xuetu.__mro__)



# 抽象类
# 抽象方法不能被实例化
# 只能被继承，且子类必须实现抽象方法
# import abc
# class Person(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def eat(self):
#         pass
#     @abc.abstractmethod
#     def sleep(self):
#         pass
#     def breathe(self):
#         print("呼吸空气")
#
# class Student(Person):
#     def eat(self):
#         pass
#     def sleep(self):
#         print("睡学校")
#
# class Boss(Person):
#     def eat(self):
#         print("下饭店")
#     def sleep(self):
#         print("睡宾馆")
#
# stu = Student()
# stu.eat()
# stu.sleep()
# stu.breathe()
# bos = Boss()
# bos.eat()
# bos.sleep()
# bos.breathe()


# 抽象类

# import abc
# # class mather(metaclass = abc.ABCMeta):
# #     @abc.abstractmethod
# #     def study(self):
# #         pass
# #     @abc.abstractmethod
# #     def play(self):
# #         pass
# #     def flawer(self):
# #         print("妈妈喜欢养花")
# #     def drink(self):
# #         print("妈妈喜欢喝茶")
# # class child(mather):
# #     def study(self):
# #         print("妈妈让我学习")
# #     def play(self):
# #         print("妈妈让我锻炼")
# # n = child()
# # n.study()
# # n.play()
# # n.flawer()
# # n.drink()


# import abc
# class DaShuai(metaclass=abc.ABCMeta):
#     def __init__(self):
#         self.name = "南派大帅"
#         self.gender = "男"
#         self.character = "强迫症晚期患者"
#     @abc.abstractmethod
#     def kongfu(self):
#         pass

# class Luo():
#     def __init__(self):
#         self.name = "罗大师"
#         self.gender = "女"
#         self.character = "开朗"
#     def kongfu1(self):
#         print("碧血剑法")
#
# class LaoHu(DaShuai,Luo):
#     def kongfu(self):
#         print("学习天马流星拳")
#     def kongfu1(self):
#         super().kongfu1()
# l = LaoHu()
# l.kongfu()
# l.kongfu1()



# __new__方法

# class Dog:
#     def __new__(cls, *args, **kwargs):
#         print("______new_______")
#         new__ = object.__new__(cls)
#         return new__
# dog1 = Dog()
# print(dog1)



# 生成器

# g = (i for i in range(10))
# print(g)
# for j in g:
#     print(j)

#
# def FeiBo(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return FeiBo(n-1)+FeiBo(n-2)
#
# f = FeiBo(5)
# print(f)
#
# import random
# while True:
#     a = random.randint(0,10)
#     if a %2 == 0:
#         print(a)
#         break
#     else:
#         continue



# def num(a,*args):
#     print(a,args)
#
# a = num(1,(2,3,5))


# class Computer:
#     __name = "wo"
#     __shuxinghao = "2132131"
#     def __id(self):
#         print("1234")
#     def __m(self):
#         print("123")
#     def kaiji(self):
#         self.__id()
#         self.__m()
#     def yunxing(self):
#         print("yunxing")
# #
# #
# c = Computer()
# c.kaiji()
# c.yunxing()
#
#
# g = (i for i in range(10))
# print(g)
# for j in g:
#     print(j)

# import sys
# print(sys.version)
# print(sys.path)
# print(sys.argv)
#
# a = 5
# def outer():
#     def inner(n):
#         print("1234")
#         f()
#         print("2222")
#     return inner
# @outer
# f()




# def jiecheng(m):
#     if m == 1:
#         return 1
#     else:
#         return jiecheng(m-1)*m
#
# j = jiecheng(10)
# print(j)

#
class Person():
    def __init__(self, name, gender, age):  # 魔术方法，对象初始化，在实例化的时候调用
        self.name = name
        self.gender = gender
        self.age = age

    @classmethod
    def cla(cls):  # 类方法，第一个参数为类本身，调用方式为实例调用或者类调用
        print("我是类方法")

    @staticmethod
    def infomation(cls):  # 静态方法，没有参数，调用方法为实例调用或者类调用
        print("姓名：{} 性别：{}，年龄：{}".format(cls.name, cls.gender, cls.age))

    def __str__(self):
        s = "我相当于说明书"
        return s
    def say(self):  # 实例方法，第一个参数为调用处，只能由实例对象调用
        print("说话")


p = Person("尿尿","母","3")
p.cla()
p.say()
p.infomation(p)
print(p)



# class Person():
#     def __new__(cls, *args, **kwargs):
#         print("__new__")
#         return object.__new__(cls)
#
#     def __init__(self):
#         print("__init__")
#
#     def __del__(self):
#         print("__del__")
# p=Person()
# print("--finish")



# class Person():
#     def __new__(cls, *args, **kwargs):
#         print("__new__")
#         return object.__new__(cls)
#
#     def __init__(self):
#         print("__init__")
#
#     def __del__(self):
#         print("__del__")
# def func():
#     p=Person()
# func()
# print("--finish")



# class Person():
#     def __new__(cls, *args, **kwargs):
#         print("__new__")
#
#     def __init__(self):
#         print("__init__")
#
#     def __del__(self):
#         print("__del__")
# def func():
#     p=Person()
# func()
# print("--finish--")



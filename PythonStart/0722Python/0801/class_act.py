# class Demo(object):
#     _x = 10
#
# a = Demo()
# print(a._x)


# 多继承

# class A(object):
#     __x = 1
#
#     def test1(self):
#         print('-----------test1')
# class B(object):
#     __x = 100
#
#     def test2(self):
#         print('--------------B test2')
# class C(B, A):
#     pass
#
#
# c = C()
# print(c.__dir__())
# print(c._A__x)
# print(c._B__x)


# class A(object):
#     def func(self):
#         print('-----------A')
# class B(A):
#     # pass
#     def func(self):
#         super().func()
#         print('--------------B ')
# class C(A):
#     # pass
#     def func(self):
#         super().func()
#         print('cccccc')
# class D(B,C):
#     def func(self):
#         super().func()
#         print('-----D-------')
#
# d = D()
# d.func()

class Car(object):
    def __init__(self, engine, brand, texture, torsion):
        self.engine = engine
        self.brand = brand
        self.texture = texture
        self.torsion = torsion
    def run(self):
        print("")

class Kache(Car):
    def engine(self):
        print("卡车的发动机是%s" % self.engine())


class Taxi(Car):
    def texture(self):
        print("轿车的材质是%s" % self.texture())


c = Kache("4缸", "大众", "塑料", "200扭")
c.engine()
c.texture()
d = Taxi()


# 多态

# class Pay(object):
#     def pay(self, money):
#         pass
#
#
# class Alipay(Pay):
#     '''支付宝支付'''
#
#     def pay(self, money):
#         print('支付宝支付了%s元' % money)
#
#
# class Applepay(Pay):
#     '''apple pay支付'''
#
#     def pay(self, money):
#         print('apple pay支付了%s元' % money)
#
#
# class Person(object):
#     # 消费
#     def consumption(self, pay, money):
#         pay.pay(money)
#         # print("使用%s消费了%d元"%(pay,money))
#
#
# alipay = Alipay()
# apply_pay = Applepay()
# person = Person()
# # 使用支付宝支付
# person.consumption(alipay, 100)
# person.consumption(apply_pay, 200)

# import abc
#
#
# class Person(metaclass=abc.ABCMeta):
#     @abc.abstractclassmethod
#     def eat(self): pass
#
#     @abc.abstractclassmethod
#     def sleep(self): pass
#
#     def breathe(self):
#         print('呼吸空气')
#
#
# class Student(Person):
#     def eat(self):
#         print('吃食堂')
#
#     def sleep(self):
#         print('睡学校')
#
#
# class BOSS(Person):
#     def eat(self):
#         print('下饭店')
#
#     def sleep(self):
#         print('睡宾馆')


# 0.抽象类不能实例化
# per=Persion
#
# # 1.不实现抽象方法会执行的时候会报错
# student = Student()
# student.eat()
# student.sleep()
#
# 2.实现抽象方法
# student = Student()
# student.eat()
# student.sleep()
# student.breathe()
# boss = BOSS()
# boss.eat()
# boss.sleep()
# student.breathe()


# 抽象练习
# 一个父亲
# import abc
#
#
# class Wulingaoshou(metaclass=abc.ABCMeta):
#
#     @abc.abstractclassmethod
#
#     def ti(self):
#         pass
#
#     @abc.abstractclassmethod
#
#     def da(self):
#         pass
#
#     def wugong(self):
#         print("龟派气波")
#
#
# class Jia(Wulingaoshou):
#     def ti(self):
#         print("佛山无影脚")
#
#     def da(self):
#         print("无影指")
#
#
# class Yi(Wulingaoshou):
#     def ti(self):
#         print("军体拳")
#
#     def da(self):
#         print("十八罗汉")
#
#
# jia = Jia()
# jia.da()
# jia.ti()
# jia.wugong()
# yi = Yi()
# yi.da()
# yi.wugong()


# from abc import ABCMeta,abstractmethod
#
# class File(metaclass=ABCMeta):
#     @abstractmethod
#     def read(self):pass
#     @abstractmethod
#     def write(self):pass
#     class Word(File):
#         def read(self):
#             print("优雅的读")
#         def write(self):
#             print("优雅的写")
#     class Txt(File):
#         def read(self):
#             print("粗暴的读")
#         def write(self):
#             print("粗暴的写")

from abc import ABCMeta,abstractmethod
class File(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def write(self):
        pass
class Word(File):
    def read(self):
        print("优雅的读")
    def write(self):
        print("优雅的写")
class Txt(File):
    def read(self):
        print("暴躁的读")
    def write(self):
        print("暴躁的写")


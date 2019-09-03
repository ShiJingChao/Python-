# 如果子类是pass 会继承父类，子类有值得话，就不会继承父类
# class Parent(object):
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)
#
# class Person(object):
#     def __init__(self, name, age):  # 请同学们附加参数
#         self.name = name
#         self.age = age
#
#     def play(self):
#         print("player")
# # 实例
# p1 = Person('fwz')
# p1.play()
# p1.play()
# p1.play()
#
#
# class M():
#     x =1
#     def play(self):
#         print('player')
#
# m1 = M()
# m1.x = 2
# m1.play()


# 二 访问权限
# 1.公有成员
# def play(self):    特征： 类内 类外 都可以访问
# x = 1                       类内类外 都可以访问，可以赋值
# 2.私有成员
# __开头的成员     例：def _play(self):
# _x = ?
# 特征 仅提供 类内访问
# *合理的私有  叫做 封装
# class P():
#     def _a(self):
#         pass
#     def _b(self):
#         pass
#     def c(self):
#         self.a()
#         self.b()
#
# p1 = P()
# p1.c()


# 练习  车
# 车的logo 性能 时速 全部设置为私有属性
# 为车设置drive驾驶的方法

# class peo:
#     def __logo__(self,name,age,sex):
#         self.name = name
#         self.age  = age
#         self.sex = sex
#     def speak(self):
#         print("my name"+self.name)
#         print("劳斯莱斯")
#     def __xingneng__(self):
#         print("极好")
#     def speed():
#         print("280码")
#     def __str__(self):
#         msg='my name is:'+self.name+","+"my age is"+self.age +","+"my sex is:"+self.sex
#         return msg
# shanghai=peo('asddsa','','')
# p = peo()
# p._logo('驾驶')


# class peo:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         print(name, age, sex)
#
#     def speak(self):
#         print("my name" + self.name)
#
#     def __str__(self):
#         msg = 'my name is:' + self.name + "," + "my age is" + self.age + "," + "my sex is:" + self.sex
#         return msg
#
#
# shanghai = peo('shanghai', '23', 'man')
# shanghai.speak()

# class Person(object):
#     def __init__(self, name):
#         self.__name = name
#     def get_name(self):
#         return self.__name
#     def set_name(self,new_name):
#         if len(new_name) >= 5:
#             self.__name = new_name
#         else:
#             print("error:名字长度需要大于或者等于5")
#
# p = Person("afu")
#
# p.set_name("wanger")
# print(p.get_name())
#
# p.set_name("lisi")
# print(p.get_name())
list=[1,2,3]
print(list*3)

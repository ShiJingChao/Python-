# 类：用来描述具有相同的属性和方法的对象的集合，
# 它定义了该集合中每个对象所共有的属性和方法，对象是类的实例


# class Persion(object):
#     nick = 'limiao'
#
#     def run(self):
#         print("你会走路？")
#
#     def song(self):
#         print("你只会爬")


# a = Persion()
# a.run()
# a.song()


# 类 定义
# 定义类的语法规则：
# class 大驼峰法命名（父类）：
# 属性 = 属性的值

# def 方法名（self）：
#     方法执行的代码
# def 方法名（self）：
#   方法执行的代码
# 例如现在我想定义一个小狗的类

# class Dog(object):
#     type = '犬科'
#
#     def eat(self):
#         print('看门 啃骨头')
#
#     def swim(self):
#         print('狗刨')


# class Dog(object):
#     print("猫")
#     def zhuahaozi(self):
#         print("抓三只耗子")
#     def jiaohuan(self):
#         print('叫三声喵')
# b = Dog()
# b.zhuahaozi()
# b.jiaohuan()

# CLASS 361 面向对象——01基本概念
# 面向过程和面向对象基本概念
# 面向过程
#   1.把完成某一个需求的 所有步骤 从头到尾 逐步实现
#   2.根据开发需求，将某些功能独立的代码 封装成一个又一个的函数
#   3.最后完成的代码，就是顺序的调用不同的函数
# 特点：
#   1.注重步骤与过程，不注重职责分工
#   2.如果需求复杂，代码会变得很复杂
#   3.开发复杂项目，没有固定的套路，开发难度很大！

# 面向对象
#   相比较函数，面向对象是更大的封装，根据职责在一个对象中封装多个方法
# 1.在完成某一个需求前，首先确定职责——要做的事情（方法）
# 2.根据职责确定不同的对象，在对象内部封装不同的方法（多个）
# 3.最后完成的代码，就是顺序地让不同的对象调用不同的方法

# 特点
# 1.注重对象和职责，不同的对象承担不同的职责
# 2.更加适合应对负责的需求变化，是专门应对复杂项目开发，提供的固定套路
# 3.需要在面向对象基础上，再学习一些面向对象的语法

# Class 362 面向对象——类和对象的基本概念
# 类 是对一群㕛相同特征 或者行为的事物的一个统称，是抽象的，不能直接使用
# 特征被称为属性
# 行为被称为方法

# CLASS 363 面向对象设计类的三要素和名词提炼法
# 设计类，要满足的三个要素：
# 1.类名 这类事物的名字，满足大驼峰命名法（每一个单词的首字母大写，单词之间没有下划线）
# 2.属性 这类事物具有什么样的的特征
# 3.方法 这类事物具有什么样的行为


# CLASS 364 内置的dir函数查询对象的方法列表
# dir内置函数
# 1.在标识符/数据后输入一个.然后按下TAB键，python会提示该对象能够够调用的方法列表
# 2.使用内置函数dir传入标识符/书u，可以查看对象内所有的属性和方法
# print(dir(Persion))

# CLASS 365定义简单类——基本语法
# 和函数基本一样
# 区别在于第一个参数必须是self
# 类名的命名规则要符合大驼峰命名法

# CLASS 366定义简单类——案例演练
# 需求：小猫爱吃鱼，小猫爱喝水
# class Cat:
#     def eat(self):
#         print('%s chiyu'%self.name)
#     def drink(self):
#         print('hehsui')
# tom=Cat()
# tom.name = "小猫"
# tom.eat()
#
# tom.drink()
# print(tom)

# 再创建一个猫对象，和tom的内存地址不同
# lazy_cat = Cat()
# lazy_cat.name = "大懒猫"
# lazy_cat.eat()
# lazy_cat.drink()
# print(lazy_cat)

# CLASS 369在类外部给类增加属性（不推荐使用）
# lazy_cat.name="大懒猫"
# 在类外给类增加属性的隐患 在运行时没有找到属性，程序会报错
# 对象应该包含有哪些属性，应该封装在类的内部


# a, b = 3, 4
#
#
# def fun(x):
#     c, d = 1, 2
#     print(locals())
#
#
# fun(6)
# print(globals())

# CLASS 372初始化方法

# 当使用 类名 创建对象时，会自动执行以下操作：
#     1.为对象在内存中 分配空间——创建对象
#     2.为对象的属性 设置初始值——初始化方法（init）
# 这个初始化方法就是 __init__ 方法，__init__是对象的内置方法
class Cat:
    def __init__(self):
        print("这是一个初始化方法")


# 使用类名（）创建对象的时候，会自动执行以下操作
# 1.为对象在内存中分配空间--创建对象
# 2.为对象的属性设置初始值——初始化方法（init）
# 这个初始化方法就是 __init__方法， init__是对象的内置方法

# __init__方法是专门用来定义一个类 具有哪些属性的方法

# CLASS 373 在初始化方法中定义属性

# 在 __init__方法内部使用self.属性名=属性的初始值 就可以定义属性
# 定义属性之后，再使用Cat类创建的对象，都会拥有该属性
# class Cat:
#     def __init__(self):
#         print("这是一个初始化方法")

# 定义用Cat类创建的猫对象都有一个name的属性
#       self.name = "TOM"
#
# def eat(self):
#     print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法__init___
# tom = Cat()
# print(tom.name)
# tom.eat()


# CLASS 374 使用参数设置属性初始值,初始化的同时设置初始值

# 在开发中，如果希望在创建对象的同时，就设置对象的属性，对__init__方法进行改造
# 1.把希望设置的属性值，定义成__init__方法的函数
# 2.在方法内部使用self.属性 = 形参接收外部传递的参数
# 3.在创建对象时，使用类名（属性1，属性2...）调用

# class Cat:
#     def __init__(self, name):
#         print("初始化方法：%s" % name)
#         self.name = name
#
#
# tom = Cat("Tom")
# lazy_cat = Cat("大懒猫")

# CLASS 375内置方法 del方法和对象的生命周期
# Tom是全局变量，在程序结束的时候系统才回收如果在print("-"*60)上面加上del tom，那么输出我去了就会在分割线上面

# class Cat:
#     def __init__(self, new_name):
#         self.name = new_name
#         print("%s 来了" % self.name)
#
#     def __del__(self):
#         print("%s我去了" % self.name)
#
#
# tom = Cat("Tom")
# print(tom.name)
# # del 关键字可以删除一个对象
# del tom
# print("-" * 60)


# 在Python中
# 当使用 类名（）创建对象时，为对象分配完空间后，自动调用__init__方法
# 当一个对象被内存中销毁前，会自动调用__del__方法
# 应用场景
# __init__改造初始化方法，可以让创建对象更加灵活
# __del__如果希望在对象被销毁前，再做一些事情，可以考虑一下__del__方法
# 一个对象从调用类名（）创建，生命周期开始
# 一个对象的__del__方法一旦被调用，生命周期结束
# 在对象的生命周期内，可以访问对象属性，或者让对象调用方法


# 内置方法str方法定制变量输出信息
# 在Python中，使用print输出对象变量，默认情况下，
# 会输出这个变量引用的对象是由那一个类创建的对象，
# 以及在内存中的地址（十六进制表示）

# 如果在开发汇总，希望使用print输出对象变量时，能够打印自定义的内容，就可以利用__str__这个内置方法了
# 注意：：__str__方法必须返回一个字符串
# class Cat:
#     def __init__(self, new_name):
#         self.name = new_name
#         print("%s来了" % self.name)
#
#     def __del__(self):
#         print("%s去了" % self.name)
#
#     def __str__(self):
#         return "我是小猫：%s" % self.name
#
#
# tom = Cat("Tom")
# print(tom)


# class Restaurant:
#     def __init__(self):
#         self.restaurant_name = "中餐"
#         self.cuisine_type = "西餐"
#     def describe_restaurant(self):
#         print(self.restaurant_name,self.cuisine_type)
#     def open_restaurant(self):
#         print("餐馆正在营业")
# #
# restaurant = Restaurant()
# print(restaurant.restaurant_name,restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# um_str = "0123456789"
# d= um_str[:]
# G = um_str[-1:-3:-1]
# e= um_str[-2:]
# print(e)
# print(G)

a = [lambda x,i=i:x*i for i in range(9)]
print(a[0](3))
print(a[4](3))
print(a[8](3))
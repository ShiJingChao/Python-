# 代码 翻译
# class Student():
#     name = ''
#     age = ''
#     number = 0
#
#     def say(self):  # 加self的都是对象方法
#         print('我叫{}，{}岁，学号{}'.format(self.name, self.age, self.number))
#
#
# zs = Student()  # 实例化一个对象，Student()是类，张三是一个对象
# zs.name = '张三'
# zs.age = 18
# zs.number = 1001
# zs.say()
# ls = Student()
# ls.name = '李四'
# ls.age = 29
# ls.number = 1002
# ls.say()
# 翻译：定义一个学生类，名字，年龄都为空字符串，初始化学号为0，定义一个说的方法，输出。
# 实例化对象，传递参数输出张三的姓名，年龄，学号 输出，再次实例化输出李四的信息

# class Teacher():
#     def __init__(self,name,age,ID):
#         self.name=name
#         self.age=age
#         self.ID=ID
#     def hehe(self):
#         self.shengao=18
# #python中对象的属性不仅可以在类里增加，也可以在类外面增加
# zs=Teacher('张三',18,101)
# print(zs.name,end=' ')
# print(zs.age,end=' ')
# print(zs.ID)
# zs.hehe()
# print(zs.shengao)
#
# ls=Teacher('李四',29,101)
# print(ls.name,end=' ')
# print(ls.age,end=' ')
# print(ls.ID)
# ls.hehe()
# print(ls.shengao)
#
# 翻译： 定义一个teacher类 ，定义一个魔术方法，有三个参数name，age，ID，定义初始操作，定义hehe类，初始化身高为18，
# 实例化，两次输出都会把身高变成18

# class Computer():
#     def __init__(self,cpu,memory,color):
#         self.cpu=cpu
#         self.memory=memory
#         self.color=color
#     def haha(self):
#         print(self.xinghao)
#
# lx=Computer('835',128,'红')
# lx.xinghao='小黑'
# lx.haha()
#
# hp=Computer('834',64,'黑')
# hp.xinghao='小黑'
# hp.haha()
# 翻译：定义一个Computer类 定义了一个魔术方法传递三个参数，定义haha方法，输出self.xinghao参数，
# 实例化，都传参了但是没有输出，只有小黑输出了
#
# class Computer():
#     __slots__ = ('cpu','memory','color','xinghao')#元组，限制对象的属性
#     def __init__(self,cpu,memory,color,):
#         self.cpu=cpu
#         self.memory=memory
#         self.color=color
#
#     def haha(self):
#         print(self.xinghao)
#
# lx=Computer('835',128,'红')
# lx.xinghao='小黑'
# lx.haha()

# 翻译：定义一个Computer类，限制对象的属性，定义魔术方法可以传递三个参数（三个参数必须是元组中所限制的），定义haha输出xinghao
#
# class Computer():
#     name='你好1111'#类属性
#     def __init__(self,cpu,memory,color):#cpu,memory,color是参数
#         self.cpu=cpu#对象属性
#         self.memory=memory
#         self.color=color
#     def haha(self):
#         print(self.xinghao)
#
# lx=Computer('835',128,'红')
# lx.xinghao='小黑'
# lx.haha()
# print(lx.name)
#
# hp=Computer('834',64,'黑')
# print(hp.name)
# print(Computer.name)
#

# 翻译：定义一个Computer类，初始化name为 你好1111
# 定义一个魔术方法 传递三个参数，但是没有输出，输出的姓名都是初始化的你好1111

# class Computer():
#     count=0
#     def __init__(self,cpu,memory,color):
#         self.cpu=cpu
#         self.memory=memory
#         self.color=color
#         Computer.count+=1
#     def haha(self):
#         print(self.xinghao)
#
#
# lx=Computer('835',128,'红')
# print(Computer.count)
#
# hp=Computer('834',64,'黑')
# print(Computer.count)
#
# 定义一个computer类，初始化计数器等于0，定义魔术方法，每调用一次，计数器次数加1，定义haha方法，实例化输出调用的次数
#
# class Computer():
#     count=0
#     def __init__(self,cpu,memory,color):
#         self.cpu=cpu
#         self.memory=memory
#         self.color=color
#         Computer.count+=1
#     def haha(self):
#         print(self.xinghao)
# # #类属性是全局的，对象属性是局部的
# lx=Computer('835',128,'红')
# print(lx.count,'xxxxxxxxxx')
# lx.count=10
# print(lx.count)
# print(Computer.count,'第一个')
#
# hp=Computer('834',64,'黑')
# print(lx.count)
# print(Computer.count,'第二个')
# print(hp.count)
# delattr(lx,'count')
# print(lx.count)

# 翻译：定义一个Computer类，计数器等于0，print(lx.count,'xxxxxxxxxx')计数器加1输出，给计数器赋值为10，输出，初始化，输出，
# 下面的同理

# 2类方法、对象方法（也叫实例方法）和静态方法  翻译
# class Computer():
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Computer.count+=1
#     def haha(self):
#         print(self.name)
#     @classmethod
#     def c123etho(cls):
#         print(cls.count,'xyz12345')
#
# zs=Computer('张三')
# zs.haha()
# Computer.c123etho()
#
# class Computer():
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Computer.count+=1
#     def haha(self):
#         print(self.name)
#     @classmethod
#     def c123etho(cls):
#         print(cls.count,'xyz12345')
#     @staticmethod
#     def cxxx():
#         print('我只是一个普通的方法，跟类对象没关系')

# zs=Computer('张三')
# zs.haha()
# Computer.c123etho()
# Computer.cxxx()

# 翻译：定义一个计数器初始值为0，定义一个魔术方法，调用的时候计数器加1，定义一个haha方法，定义一个静态方法 调用的时候输出count，定义一个这个类特有的方法，

# 定义一个静态方法，静态方法不会改变输出不变。

class Gun:
    def __init__(self, model):
        # 枪的型号
        self.model = model
        self.bullet_count = 0
    def add_bullet(self,count):
        self.bullet_count+=count
    def shoot(self):
        # 判断是否还有子弹
        if self.bullet_count <=0:
            print("没子弹了。。。")
            return

        #发射一颗子弹
        self.bullet_count-=1
        print("%s 发射子弹[%d]..."%(self.model,self.bullet_count))

#创建枪对象
m99 = Gun('M99')
m99.add_bullet(50)
m99.shoot()



# 4.私有化封装：翻译
# class People():
#     def __init__(self, name, __age):
#         self.name = name
#         self.__age = __age
#
#     def say(self):
#         print(self.name, self.__age)
#
#
# zs = People('老郭', 20)
# print(zs.name)
# zs.say()

# 翻译 定义一个Person类，定义魔术方法，可以传递name，__age两个参数
# 类中有两个方法，第二个方法调用第一个方法，函数嵌套，执行say方法的时候，会执行第一个方法，执行完再返回

# 术语
# 创建出来的对象叫做类的实例
# 创建对象的动作叫做实例化
# 对象的属性叫做实例属性
# 对象调用的方法叫做实例方法
# 在程序执行时：
#     1.对象各自拥有自己的实例属性
#     2.调用对象方法，可以通过self.
#     访问自己的属性和调用自己的方法


# class 408——类是一个特殊的对象

# Python中一切皆对象
# class A：定义的类属于类对象
# ob = A() 属于实例对象

# CLASS 409 类属性的定义及使用
# class Tool(object):
# 使用赋值语句定义类属性
# count = 0
#
# def __init__(self, name):
#     self.name = name
#     Tool.count += 1


# 1.创建工具对象
# tool = Tool("刀子")
# 2.输出工具对象的总数
# tool1 = Tool("斧子")
# print(Tool.count)

# CLASS-410类属性-属性查找机制

# 在Python中属性的获取 存在一个 向上查找 机制
# print(tool.count)   #也可以输出 不推荐使用，容易混淆，仅供科普

# Class-411
# 如果使用 对象.类属性= 值赋值语句，只会给对象添加一个属性，而不会影响到类属性的值
# tool1.count = 99
# print(tool1.count)
# print(Tool.count)


# CLASS412——类方法-基本语法

# 语法：
# @classmethod
# def 类方法名(cls):
#    pass
# 类方法需要修饰器@classmethod 来标识，告诉解释器这是一个类方法
# 类方法的第一个参数应该是cls
# 由哪一个类调用的方法，方法内的cls就是哪一个类的引用
# 通过类名.调用类方法，调用方法时，不需要传递cls参数
# 在方法内部——也可以通过cls.访问类的属性，也可以通过cls.调用其他的类方法

class Tool:
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量%d" % cls.count)

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("螺丝刀")
Tool.show_tool_count()


# CLASS——414-静态方法

# 在开发中，如果需要在类中封装一个方法，这个方法：
# 既不需要访问实例属性或者调用实例方法
# 也不需要访问类属性或者调用类方法
# 这个时候，可以把这个方法封装成一个静态方法
# 语法如下
# @staticmethod
# def 静态方法名（）
#       pass
# 静态方法需要用修饰器@staticmethod来标识，告诉解释器这是一个静态方法
# 通过类名.调用静态方法
class Dog:
    # 不访问实例属性/类属性的时候，就可以定义为静态方法
    @staticmethod
    def run():
        print("小狗要跑...")
# 通过类名.调用静态方法——不需要创建对象
Dog.run()
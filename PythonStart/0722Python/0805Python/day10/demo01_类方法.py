"""
    1. 类属性: 归类所有,只有一份,所有对象共享这一份类属性;
    2. 实例属性: 归对象所有,每个对象都有一份,对象之间的实例属性互不影响;

    3. 实例方法:
        第一个参数, 都是self, self 指的是当前调用的对象;
        可以访问:
            self.实例属性
            类名.类属性

    4. 类方法:
        第一个参数, 都是cls, cls 指的是当前的类
        可以访问:
            类名.类属性; cls.类属性;
            ** 默认不能访问实例属性

        语法规则:

            class 类名:
                @classmethod
                def 类方法名(cls, 参数,...):
                    pass

        * 类方法可以由类调用,也可以由实例调用;
        * 类方法中可以通过传递实例作为参数, 从而访问到实例方法和实例属性;

    5. 静态方法:
            如果类中一个方法既不操作类, 也不操作实例, 那么定义为静态方法;
            没有默认的参数;
            语法:
                class 类名:
                    @staticmethod
                    def 静态方法名():
                        pass

            可以由类调用,也可以由实例调用
----------------------------------
[小结]:
    1. 如果需要定义一个方法, 操作实例, ---> 实例方法
    2. 如果需要定义一个方法, 操作类,   ---> 类方法
    3. 如果需要定义一个方法, 既不操作实例也不操作类  ---> 静态方法
"""
class Person:
    country = "中国"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义一个实例方法, self, 访问实例属性, 访问类属性
    def show_info(self):
        print("实例方法:show_info, {}, {}, {}".format(self.name, self.age, self.country))

    # 定义一个类方法, cls当前类, 可以访问类属性, 不能访问实例属性
    @classmethod
    def test(cls):
        print("类方法:test--国籍:{}".format(cls.country))  # Person.country,

    # 定义一个类方法, 传入一个实例作为参数, 函数体中即可操作该实例(属性,方法)
    @classmethod
    def test2(cls, p_obj):
        print("类方法操作实例:test2--{}, {}".format(cls.country, p_obj.name))

    @staticmethod
    def introduce():
        print("我是一个静态方法, 我既不操作类, 也不操作实例")


p1 = Person("罗云熙", 28)
p2 = Person("李现", 27)

p1.show_info()  # 使用对象调用实例方法
Person.show_info(p2)  # 不建议

"""
实例方法:show_info, 罗云熙, 28, 中国
实例方法:show_info, 李现, 27, 中国
"""
Person.test()  # 可以用类调用类方法
p1.test()  # 也可以用实例调用类方法
p2.test()

p1.test2(p1)  # 类方法操作实例:test2--中国, 罗云熙
Person.test2(p2)  # 类方法操作实例:test2--中国, 李现

Person.introduce()  # 我是一个静态方法, 我既不操作类, 也不操作实例
p1.introduce()  # 我是一个静态方法, 我既不操作类, 也不操作实例



"""
    惯性写法:
        父类: __init__(self, 参数1, 参数2,..):
                self.属性1 = 参数1
                self.属性2 = 参数2
                ....
        子类: __init__(self, 参数1, 参数2,....)
                super().__init__(参数1, 参数2,...)
                self.新增属性 = 参数

    * 子类继承父类, 如果子类中没有init方法, 创建子类对象时, 会自动调用父类的init方法;
    * 子类继承父类, 如果子类中有init方法, 创建对象时, 就不会调用父类的init方法了,
            如果需要使用父类的init方法, 则程序员需要手动调用super().__init__(参数1, 参数2,...)

    属性的覆盖: 子类中覆盖父类中的类属性;
    派生属性: 子类中新增的, 父类中没有的属性;
"""
class Father:
    country = "中华民国"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_me(self):
        print("我是{}, 我的年龄{}".format(self.name, self.age))


class Son(Father):
    country = "中华人名共和国"  # 属性的覆盖
    def __init__(self, sex, name, age):
        super().__init__(name, age)
        self.sex = sex   # 派生属性


s = Son("男", "史狗蛋", 17)
s.show_me()  # AttributeError: 'Son' object has no attribute 'name'
# 我是史狗蛋, 我的年龄17



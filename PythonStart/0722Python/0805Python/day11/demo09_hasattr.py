"""
    hasattr():
        功能: 检测是否具有某个类方法, 类属性, 实例属性, 实例方法
        返回值: bool值

        hasattr(对象, 实例属性/实例方法)
        hasattr(类, 类属性/类方法)
"""


class Person:
    country = "中国"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("我的姓名: %s, 年龄: %d" % (self.name, self.age))

    @classmethod
    def show_country(cls):
        print(cls.country)


p1 = Person("似鸟龙", 200)

print(hasattr(p1, "name"))  # True
print(hasattr(p1, "show_info"))  # True
print(hasattr(p1, "get_num"))  # False

print(hasattr(Person, "country"))  # True
print(hasattr(Person, "show_country"))  # True



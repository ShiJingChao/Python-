"""
    delattr():
        功能: 删除对象/类的属性
        返回值: 无

        delattr(对象, 属性名)
        delattr(类, 属性名)

        要删除的属性不存在, 报错AttributeError: color
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


p1 = Person("腕龙", 900)

delattr(p1, "age")
# print(p1.age)  # AttributeError: 'Person' object has no attribute 'age'

delattr(Person, "country")
# print(Person.country)  # AttributeError: type object 'Person' has no attribute 'country'
# print(p1.country)  # AttributeError: 'Person' object has no attribute 'country'

delattr(p1, "color")  # AttributeError: color




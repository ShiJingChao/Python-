"""
    反射方法:
        getattr()
            功能: 获取实例的属性值或者方法地址
            返回值: 属性的值/方法的地址

        getattr(对象, 属性名/方法名)
        getattr(类, 属性名/方法名)
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


p1 = Person("慈母龙", 100)

name = getattr(p1, "name")
print(name)  # 慈母龙

show_info = getattr(p1, "show_info")
print(show_info)  # <bound method Person.show_info of <__main__.Person object at 0x0000000001E798C8>>

show_info()  # 方法调用   我的姓名: 慈母龙, 年龄: 100

print(getattr(Person, "country"))  # 中国

show_country = getattr(Person, "show_country")
print(show_country)  # <bound method Person.show_country of <class '__main__.Person'>>
show_country()

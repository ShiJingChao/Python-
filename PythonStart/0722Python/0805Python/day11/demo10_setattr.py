"""
    setattr():
        功能: 设置实例/类的属性值
        返回值: 无

        setattr(对象, 属性名, 属性值)
        setattr(类, 属性名, 属性值)

        如果属性已存在, 重新赋值;
        如果属性不存在, 添加属性并赋值;
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


p1 = Person("似鸡龙", 400)

setattr(p1, "age", 500)
print(p1.age)  # 500

setattr(p1, "friend", "似鸟龙")
print(p1.friend)  # 似鸟龙

setattr(Person, "country", "中华人民共和国")
print(Person.country)  # 中华人民共和国

setattr(Person, "color", "黄种人")
print(Person.color)  # 黄种人
print(p1.color)  # 黄种人




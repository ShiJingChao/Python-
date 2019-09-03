"""
    实例属性:
            实例变量(对象属性, 对象变量)
            实例属性归实例(对象)所有; 每个实例(对象)都有一份, 各个实例(对象)之间互不影响;

            self.实例属性

    类属性:
            类属性归类所有, 只有一份, 所有实例可以共享这一份类属性;
            类属性不!能!用self调用;

            语法:
                class 类名:
                    类属性 = 值
                    def 方法名():
                        pass

        1. 如果类属性为可变数据类型, 类和实例均可修改类属性的值;
        2. 如果类属性为不可变数据类型, 只有类可以修改类属性的值;
                如果使用实例修改不可变数据类型的类属性, 实际上相当于给实例添加了一个同名的实例属性;
"""


class Person:
    country = "中国"
    technology = ["石器", "冷兵器"]
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


p1 = Person("小黄", 22, "男")
p2 = Person("子建", 22, "女")

print(Person.country)  # 类名可以访问类属性
print(p1.country)  # 中国
print(p2.country)  # 中国

# 使用类更改类属性(不可变数据类型)
Person.country = "中华人民共和国"
print(p1.country) # 中华人民共和国
print(p2.country) # 中华人民共和国

# 使用实例不!可!以!修改类属性(不可变数据类型)
p1.country = "China"  # 给p1增加一个同名的实例属性
print(Person.country)  # 中华人民共和国
print(p2.country)  # 中华人民共和国
print(p1.country)  # 访问的是p1的实例属性

print("------------------------------")
# 使用类修改类属性(可变数据类型)
Person.technology.append("热兵器")   # ["石器", "冷兵器"]
print(Person.technology)  # ['石器', '冷兵器', '热兵器']
print(p1.technology)  # ['石器', '冷兵器', '热兵器']
print(p2.technology)  # ['石器', '冷兵器', '热兵器']

# 使用实例可!以!修改类属性(可变数据类型)
p1.technology.pop()  # ['石器', '冷兵器', '热兵器']
print(Person.technology)  # ['石器', '冷兵器']
print(p2.technology)  # ['石器', '冷兵器']
print(p1.technology)  # ['石器', '冷兵器']



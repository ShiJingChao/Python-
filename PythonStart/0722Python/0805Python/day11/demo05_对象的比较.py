"""
    对象的比较:
        1. 基础数据类型的对象
            is : 比较的是对象的地址
            == : 比较的是对象的内容

            cmd 对于小整数 [-5, 256] 之间的数字,进行了缓存, 所以可以在缓存中重复使用;
            pycharm做了优化, 他把不可变数据类型中的很大范围的数据都做了缓存, 所以在缓存中可以重复使用,
                在pycharm中对某些即使很大的整数进行地址的比较, is, 都是相等的;

        2. 自定义类的对象
            is 和 == 比较的都是对象的地址

        3. 需求: 只要俩对象的属性值都相等, 我们就认为这俩对象相等;
            通过__eq__()方法去实现;  必须有返回值bool, 用来代表是否相等;
            使用__eq__()方法定义比较的规则, 对象进行比较时, 需要使用 == 关系运算符进行比较;

            对象.__dict__ 获取当前对象的属性, 包括私有(字典{"属性名": "属性值", ...})
"""

a = "12345"
b = "12345"

if a is b:     #  a == b:
    print(True)
else:
    print(False)

c = 621
d = 621
if c is d:
    print("c的地址:", id(c))
    print("d的地址:", id(d))
    print(True)
else:
    print(False)

"""
c的地址: 31413168
d的地址: 31413168
True
"""
print(" ---------------------------- ")
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
print(id(list1))  # 3691080
print(id(list2))  # 3691592

# is 比较的地址
# == 比较的是值

if list2 == list1:
    print("两个列表的值相等")
else:
    print("两个列表的值不不不不相等")

if list2 is list1:
    print("两个列表的地址相等")
else:
    print("两个列表的地址不不不不相等")

print(" -------------------- 自定义类的对象 ----------------")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):  # other, 另外一个要进行比较的对象
        if self.__dict__ == other.__dict__:  # 如果当前对象和被比较对象的所有属性值相等, 我们就认为这俩对象相等
            return True
        else:
            return False


p1 = Person('副栉龙', 18)
p2 = Person('副栉龙', 18)
print("p1的地址:", id(p1))  # p1的地址: 35298824
print("p2的地址:", id(p2))  # p2的地址: 35298696

if p1 == p2:
    print("用==运算符,判断相等")

if p1 is p2:
    print("这俩对象地址相等")





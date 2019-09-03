"""
    __hash__() : 当获取对象的哈希值时, 调用该魔术方法;
                hash(对象)

                set, list, dict 没有__hash__()方法, hash(列表对象): 报错,不可被哈希;
                        列表对象.__hash__ --> None

                如果只定义了__eq__()方法, 而没有定义__hash__(), 默认会将__hash__方法设置为None
        哈希算法:
            1. 算法: 加减乘除就是一个算法; 输入*2-->输出;
                输入4, 输出8;

            2. 哈希算法: Hash, 中文翻译为散列或者哈希;
                    可以输入, 计算出一个结果, 结果为输出值,也叫哈希值;
                    输入: 字符串, 数据, 也可以是各种文件;

                    特点:
                        1. 同一个对象的哈希值是固定的;
                        2. 不能够从结果推算出输入;

                    应用的场景:
                        保证信息的安全;密码输入;数据传输等;

            3. 哈希与基础数据类型
                hash() 可以应用的数据类型, str, number, tuple
                        不可应用于 list, dict, set

                可被哈希的对象的特点:
                    1. 在对象的生命周期内, 其哈希值不会发生改变;
                    2. 这个对象可以与其他对象进行比较; 这个对象中要实现了__eq__()方法;

                * 凡是不可被哈希的对象, 他的__hash__都是None;

            4. 字典中的key: 不可变的数据类型; 可被哈希的对象;
               集合中的元素: 不可变的数据类型; 可被哈希的对象;
"""

s1 = '三角龙'
s2 = '剑龙'

print(hash(s1))  # -2682103812133621423
print(hash(s2))  # -1272876723272132871
print(hash(128))
print(hash(998.321))

t1 = (1, 2, 3)
print(hash(t1))  # 2528502973977326415

list1 = [1, 2, 3]
# print(hash(list1))  # TypeError: unhashable type: 'list'

print(list1.__hash__)  # None

set1 = {1, 2, 3}
print(set1.__hash__)  # None

class Person:
    def show_me(self):
        print("啦啦啦啦, 我是甲龙")

    def __hash__(self):
        pass

p = Person()
# print(p.show_me())  # 此时为函数的调用, 打印的是函数执行的结果, 也就是返回值
print(p.show_me)  # 打印对象的函数名;  <bound method Person.show_me of <__main__.Person object at 0x00000000026A9AC8>>

print(" ---------------A-------------------- ")


# class A:
#     def __init__(self):
#         self.name = 1
#
#
# a = A()
# print(id(a))  # 35298696
# print(hash(a))  # -9223372036852569640
# print(hash(a) * 16 )  # -147573952589641114240
# ? 哈希值和内存地址之间的16的关系;


print(" ------------------B--------------------- ")


class A:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):  # 定义对象之间比较的规则
        if self.name == other.name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.name)


a1 = A("无齿翼龙")
a2 = A("无齿翼龙")

print(a1 == a2)  # True
print(a1.__hash__)  # None
print(a2.__hash__)  # None
# print(hash(a1))   # TypeError: unhashable type: 'A'
# print(hash(a2))   # TypeError: unhashable type: 'A'

print(hash(a1))  # 6884713593658924492
print(hash(a2))  # 6884713593658924492

# 练习1: 如果两个数都能被6整除, 则让这俩数比较结果为相等
class Num:
    def __init__(self, num):
        self.num= num

    def __eq__(self, other):
        if self.num % 6 == 0 and other.num % 6 == 0:
            return True
        else:
            return False


n1 = Num(6)
n2 = Num(12)

if n1 == n2:
    print("相等")

# 练习2: 设计二位坐标类Point判断2个坐标是否相等,
#       并能根据hash函数计算坐标的哈希值;


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))


point1 = Point(3, 4)
point2 = Point(3, 4)

print(point1 == point2)

print(hash(point1))  # 6884713593658924492
print(hash(point2))  # 6884713593658924492





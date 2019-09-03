"""
    函数的参数:
        形参可以是什么样子的?
            1. 位置参数: postional arguments 默认的参数
                实参的个数与形参相同, 实参与形参一一对应;

            2. 默认值参数: default arguments
                定义一个函数的时候, 给形参一个默认的值;

                默认值参数:
                    1. 给默认值参数的形参传值时, 函数会采用实参的值
                    2. 不给默认值参数的形参传值时, 函数会采用定义时默认的值

                [注意]:
                    1. 默认值参数的赋值时机: 函数声明的时候就被赋值了;
                    程序执行的过程:
                            顺序执行
                            函数的声明定义语句(默认值参数的赋值) --->  被执行
                                函数体 --->  不被执行(调用时才执行)
                    2. 如果默认值参数的值是一个可变数据类型对象, 那么函数多次调用, 操作的是同一个参数对象
                        如果不想使用同一个参数变量,可以使用实参进行覆盖;

            3. 可变参数
                    可变长的参数, 参数的个数是不确定的; 用于接收(0-N)个参数;

                    1. 可变元祖参数: *参数名
                            传入的实参 *元组: *具有打散序列的功能, 将元组中的每个元素作为可变参数传入

                    2. 可变字典参数: **参数名
                            传入实参时:  key=value, key=value, 关键字参数形式传入
                            传入实参时 **字典: **具有打散字典的功能, 将字典中的键值对以关键字参数的形式传入
    问题:
        如果在同一个函数中, 同时出现位置参数,可变元组参数,默认值参数,可变字典参数,参数有什么位置要求吗?

            要求遵守顺序: 位置参数, 可变元组参数, 默认值参数, 可变字典参数

"""

def get_sum(a, b):  # 位置参数
    return a + b

get_sum(10, 20)

def get_sum2(a, b=100):  # a:位置参数 b:默认值参数
    print("参数a的值为:", a)
    print("参数b的值为:", b)
    return a + b

get_sum2(90)
print("-------------")
get_sum2(90, 1)
get_sum2(90, b=1)
print("~~~~~~~~~~~~~~~~~~")

num = 100

def get_sum3(a, b=num):   # 默认值参数的赋值时机: 函数声明的时候;
    print("参数a的值为:", a)
    print("参数b的值为:", b)
    return a + b

num += 3  # num = num + 3 = 100 + 3 = 103

get_sum3(100)  # 参数b的值为: 100

print("*" * 30)

list1 = ["a", "b", "c"]

def get_list(b=list1):  # 默认值参数
    b.append("d")
    return b  # 返回值为参数b

print(get_list())  # 相当于打印参数b  ['a', 'b', 'c', 'd']
print(get_list())  # 相当于打印参数b  ['a', 'b', 'c', 'd', 'd']

print(get_list(["a", "b", "c"]))  # ['a', 'b', 'c', 'd']

print("========================")

dict1 = {"age": "三十三", "name": "小黄花"}

import random
def get_dict(b=dict1):
    # chr() 传入编码 给出对应的字符 65A-90Z
    code = random.randint(65, 90)
    b[chr(code)] = code  #  {"A": 65}
    return b

print(get_dict())  # {'age': '三十三', 'name': '小黄花', 'S': 83}
print(get_dict())  # {'age': '三十三', 'name': '小黄花', 'S': 83, 'E': 69}

print("----------------华丽丽的:可变元组参数-------------------")

def tuple_args(*args):  # 可变元祖参数 参数的个数是不确定的 0- N
    print(args)
    print(type(args))

tuple_args()  # () <class 'tuple'>
tuple_args(1, 2, 3, 4)  # 实参 (1, 2, 3, 4)

tp1 = ("李小花", "王二狗", "刘三胖")

tuple_args(tp1)  # (('李小花', '王二狗', '刘三胖'),)
tuple_args(*tp1)  # ('李小花', '王二狗', '刘三胖')  * 具有打散序列的功能

print("----------------华丽丽的:可变字典参数-------------------")

def dict_args(**kwargs):  # key word arguments 关键字参数 可变的是参数个数 0-N
    print(kwargs.get('name'))
    # print(kwargs)
    # print(type(kwargs))

dict_args()  # {}
dict_args(name="lixuer")  # {'name': 'lixuer'}
dict_args(name='小花', age=18, sex='女')  # {'name': '小花', 'age': 18, 'sex': '女'}

dict1 = {"name": "敖丙", "brother": "敖甲"}
dict_args(**dict1)  # ** 具有打散字典的功能, 直接将字典中的键值对作为可变字典参数传入

print("%%%%%%%%" * 30)

def mix_args(a, b, c, *d, e="默认值1", f="默认值2", **g):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("可变元组参数d:", d)
    print("默认值参数e:", e)
    print("默认值参数f:", f)
    print("可变字典参数g:", g)

mix_args(1, "abc", 3, "A", "B", "C", "D", f="我是默认值", name="小花", friend="二狗")

print("================")

# def mix_args2(a, b="b",  *p, **kwargs):
#     print("a:", a)
#     print("b:", b)
#     print("*p:", p)
#     print("**kwargs:", kwargs)
#
# mix_args2(100, "a", "b", "c", name="小花")

# a: 100
# b: a
# *p: ('b', 'c')
# **kwargs: {'name': '小花'}
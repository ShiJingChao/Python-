"""
1.定义一个函数，通过参数，接收三角形边长，打印三角形
*
**
***
****
*****
******
*******
********
"""


def get_triangle(n):  # 边长
    for x in range(1, n+1):
        print('*' * x)


get_triangle(6)

"""
2.定义一个函数，求一个数的绝对值
"""


def get_abs(n):  # 数
    if n >= 0:
        return n
    else:
        return 0-n


print(get_abs(-0.99))

"""
3.定义一个函数，求1-n的范围内，偶数的和
"""


def get_even(n):
    s = 0  # 用来记录前1-n个数的和
    for x in range(2, n+1, 2):
        s += x
    return s


print(get_even(100))  # 2550

"""
4.定义一个函数，返回两个数中的最大值
"""

def get_big_num(a, b):
    if a > b:
        return a
    else:
        return b

print(get_big_num(100, 200))


"""
5.定义一个函数，用于求2019年1月到month前一个月的总天数, month最小为2
step1: 遍历出1-n的每个月份
step2: 分别或得每个月份的天数
step3: 将每个月份的天数加在总天数中
"""


def days(n):
    list1 = [1, 3, 5, 7, 8, 10, 12]
    num = 0  # 计算总天数
    for i in range(1, n):  # 获取1-month前一个月的所有月份
        if i in list1:
            month = 31  # 当前月份的天数
        elif i == 2:
            month = 28  # 当前月份的天数
        else:
            month = 30  # 当前月份的天数
        num += month
    return num


print(days(7))  # 1+2+3+4+5+6   31+28+31+30+31+30 = 181


"""
6.定义一个函数，求两个数的最大公约数
"""


def get_divisor(a, b):  # a=303, b=104
    temp_num = b  # 代表a,b中的较小数 temp_num=104
    if a < b:
        temp_num = a

    for x in range(temp_num, 0, -1):  # 104, 103, 102, ...., 1,
        if a % x == 0 and b % x == 0:
            return x


# def common_divisor(a,b):
#     list1 = []  # a数的所有约数 [2,3,4]
#     list2 = []  # b数的所有约数 [2,4,6]
#     for i in range(1,a):
#         if a % i == 0:
#             list1.append(i)
#     print(list1)
#     for j in range(1,b):
#         if b % j == 0:
#             list2.append(j)
#     print(list2)
#     set1=set(list1)&set(list2)  # [2,4]
#     list3=list(set1)
#     return max(list3)  # 4

"""
7.定义一个函数，求两个数的最小公倍数
"""


def get_multiple(a, b):  # 3, 7
    for x in range(1, a * b + 1):
        if x % a == 0 and x % b == 0:
            return x


print(get_multiple(3, 6))


def get_multiple_two(a, b):  # 3, 7
    temp_num = b  # step1: 找到a,b中较大数
    if a > b :
        temp_num = a

    for x in range(temp_num, a * b + 1):
        if x % a == 0 and x % b == 0:
            return x


print(get_multiple_two(3, 7))

"""
8.使用递归算法求兔子问题，第n个月有几只兔子?
    最开始一对小兔子;
    小兔子成长到第三个月变成成熟兔子;
    成熟兔子每个月可以生一对小兔子;
	1 1 2 3 5 8 13 21 34 55 89 144 ...... 斐波那契数列

观察发现:
    每相邻三个数之间的关系: 第三个数 = 前两个数之和

分析:
    求第n个月的兔子对数 = 第n-1个月兔子的对数 + 第n-2个月兔子对数
    第4个月 = 第3个月 + 第2个月 --> 2 + 1
    第3个月 = 第2个月 + 第1个月 --> 2
    第2个月 = 1
    第1个月 = 1
"""


# 求第n个月兔子的总对数
def get_rabbit_count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return get_rabbit_count(n-1) + get_rabbit_count(n-2)


print(get_rabbit_count(5))  # 5
print(get_rabbit_count(10))  # 55
















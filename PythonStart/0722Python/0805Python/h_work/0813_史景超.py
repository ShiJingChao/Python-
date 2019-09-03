
# 1.定义一个函数，通过参数，接收三角形边长，打印三角形
# import math
# def side(a, b):  # 三角形
#      for i in range(1, min(a, b) + 1):
#           print("*" * int(i * max(a, b) / min(a, b)))
#
# side(3, 4)

# 2.定义一个函数，求一个数的绝对值
# def abss(a):
#     if a < 0:
#         return 0-b
#     else:
#         return a
# print(abss(-10))

# 3.定义一个函数，求1-n的范围内，偶数的和
# def summ(n):
#     s = 0
#     for i in range(2,n+1,2):
#         s = s+i
#     return s
# print(summ(10))


# 4.定义一个函数，返回两个数中的最大值
# def big(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(big(5,6))

# 5.定义一个函数，用于求2019年1月到month前一个月的总天数
# def day(m):
#     a = [0,31,59,90,120,151,181,212,243,273,304,334]
#     for i in range(1,len(a)):
#         if i == m:
#             return a[i-1]
# print(day(1))


# 6.定义一个函数，求两个数的最大公约数

def gcd(a,b):
    x = min(a,b)
    for i in range(x,1,-1):
        if a % i == 0 and b % i == 0:
            return i
    else:
        return "最大公约数为1"
print(gcd(15,30))

# 7.定义一个函数，求两个数的最小公倍数

def mul(a,b):
    m = gcd(a,b)
    if m == "最大公约数为1":
        return a*b
    else:
        return a*b//m
print(mul(129,270))


# 8.使用递归算法求兔子问题，第n个月有几只兔子?
# 	1 1 2 3	5 8 13 21 34 55 89 144 ......
# def fib_se(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib_se(n-1)+fib_se(n-2)
# a = fib_se(8)
# print(a)
#
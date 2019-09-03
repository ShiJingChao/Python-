"""
    函数的参数:
        形参: 形式上的参数; 在函数声明定义时, 写在括号里的变量
        实参: 实际上的参数; 在函数调用的时候, 写在调用处括号里的值;
            函数调用时,才能确定实参;

    函数调用:
        A: 函数名()
        B: 函数名(实参匹配形参)

"""
# 求1-n的阶乘
def factorial(n):  # 形参的本质 就是一个变量
    num = 1
    for x in range(1, n+1):
        num *= x
    print(num)

#  1. 求1-5的阶乘
factorial(5)  # 实参5
# def five_factorial():
#     num = 1  # 用来定义前n个数的乘积
#     for x in range(1, 6):
#         num *= x   # num = num * x  将num每次乘以x之后的结果 重新赋值给num变量
#     print(num)

# 2. 求1-10的阶乘
factorial(10)  # 实参10
# def ten_factorial():
#     num = 1  # 用来定义前n个数的乘积
#     for x in range(1, 11):
#         num *= x   # num = num * x  将num每次乘以x之后的结果 重新赋值给num变量
#     print(num)


# 3. 求1-100的阶乘
factorial(100)  # 实参100
# def hundred_factorial():
#     num = 1  # 用来定义前n个数的乘积
#     for x由 in range(1, 101):
#         num *= x   # num = num * x  将num每次乘以x之后的结果 重新赋值给num变量
#     print(num)

"""
练习:
1. 定义一个方法,求两个数的和,这两个数可以由参数传入
2. 定义一个方法,求三个数的平均值,这三个数..........
"""
def get_sum(a, b):
    print(a + b)

get_sum(100, 200)

def get_avg(a, b, c):
    print((a + b + c) / 3)

get_avg(100, 200, 300)


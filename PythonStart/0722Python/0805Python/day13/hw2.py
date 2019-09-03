"""
2.打印菱形(函数)
	1. 空格, *组成菱形
	2. 输入菱形上半部分行数即可打印

3.给2新增功能,验证输入的内容是否合法
	比如输入内容为 3,可以
	    输入内容为 a,不可以打印
	*
   ***
 ******
********
 ******
  ***
   *

4.给2新增功能, 支持循环输入
"""

def four(func):

    def inner():
        while True:
            func()

    return inner


def three(func):  # func: 被装饰的函数

    def inner():
        n = input("请输入菱形上半部分的行数:")
        if n.isdigit():   # 判断字符串是否全部由数字字符组成
            n = int(n)
            func(n)  #  此时,才是调用的rhombus()函数
        else:
            print("您的输入不合法!不能打印~")
    return inner

@four
@three
def rhombus(n):  # 菱形 参数:上半部分的行数
                                      # 1, 2, 3, 4, 5   -->  n 行数
                                      # 2, 4, 6, 8, 10  -->  2n 行数的两倍 --> stop
    for count in range(1, 2*n, 2):   # 1, 3, 5, 7,  9   --> 1-stop之间的所有的奇数
        s = "*" * count
        print(s.center(2*n-1))  # 1, 3, 5, 7, 9, ...

    for count in range(2*n-3, 0, -2):  # 2n-1: 1,3,5,7,9   stop: 0
        s = "*" * count
        print(s.center(2*n-1))


rhombus()
# 这是一个被装饰过的函数,
# 调用该函数时, 实际执行的是装饰器的内层函数(闭包函数) --> inner()
# 而inner()不需要参数, 所以此时, rhombus也不需要参数

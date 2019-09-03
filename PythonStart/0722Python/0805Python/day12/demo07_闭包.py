"""
    闭包:
        外层函数嵌套内层函数, 在内层函数中使用外层函数的局部变量;
        局部变量和内层函数统称为闭包;
        内层函数为闭包函数;

        * 闭包函数访问外层函数的局部变量时, 访问的总是该变量的最新值;

"""


def outer():
    x = 10  # 外层函数的局部变量

    def inner():
        nonlocal x  # 关键字标记 变量x 是外层函数的局部变量
        x += 1
        return x

    return inner
    # return inner()


r1 = outer()  # r1 --> 函数地址(内层函数)

print(r1())  # x=? 11
print(r1())  # x=? 12
print(r1())  # x=? 13



# return inner
# r = outer()  # print(inner)  --> 打印函数名 : 函数的地址
# print(r)  # r --> <function outer.<locals>.inner at 0x00000000026980D8>
#
# print(r())  # 此时才是调用inner()函数的调用处


# return inner()
# r = outer()
# print(r)  # 11




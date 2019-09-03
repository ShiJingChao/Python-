"""
    关键字:
        global : 在局部作用域中标记一个变量为全局变量
                    可以将局部变量变成一个全局变量

        nonlocal : 在局部作用域中标记一个变量是外层封闭作用域中的变量
                    可以修改外层(非全局)变量

        关键字 变量名
"""
# 举个栗子

g_num = 1000


def func():
    # print(g_num)  # 1000
    # g_num = 2000  # 在函数内部定义了一个与全局变量同名的局部变量
    # print(g_num)  # 2000
    # 在函数中修改全局变量g_num的值
    global g_num
    g_num = 2000


func()
print(g_num)  # 1000   2000

print("======================================")


def outer():
    o_num = 1000
    def inner():
        # print(o_num)  # 1000
        # o_num = 2000  # 在内层函数中声明了一个和外层函数中重名的局部变量
        # print(o_num)  # 2000
        # 在内层函数中 修改封闭作用域中的o_num变量
        nonlocal o_num
        o_num = 2000
        print(o_num)  # 2000

    inner()
    print(o_num)  # 1000  2000


outer()




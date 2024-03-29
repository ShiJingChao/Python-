"""
    作用域
        1. 概念: 针对变量而言, 程序执行的过程中,变量能够起作用(可应用)的范围;
                * 只有 函数, 类, 模块 会产生作用域, 代码块不会产生作用域;

        2. 作用域的分类:
            根据变量的位置,可以将作用域分为四类;
            LEGB;
            Local, 局部作用域(函数内部的作用域)
            Enclosing, 封闭作用域(两层函数嵌套, 外层嵌套函数的作用域)
            Global, 全局的作用域(模块的作用域)
            Bulid-in, 内建的作用域(python内置的)

        3.作用域的查找规则, 遵循LEGB法则;
            按顺序依次在局部作用域,封闭作用域,全局作用域,内建作用于中进行查找,一旦查找到了,就不会继续进行查找;
            如果在LEGB中都没有查找到, 则会发生异常: NameError: name 'abc' is not defined

            * 局部作用域中可以访问到 局部作用域, 封闭作用域, 全局作用域, 内建作用域中的变量;
            * 封闭作用域中可以访问到 封闭作用域, 全局作用作用域域, 内建作用域中的变量;
                封闭作用域不能访问到局部作用域中的变量
            * 全局作用域中可以访问到 自己和内建作用域中的变量;
                    不能访问到封闭作用域和局部作用域中的内容;

"""
a = "a"  # 全局作用域中的变量

def outer():
    b = "b"  # 封闭作用域中的变量
    # print(b, a, type) # b a <class 'type'>
    # print(c)  #  NameError
    def inner():
        c = "c"  # 局部作用域中的变量
        # print(a, b, c, type)  # a b c <class 'type'>

    inner()

outer()

print(a, type)  # a <class 'type'>
# print(b, c)



"""
    函数的定义和调用:
        函数: 把具有某一段功能的代码提取出来, 封装成一个代码块, 在需要的时候进行调用;

        特点:
            A : 去除重复的代码;
            B : 当函数功能发生修改时, 只需要修改函数体即可;
                (增强程序的拓展性)

        函数体:
            实现函数功能的代码;
            1. 函数声明的时候, 不会执行函数体;
            2. 函数调用的时候, 才会执行函数体;
            3. 一个函数体可以被多次执行(一个函数可以被多次调用)

        函数定义的规则:
            def 函数名():
                函数体:实现函数功能的代码

        使用函数的步骤:
            step1: 先定义(声明)一个函数(函数的声明需要在调用之前)
            step2: 函数的调用

        函数名: 必须满足标识符的命名规则;
                数字字母下划线组成;
                数字不能打头;
                不能是关键字;
                ----
                建议: 1. 不能与python内置的函数名重名;
                      2. 不要使用拼音,多个英文单词组成的时候,中间以下划线连接;
"""
def get_sum():
    s = 0
    num = 1
    while num <= 10:
        s += num
        num += 1
    print(s)
# 1. while循环求1-10的和
# num_sum = 0
# num = 1
# while num <= 10:
#     num_sum += num
#     num += 1
# print(num_sum)
get_sum()

print("----------------")
print("python good good, i love python")

# 2. while循环用来求1-10的和
# s = 0
# num = 1
# while num <= 10:
#     s += num
#     num += 1
# print(s)
get_sum()


"""
练习:
1. 定义一个函数,用于求5的阶乘
2. 定义一个函数,打印三角形,然后调用
*
**
***
3. 定义一个函数,用于打印一行分割线
4. 定义一个函数,用于打印三行分割线
"""

def factorial():
    num = 1
    for x in range(1, 6):
        num *= x   # num = num * x
    print(num)

factorial()  # 120

def triangle():
    for x in range(1, 4):
        print("*" * x)

triangle()

def split_line():
    print("~~~~~~~~~~~~~~~~~")

split_line()

def three_lines():
    for x in range(3):
        split_line()  # 每次循环 调用split_line函数 ---> 每次循环 执行了一下split_line的函数体
        # print("~~~~~~~~~~~")

three_lines()

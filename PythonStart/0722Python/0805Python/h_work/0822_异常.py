# 1、定义一个函数func(filename) filename:文件的路径，
#   函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误。
import os

def func(filename):
    try:
        file = open(filename,"r",encoding="utf8")
        f =  file.read()
        file.close()
        print(f)
        return f
    except FileNotFoundError:
        print("文件不存在")

f = func("D:/1.txt")



# 2、编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数"的异常


# def com(num1,num2):
# #     if num1 <= num2:
# #         e = Exception("被减数不能小于减数")
# #         raise e
# #     else:
# #         print(num1-num2)
# #
# # num1 = int(input("输入第一个数"))
# # num2 = int(input("输入第二个数"))
# # com(num1,num2)



# 3、定义一个函数func(listinfo) listinfo:为列表，listinfo = [133, 88, 24, 33, 232, 44, 11, 44]，
# 返回列表小于100，且为偶数的数

def func(listinfo):
    a = []
    for i in listinfo:
        if i <100 and i % 2 == 0:
            a.append(i)
    return a


listinfo = [133, 88, 24, 33, 232, 44, 11, 44]
func(listinfo)
print(func(listinfo))


# 4.怎样理解单例模式？

"""
单例模式是一种开发过程中常用的设计模式，保证在类中只有一个对象实例存在，在程序运行期间只存在一个实例对象，避免内存空间的浪费


"""
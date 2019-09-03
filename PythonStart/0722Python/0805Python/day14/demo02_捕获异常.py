"""
    捕获异常: 异常的一种处理方式, 通过这种处理可以使python解释器在遇到错误时, 程序仍然能正常的执行结束
    ValueError
    IndexError
    NameError
    ....

    语法:
    try:
        代码

    except 异常的类型1: ValueError:
        对异常的处理...

    except 异常的类型2: ZeroDivisionError
        对异常的处理...

    多个except;

a除以b :  a / b
a除b : b / a
"""
# 需求: 用户输入一个整数, 把整数+10, 除5之后, 输出;

print(ValueError)  # <class 'ValueError'>
print(ZeroDivisionError)  # <class 'ZeroDivisionError'>

try:
    num = input("请输入一个整数:")  # str
    num = int(num)  # "9" --> 9
    num += 10
    num = 5 / num
    print(num)
except ValueError:
    print("输入的不是一个数字")
except ZeroDivisionError:
    print("-----over-----")





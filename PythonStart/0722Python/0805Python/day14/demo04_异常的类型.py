"""
   异常的类型:
    ValueError
    IndexError
    ZeroDivisionError

    理解:
        程序执行的过程中, 发生了错误, 此时python解释器, 会创建相应异常类的对象, 并把该异常对象抛出;

    捕获异常的理解:
        尝试执行某代码块, 执行的过程中, 遇到了抛出的异常对象, 捕获并进行处理;

    try:
        代码
    except 异常类型 as 异常对象:  --->  理解: 捕获该异常类型的异常对象,并进行处理
        异常的处理

    except Exception as 对象:  ---> 理解: 对于未知异常类型对象的捕获, 可以使用父类Exception进行捕获;
        处理
"""

print(NameError.__mro__)  # (<class 'NameError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
print(ValueError.__mro__)  # (<class 'ValueError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
print(IndexError.__mro__)  # (<class 'IndexError'>, <class 'LookupError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
print(ZeroDivisionError.__mro__)  # (<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)


try:
    list1 = ["万启龙", "小黄龙", "小黑龙", "大花龙"]

    n = 0
    while n <= len(list1):  # n <= 4;  n = 0,1,2,3,4
        print(list1[n])
        n += 1
except ValueError:  # 此时, 捕获的是ValueError异常类的对象
    print("---值错误----")
except NameError:
    print("---名错误----")
except Exception as e:   # 此时, 如果异常不是以上类型, 那么只要是Exception的对象或者子孙后代类对象, 都能够在此处被捕获到;
    print(type(e), e)

# class A:
#     def say(self):
#         pass
#
# class B(A):
#     def say(self):
#         pass
#
# class C(A):
#     def say(self):
#         pass
#
#
#
# def func(a_obj):
#     a_obj.say()


# func(C())


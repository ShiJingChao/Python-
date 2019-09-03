"""
    添加多个装饰器
"""

#
# def outer1(func):
#
#     def inner():
#         print("----装饰1-调用前----")
#         func()
#         print("----装饰1-调用后----")
#
#     return inner
#
#
# def outer2(func):
#
#     def inner():
#         print("====装饰2-调用前====")
#         func()
#         print("====装饰2-调用后====")
#     return inner
#
# @outer2
# @outer1
# def study():
#     print("亲爱的python,热爱的还是python")
#
#
# """
# ====装饰2-调用前====
# ----装饰1-调用前----
# 亲爱的python,热爱的还是python
# ----装饰1-调用后----
# ====装饰2-调用后====
# """
#
# study()

def say_hi(func):
    def wrapper(*args,**kwargs):
        print("Hi")
        ret = func(*args,**kwargs)
        print("Bye")
        return ret
    return wrapper

def say_yo(func):
    def wrapper(*args,**kwargs):
        print("Yo")
        return func(*args,**kwargs)
    return wrapper
@say_hi
@say_yo
def func():
    print("Rock&Roll")

func()



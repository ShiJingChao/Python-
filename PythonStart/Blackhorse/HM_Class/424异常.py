# try:
#     num = int(input("输入整数"))
# except:
#     print("输入错误")

# CLASS 426 错误类型捕获

# 在程序执行，可能会遇到不同类型的异常，
# 并且需要针对不同类型的异常，做出不同的相应，
# 这个时候就要捕获错误类型了
# 语法如下：
# try:
#   #尝试执行的代码
#   pass
# except 错误类型1：
#   针对错误类型1，对应的代码处理
#   pass
# except (错误类型2，错误类型3)：
#   针对错误类型2和3，对应的代码处理
# except Exception as result:
#   print("未知错误%s"%result)
# try:
# try:
#     num = int(input("请输入一个整数："))
#     result = 8/num
#     print(result)
# except ValueError:
#     print("请输入正确的整数")
# except ZeroDivisionError:
#     print("除数不能为0")

# CLASS 427 捕获未知错误
# 如果希望程序 无论出现任何错误，
# 都不会因为Python解释器抛出异常而被终止，
# 可以再增加一个except
# 语法如下：
# except：Exception as result：
#     print("未知错误%s"%result)
#
# try:
#     num = int(input("请输入一个整数："))
#     result = 8 / num
#     print(result)
# except ValueError:
#     print("请输入正确的整数")
# except Exception as result:
#     print("未知错误%s" % result)
# else:
#     print("try中没有异常执行")
# finally:
#     print("有没有异常都会执行")

# CLASS-429异常的传递
# 当函数/方法执行出现异常，会将异常传递给函数/方法的调用一方
def demo():
    return int(input("请输入整数："))


def demo2():
    return demo()


# 利用异常的传递性，在主程序捕获异常
try:
    print(demo())
except Exception as result:
    print("未知错误%s" % result)

# CLASS 430 主动抛出异常
# 抛出异常：在开发中满足特定的业务需求时，
# 希望抛出异常，可以创建一个Exception的对象
# 使用raise关键字抛出异常对象
# 用户登录模块 密码长度小于8，抛出异常
def input_password():
    # 1.提示用户输入密码
    pwd = input("请输入密码：")
    # 2.判断密码长度 >=8，返回用户输入的密码
    if len(pwd)>=8:
        return pwd
    # 3.如果<8主动抛出异常
    # 创建异常对象，可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")
    # 主动抛出异常
    raise ex
try:
    print(input_password())
except Exception as result:
    print(result)
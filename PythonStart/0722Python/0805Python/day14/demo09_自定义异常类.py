"""
    自定义异常类:
        异常可以抛出, 打断程序的执行;
"""


class PassWordError(Exception):
    def __init__(self, at_least, your_len):  # 参数1: 规定密码的最小长度; 参数2:当前输入的密码长度
        self.at_least = at_least
        self.your_len = your_len

    def __str__(self):
        return "规定的最小长度为{}, 您当前设置的长度为{}".format(self.at_least, self.your_len)


def func():
    pw = input("请输入您的密码:")

    if len(pw) >= 8:
        print("您的密码设置成功")
    else:
        e = PassWordError(8, len(pw))
        raise e

func()






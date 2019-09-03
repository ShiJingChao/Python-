g_num = 100
g_list = []
_money = 0.1  # from 模块 import * 此时单下划线开头的变量,函数等无法导入到模块中去

__all__ = ["_money", "g_list"]  # __all__ 给列表中添加字符串元素, 能被导入到模块中的内容,添加到列表中去

# 传入参数的个数不固定, 将传入的所有参数求和并返回
def get_sum(*args):  # args = (10, 20, 30)  args形参是接收所有实参的元组
    s_num = 0
    for x in args:
        s_num += x
    return s_num


# print(__name__)


# 如果当前模块为主程序(单机鼠标右键,执行当前.py文件), 则执行以下代码; 此时 __name__ = __main__
# 如果当前模块为被导入的模块, 则不执行以下代码; 此时 __name__ 为 模块名(my_demo)
if __name__ == "__main__":
    r = get_sum(10, 20, 30)
    print(r)
    print(__name__)  # __main__




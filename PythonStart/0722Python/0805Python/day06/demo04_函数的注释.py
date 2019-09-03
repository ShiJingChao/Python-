"""
    函数的注释: 解释说明程序
        1,功能
        2,参数(函数的使用方法)  函数名(参数)
        3,返回值
        在函数体中,输入三对引号,回车,自动生成函数说明文档格式;

        查看函数的说明文档 函数名.__doc__
        如果该函数没有说明文档, 函数名.__doc__ 返回一个 None
"""

def get_sum(a, b):
    """
    求两个数的和
    :param a: 一个数
    :param b: 另一个数
    :return: 两个数的和
    """
    return a + b

print(get_sum.__doc__)

print(print.__doc__)

def get_big_num(a, b):
    if a > b:
        return a
    else:
        return b

print(get_big_num.__doc__)  # None



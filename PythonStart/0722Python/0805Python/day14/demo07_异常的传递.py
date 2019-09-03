"""
异常的传递:
    当函数中产生异常, 函数本身可以处理, 如果没有处理, 异常对象传递给了调用处.
    调用处应该处理, 如果调用处也没有处理, 异常对象就会传递给主程序, 主程序应该处理,
    如果主程序也没有处理, 打断程序的执行;

    函数, 调用处, 主程序中任一地方, 处理了异常, 都不会打断程序的执行;

"""
import random


def get_element(index):
    """
    根据索引值, 获取对应的龙
    :param index: 索引值
    :return: 字符串龙
    """
    d_list = ["似鸟龙", "似鸡龙", "副栉龙", "无齿翼龙", "甲龙"]
    return d_list[index]
    # try:
    #     d_list = ["似鸟龙", "似鸡龙", "副栉龙", "无齿翼龙", "甲龙"]
    #     return d_list[index]
    # except:
    #     return "发生了异常, 容俺处理一下子"


def guss_dragon():
    index = random.randint(0, 10)  # [start, stop]
    print(get_element(index))
    # try:
    #     print(get_element(index))
    # except:
    #     print("发生了异常, 容俺处理一下子")


if __name__ == "__main__":
    try:
        guss_dragon()
    except:
        print("发生了异常, 容俺处理一下子")

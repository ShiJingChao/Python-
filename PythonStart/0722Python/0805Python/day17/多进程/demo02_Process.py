"""
    多进程

    执行一个py程序, 由系统创建一个主进程, 执行;
    在这个主进程的过程中, 又创建了一个子进程, 让子进程执行;
"""
from multiprocessing import Process
import time
import random


def func():
    for i in range(3):
        print("中秋节你给女朋友准备什么礼物了? 你给男朋友准备啥礼物了?")
        time.sleep(3)


# func()  # 相当于在主进程中调用了该函数

if __name__ == "__main__":
    # 创建一个进程, 让进程去执行这个函数
    p = Process(target=func)  # target : 这个进程执行的任务

    # 让这个进程去执行
    p.start()

    for x in range(3):
        print("\t主进程...第{}次循环...".format(x+1))
        time.sleep(random.random())  # 随机睡了0.几秒


    # 主进程虽然没有代码了, 但是主进程, 并未结束, 主进程会等待子进程执行完毕后再结束

"""
    1. 创建一个子进程, 打印1-100的数字
    2. 创建一个子进程, 打印A-Z的字母
"""



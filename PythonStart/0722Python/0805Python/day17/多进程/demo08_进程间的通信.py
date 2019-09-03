"""
    创建俩进程
    1. 往队列中存储数据,
    每次存储一个数随机睡0.几秒钟
    2. 一直不停地从队列中往外取数据
"""
from multiprocessing import Process, Queue
import time
import random


def save_number(q):  # 往队列存储数据, 参数: 为所操作的队列
    for x in range(1, 101):
        q.put(x)
        print("存储数据:{}".format(x))
        time.sleep(random.random())


def get_number(q):  # 从队列中获取数据, 参数: 为所操作的队列
    while True:
        print("\t从队列中取出的数据: {}".format(q.get()))


if __name__ == "__main__":

    q = Queue()

    p1 = Process(target=save_number, args=(q, ))
    p2 = Process(target=get_number, args=(q, ))

    p1.start()
    p2.start()












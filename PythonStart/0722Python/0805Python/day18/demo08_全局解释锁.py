"""
    全局解释锁:
        进程中都有一把自己的独立的全局解释锁, 在cpu调度执行线程的时候,
        执行哪个线程, 就给这个线程上一把全局解释锁, 在调度结束之后, 在释放这把锁;

        计算密集型;
            需要进行大量的计算, 消耗cpu的资源, 比如计算圆周率, 给视频进行高清的解码;

        *可以多进程的方式, 由系统创建一个主进程, 在进程中又去创建了一个主线程, 主线程中执行的

        IO密集型;
            涉及到网络, 磁盘的IO操作;
"""
from threading import Thread
from multiprocessing import Process
import time


# 做了一亿次的运算
def func():
    t1 = time.time()
    i = 0
    for x in range(100000000):
        i += 1
    t2 = time.time()
    print(t2 - t1)


# 做了两亿次的运算
def func2():
    t1 = time.time()
    i = 0
    for x in range(200000000):
        i += 1
    t2 = time.time()
    print(t2 - t1)


if __name__ == "__main__":

    for x in range(2):
        p = Process(target=func)
        p.start()
    """
    12.792732000350952
    12.863735914230347
    """
    # for x in range(2):
    #     t = Thread(target=func)
    #     t.start()
    """
    18.80807590484619
    19.0670907497406
    """

    # t = Thread(target=func2)
    # t.start()
    # 19.563118934631348

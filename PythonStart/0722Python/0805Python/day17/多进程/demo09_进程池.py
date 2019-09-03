"""
    进程池
"""
from multiprocessing import Pool


def func():
    print("啦啦啦啦------")


if __name__ == "__main__":

    # 创建进程池对象, 并指明了每个进程的任务, 子进程们就自动启动了;
    p = Pool(3, func)  # 池子里, 有三个子进程, 每个子进程都执行func的功能
    p.close()  # 代表没有新的进程加入进程池了, 在调用join方法之前必须要调用close方法
    p.join()  # 阻塞, 阻塞当前程序的执行, 直到自己进程池的进程执行完毕

    print("---主进程就是我, 我就是主进程----")



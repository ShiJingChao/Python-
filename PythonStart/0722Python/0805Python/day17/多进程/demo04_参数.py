"""
    Process:
        target: 指定该进程执行的任务
        name: 默认值Process-1, Process-2, ..., 也可以给名字重新赋值
        args: 类型为元组, 用来给target中的函数传参;
        kwargs: 类型为字典, 用来给target中的函数传参; 字典中的key为形参, 字典中的value为实参;

    os.getpid() : 获取当前正在执行的进程id
    os.getppid() : 获取当前正在执行的父进程的进程id

"""
from multiprocessing import Process
import os


def func(a, b):
    print("参数的和为: ", a + b)
    print("当前执行的进程是:{}".format(os.getpid()))
    print("当前执行的进程的爹(父进程)是:{}".format(os.getppid()))


if __name__ == "__main__":

    print("\t主进程中的进程id是:{}".format(os.getpid()))

    # 创建进程对象
    # p = Process(target=func, name="进程1", args=(100, 1))
    # p = Process(target=func, name="进程1", kwargs={"a": 100, "b": 1})
    p = Process(target=func, name="进程1", args=(100,), kwargs={"b": 1})
    print(p.name)  # Process-1

    p.start()

    # p2 = Process(target=func, name="进程2")
    # print(p2.name)  # Process-2

    # p3 = Process(target=func, name="进程3")
    # print(p3.name)  # Process-3


# 创建一个进程, 传入一个参数(睡眠时间),
# 让程序睡一会儿, 打印当前程序执行的时间;
# 思路: func() ---> 先计算当前时间, 中间执行代码,
# 最后在计算当前时间, 将两个时间做差,
# 差:就是程序执行的时间










"""
    当前时间到1970-01-01 00:00:00的秒数

    .join()  阻塞当前进程的执行, 直到自己进程执行完毕
    .join(time)  阻塞当前进程time秒钟, 如果阻塞时间大于自己进程的执行时间, 则只堵着到自己进程执行完毕

    .is_alive() 判断进程是否还活着;
"""
from multiprocessing import Process
import time


def func(s_time):
    t1 = time.time()  # 时间戳  程序执行到第6行代码时的时间戳
    time.sleep(s_time)
    t2 = time.time()  # 时间戳 程序执行到第8行代码时的时间戳
    print("程序执行的时间:%.5f" % (t2 - t1))  # 时间差为: 秒数


if __name__ == "__main__":
    p = Process(target=func, args=(2, ))
    p.start()
    print(p.is_alive())  # True

    # 希望子进程执行完毕后再执行主进程;
    # p.join()  # 阻塞当前进程的执行, 直到p进程执行完毕
              # 堵着主进程, 不让主进程执行....直到我自己的进程执行完毕了, 再让主进程继续执行

    # p.join(1)  # 阻塞当前进程的执行, 阻塞时间为1s
    p.join(5)  # 阻塞时间如果大于p进程的执行时间, 则只阻塞当前进程直到自己执行完毕;

    print("\t嗨嗨嗨, 我是一个主进程, 我来刷点存在感....")
    print(p.is_alive())  # False





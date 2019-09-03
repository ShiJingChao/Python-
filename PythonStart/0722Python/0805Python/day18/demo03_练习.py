"""
    两个线程对同一个全局变量分别进行1000万次+1的操作

    for x in range(10000000):
        i += 1

        lock.release()
        lock.acquire()
"""
from threading import Thread, Lock

i = 0
lock = Lock()


def func_add():
    global i  # 全局变量i
    for x in range(10000000):
        lock.acquire()
        i += 1
        lock.release()


if __name__ == "__main__":
    t1 = Thread(target=func_add)
    t2 = Thread(target=func_add)
    t1.start()
    t2.start()

    t1.join()  # 阻塞(它后边代码的执行), 主线程的执行, 直到t1执行完毕
    t2.join()  # 阻塞 主线程的执行, 直到t2执行完毕

    print(i)  # 20000000打印i, 主线程等着子线程都执行完了, 才打印的i



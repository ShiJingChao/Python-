"""
    线程对象的常用方法和参数
    Thread()
        参数1: 被执行的任务
        参数2: name= 线程的名字
        参数3: args=() 类型为元组, 用来给被执行的函数, 传递参数
        参数4: kwargs={} 类型为字典, 用来给被执行的函数, 传递参数; key为参数名, value为参数值;

    .join()  阻塞当前线程的执行, 直到自己线程执行完毕
            如果设置了timeout(阻塞时间), 若在阻塞时间内t线程执行完毕, 则不会再继续阻塞

    .is_alive() 判断该线程是否还活着
"""
from threading import Thread, current_thread
import time


def func(name1, name2):
    print("{}和{}被会会蛰了....真真真真真...疼啊...".format(name1, name2))
    time.sleep(2)


if __name__ == "__main__":

    t = Thread(target=func, name="t线程", args=("张杰", ), kwargs={"name2": "张碧晨"})
    t.start()
    print(t.is_alive())  # True
    # print(t.name)  # 子线程名字 Thread-1  t线程
    # print(current_thread().name)  # 主线程

    # t1 = Thread(target=func)
    # print(t1.name)  # Thread-2
    t.join(10)  # 阻塞当前线程的执行, 直到自己线程执行完毕
                # 阻塞主线程的执行, 直到t线程执行完毕
                # timeout 阻塞时间, 如果t线程已经执行完毕, 则不会继续阻塞

    print("啦啦啦...我是八卦娱乐制造者....")
    print(t.is_alive())  # False




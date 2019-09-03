"""
    自定义线程类

        传参睡一下, 计算程序执行的时间
"""
from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, s_time):  # 睡觉的时间
        super().__init__()
        self.s_time = s_time

    def run(self):  # 重写run方法, start线程对象时, 会自动的调用run方法,
        # 将该线程类执行的具体功能写入到当前方法中去
        t1 = time.time()
        time.sleep(self.s_time)
        t2 = time.time()
        print("程序执行的时间: %.5f" % (t2 - t1))


if __name__ == "__main__":

    t = MyThread(2)
    t.start()








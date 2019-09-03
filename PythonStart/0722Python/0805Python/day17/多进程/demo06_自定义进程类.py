"""
    自定义进程类

        该进程执行的功能, 写到run方法中;
        进程对象执行的时候, 会自动的调用run方法;
"""
from multiprocessing import Process
import time, os


# 自定义进程类, 参数:睡的时间-->属性
class MyProcess(Process):
    def __init__(self, s_time, group=None, target=None, name=None, args=(), **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.s_time = s_time

    # 新增属性: 表示睡眠时间
    # def __init__(self, s_time):
    #     super().__init__()
    #     self.s_time = s_time

    # 方法的重写: 方法名和父类方法名一模一样
    def run(self):
        t1 = time.time()  # 时间戳 , 秒数
        time.sleep(self.s_time)
        t2 = time.time()  # 时间戳 , 秒数
        print("进程{}, 执行的时间是{:.5f}".format(os.getpid(), t2 - t1))


if __name__ == "__main__":
    p = MyProcess(2)
    p.start()









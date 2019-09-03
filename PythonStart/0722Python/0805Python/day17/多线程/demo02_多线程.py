"""
    多线程
"""
import threading

def sing():
    for x in range(5):
        # 打印当前执行的线程的名字;
        print("\t{}唱支山歌给党听~~~~~~{}".format(threading.current_thread().name, x + 1))


if __name__ == "__main__":
    print("当前线程为:{}".format(threading.current_thread().name))

    t = threading.Thread(target=sing)  # 创建子线程对象, 并指明执行的具体任务
    t.start()  # 让这个线程启动

    print("我是一个主线程, 啦啦啦啦啦---")
"""
1. 创建一个线程, 打印100个数字, 并打印当前线程的名字
2. 创建一个线程, 随机打印100个字母, 并打印当前线程的名字
"""



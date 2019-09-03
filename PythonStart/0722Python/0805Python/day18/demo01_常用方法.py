"""
    常用方法:
        1. join()
        2. is_alive()
        3. isAlive()  同上
        4. getName()  获取线程名字, 直接操作属性的效果一样
        5. setName()  设置线程名字, 直接操作属性的效果一样
        6. enumerate()  获取当前正在执行的线程对象的列表
        7. activeCount() 获取正在执行的线程数量, len(enumerate())
"""
from threading import Thread, enumerate, active_count, activeCount
import time, random


def func():
    print("今天倒数第二天, 你复习的怎么样啦?")
    time.sleep(random.random())


if __name__ == "__main__":
    t = Thread(target=func, name="t线程")  # Thread-1
    # print(t.name)  # t线程
    # print(t.getName())  # t线程
    # t.name = "线程t"
    # print("改了个名: ", t.name)
    # t.setName("线t程")
    # print("呦呦呦改了个名:", t.getName())

    t.start()
    # print(t.isAlive())  # True
    print("正在执行的线程列表:", enumerate())  # [主线程, t线程]
    print("正在执行的线程数量:", active_count())

    t.join()  # 阻塞主线程的执行, 等待t线程执行完毕后, 在执行底下的代码
    print("---我是主线程, 我等着t线程执行完毕后, 我再执行的----")
    # print(t.isAlive())  # False
    print("正在执行的线程列表:", enumerate())  # [主线程, ]
    print("正在执行的线程数量:", activeCount())












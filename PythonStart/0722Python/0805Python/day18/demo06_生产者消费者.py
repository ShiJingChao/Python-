"""
    生产者, 消费者
                对于队列而言, 生产者就是用来往队列中存储数据;
                              消费者就是用来从队列中取出数据;

    生产/消费 ---> 数字
    线程1: 生产者
    线程2: 消费者
"""
from threading import Thread, current_thread
from multiprocessing import Queue
import time, random


def product(q, q_product):  # 参数1: 生产消费所共同操作的队列 参数2: 生产者要生产的数据0~49
    # while True:
    #     if q_product.empty():
    #         break
    while not q_product.empty():  # 如果不为空, 就执行以下代码;
        num = q_product.get()  # 从队列中拿出将要生产的数据
        q.put(num)  # 将生产的数据放入队列中
        print("生产者线程:{}, 生产数据:{}".format(current_thread().name, num))  # 8
        time.sleep(3)


def customer(q):  # 消费的数据从 队列中 获取
    while True:
        res = q.get()  # block=True 阻塞, 直到获取到数据为止
        print("\t消费者线程:{}, 消费数据:{}".format(current_thread().name, res))  # Thread-2 --> 8


if __name__ == "__main__":
    q = Queue()  # 全局变量, 多线程之间可以修改可变全局变量的值

    q_product = Queue()  # 生产者要生产的数据 0~49
    for x in range(50):
        q_product.put(x)

    for x in range(3):
        t1 = Thread(target=product, args=(q, q_product))
        t1.start()

    for x in range(3):
        t2 = Thread(target=customer, args=(q, ))
        t2.start()














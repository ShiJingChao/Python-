"""
    北京 --> 南京
    1000张票

    携程, 飞猪, 支付宝, 微信, 火车站窗口, 12306

    需求: 多线程售票
    全局变量: ticket = 6
    开启4个线程: 同时售票
                成功售票之前, 手续时间, 随机睡0.几秒钟

    互斥锁: 锁, 锁门, 开门
        功能: 如果有一个线程访问到被锁住的资源了, 那么在解锁之前, 其他的线程都不能够访问到该资源;
        凡是上锁的地方, 必须解锁
"""
from threading import Thread, current_thread, Lock
import time, random

lock = Lock()
ticket = 6  # 票的总数


def sale_ticket():
    while True:
        global ticket
        lock.acquire()  # 上锁
        if ticket > 0:  # 卖票
            time.sleep(random.random())
            ticket -= 1
            print("{}: 售票一张, 余票:{}张".format(current_thread().name, ticket))
            lock.release()  # 解锁
        else:
            print("票已售完")
            lock.release()  # 解锁
            break


if __name__ == "__main__":

    for x in range(4):
        t = Thread(target=sale_ticket)
        t.start()
    """
    创建了4个线程, 每个线程去执行sale_ticket;
    
    每个线程, while True, 卖票, 卖票, 卖票, ...直到没票了, 跳出循环, 线程结束了
    
    """









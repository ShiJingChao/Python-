"""
    多线程传参, 不可变类型参数
                如果将不可变类型的全局变量作为参数传入子线程中, 子线程不会更改全局变量的值;

    线程1: 把59+1, score通过参数传入
    线程2: 获取score的值, score通过参数传入
    主线程, 等待以上线程执行完毕后, 获取全局变量score的值, 并打印
"""
from threading import Thread, current_thread

score = 59


def add_one(score):
    score += 1
    print("{}, score的值: {}".format(current_thread().name, score))  # 60


def get_score(score):
    print("{}, 获取的score的值是{}".format(current_thread().name, score))  # ?


if __name__ == "__main__":

    t1 = Thread(target=add_one, args=(score, ))
    t1.start()
    t1.join()  # 阻塞 主线程中底下代码的执行, 直到t1执行完毕  60

    t2 = Thread(target=get_score, args=(score,))  # 全局变量score
    t2.start()
    t2.join()  # 阻塞 主线程中底下代码的执行, 直到t2执行完毕  59

    # 看一下全局变量的值 有没有被更改
    print("主线程中全局变量score: {}".format(score))   # 59







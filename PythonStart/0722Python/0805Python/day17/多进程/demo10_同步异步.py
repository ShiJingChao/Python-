"""
    目标: 小花跟二狗去吃饭, 二狗说我要先上厕所;

    同步:
        1. 二狗上厕所, 小花等着
        2. 二狗出来, 小花二狗一起去吃饭

    异步:
        1. 二狗上厕所; 小花自己去吃饭
        2. 二狗上完厕所再去吃饭
"""
from multiprocessing import Pool
import time, random


def eat():
    print("去吃饭......")
    time.sleep(random.random())


def WC():
    print("先上厕所")
    time.sleep(random.random())
    print("再去吃饭")
    time.sleep(random.random())


if __name__ == "__main__":

    p = Pool(2)

    # 同步
    # p.apply(eat)
    # p.apply(WC)

    # 异步
    p.apply_async(eat)
    p.apply_async(WC)

    p.close()
    p.join()

    print("---别人笑我太疯癫, 我笑别人不是主进程---")











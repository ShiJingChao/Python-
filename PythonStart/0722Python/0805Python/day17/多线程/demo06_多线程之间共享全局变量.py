"""
    多线程之间共享全局变量
"""
from threading import Thread, current_thread

score = 59


def change_score():
    global score  # 使用global关键字标记全局变量
    score += 1
    print("更改后的score值为: ", score)


def get_score():
    global score
    print("获取到的score值为:", score)


# print(score)  # 59
# change_score()  # 60
# print(score)  # 60

if __name__ == "__main__":
    t1 = Thread(target=change_score)
    t2 = Thread(target=get_score)

    t1.start()
    t1.join()  # 先把t1线程执行完毕  60
    print("主线程:", score)  # 60

    t2.start()
    t2.join()  # 再把t2线程执行完毕 60

    print("主线程:", score)  # 最后在执行主线程 60



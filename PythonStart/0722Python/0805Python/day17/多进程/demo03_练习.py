from multiprocessing import Process
import time, random, os


def print_number():
    for num in range(1, 101):
        print("p1进程.....{}".format(num))
        time.sleep(random.random())


def print_alpha():
    for code in range(65, 91):
        print("\tp2进程.....{}".format(chr(code)))
        time.sleep(random.random())


if __name__ == "__main__":

    p1 = Process(target=print_number)
    p2 = Process(target=print_alpha)

    p1.start()
    p2.start()

    print("嗨嗨嗨, 刷点存在感, 我是主进程....")










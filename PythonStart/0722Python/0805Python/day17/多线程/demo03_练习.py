from threading import Thread, current_thread
import random, time


def print_number():
    for x in range(1, 101):
        print("%s, 打印数字: %d" % (current_thread().name, x))


def print_alpha():
    for x in range(1, 101):
        # A-Z: 65-90  a-z: 97-122
        code = random.randint(97, 122)
        print("\t%s, 打印字母: %s" % (current_thread().name, chr(code)))


if __name__ == "__main__":
    t1 = Thread(target=print_number)
    t2 = Thread(target=print_alpha)

    t1.start()
    t2.start()

    print("\t\t我是一个主线程: %s" % current_thread().name)



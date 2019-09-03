"""
    多线程传参, 传递可变数据类型参数
        多线程之间传参, 如果参数为可变数据类型的全局变量, 那么子线程可以更改全局变量的值;

    线程1: 把李雪追加进去, god_list通过参数传入
    线程2: 获取god_list的值, god_list通过参数传入
    主线程, 等待以上线程执行完毕后, 获取全局变量god_list的值, 并打印
"""
from threading import Thread, current_thread

god_list = ["肖战", "王一博"]


def add_element(g_list):
    g_list.append("李雪")
    print("{}, g_list的值:{}".format(current_thread().name, g_list))


def get_list(g_list):
    print("\t{}, g_list的值:{}".format(current_thread().name, g_list))


if __name__ == "__main__":
    t1 = Thread(target=add_element, args=(god_list, ))
    t1.start()
    t1.join()  # 阻塞, 阻塞主线程的执行, 直到t1线程执行完毕  ["肖战", "王一博", "李雪"]

    t2 = Thread(target=get_list, args=(god_list, ))
    t2.start()
    t2.join()  # ["肖战", "王一博",  "李雪"]

    print("主线程, god_list:{}".format(god_list))  # god_list: 全局变量  ["肖战", "王一博",  "李雪"]


















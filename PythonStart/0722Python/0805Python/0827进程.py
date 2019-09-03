# from multiprocessing import Process
import threading
from multiprocessing import Process,Queue
import random
# def func():
#     for i in range(1,101):
#         print(i)
#
# def funcc():
#     for i in range(65,91):
#         print(chr(i))
# if __name__ == "__main__":
#     f = Process(target=func)
#     f.start()
#     p = Process(target=funcc)
#     p.start()

# import time
# def save_number(q):  # 往队列存数据,参数为所操作的队列
#     for i in range(1,101):
#         q.put(i)
#         print("存储数据：{}".format(i))
#         time.sleep(random.random())
#
#
# def get_number(q):   # 从队列获取数据，参数为所操作的队列
#     while True:
#         print("\t从队列中取出的数据：{}".format(q.get())
#
# if __name__ == "__main__":
#
#     q = Queue()
#
#     p1 = Process(target=save_number,args=(q,)))
#     p2 = Process(target=get_number,args=(q,)))
#     p1.start()
#     p2.start()


# 进程池
from multiprocessing import Pool

"""
写一个函数，假装下载
    循环5次，每次下载完成20%，
    每次循环下载随机睡一会
创建一个列表，如下
    list = ["哪吒之魔童降世"，"喜洋","电锯","七宗罪","洋洋","熊出没"]
    创建一个进程池包含3个进程，让这3个进程下载
    以上列表中的所有电影

"""
# import time
# import random
# def down(movie):
#     for i in range(5):
#         print("电影：{}下载进度{}".format(movie,(i/4*100)))
#         time.sleep(random.random())
#     return movie
# def alert(movie):
#     print("恭喜{}下载完成了...".format(movie))
#
# if __name__ == "__main__":
#     list = ["哪吒之魔童降世","喜洋", "电锯", "七宗罪", "洋洋", "熊出没"]
#     p = Pool(3)
#     for movie in list:
#         p.apply_async(down,(movie,),callback=alert)
#     p.close()
#     p.join()


# def num():
# #     for i in range(1,101):
# #         print("当前线程名字：{}打印的数字为{}".format(threading.current_thread().name,i))
# #
# # def letter():
# #     for i in range(1,101):
# #         print("当前线程为：{}".format(threading.current_thread().name))
# #         print(chr(random.randint(65,90) or chr(random.randint(97,122))))
# #
# # print("当前线程为：{}".format(threading.current_thread().name))
# # t = threading.Thread(target=num)
# # tt = threading.Thread(target=letter)
# # t.start()
# # tt.start()
# # print("我是主线程")

from threading import Thread,current_thread,Lock
import time,random
# lock = Lock()
# ticket = 6  # 票的总数
#
# def sp():
#     while True:
#         global ticket
#         lock.acquire()  # 上锁
#         if ticket > 0:
#             time.sleep(random.random())
#             ticket -= 1
#             print("{}线程在售票,成功售票一张，余票{}".format(current_thread().name, ticket))
#             lock.release()  # 解锁
#         else:
#             print("票已售完")
#             lock.release()  # 解锁
#             break
#
# if __name__ == "__main__":
#     list = ["携程","飞猪","支付宝","微信","火车站窗口","12306"]
#     for i in range(4):
#         t = Thread(target=sp)
#         t.start()




# def addd():
    # while True:
    #     global i
    #     lock.acquire()
    #     if i< 20000000:
    #         i += 1
    #         print("{}线程在执行，i的值为{}".format(current_thread(), i))
    #         lock.release()
    #     else:
    #         print("结束")
    #         lock.release()
    #         break
#     global i
# #     for x in range(10000000):
# #         lock.acquire()
# #         i+=1
# #         lock.release()
# # i = 0
# # if __name__ == "__main__":
# #     # for i in range(2):
# #     #     t = Thread(target=addd)
# #     #     t.start()
# #     t1 = Thread(target=addd)
# #     t2 = Thread(target=addd)
# #     t1.start()
# #     t2.start()
# #
# #     t1.join()
# #     t2.join()
# #     print(i)



# def func_add(score):
#     score += 1
#     print("{},score的值：{}".format(current_thread().name,score))
#     return score
# def get_score(score):
#     print("{},获取的score的值是{}".format(current_thread(),score))
# score = 59
# if __name__ == "__main__":
#     t1 = Thread(target=func_add,args=(score,))
#     t2 = Thread(target=get_score,args=(score,))
#     t1.start()
#     t1.join()
#     t2.start()
#
#     t2.join()
#     print("主线程中全局变量为score：{}".format(score))


#
# def func_add(god_list):
#     god_list.append("李雪")
#     print("{},score的值：{}".format(current_thread().name,god_list))
# def get_score(god_list):
#     print("{},获取的score的值是{}".format(current_thread(),god_list))
# god_list = ["肖战","王一博"]
# if __name__ == "__main__":
#     t1 = Thread(target=func_add,args=(god_list,))
#     t2 = Thread(target=get_score,args=(god_list,))
#     t1.start()
#     t1.join()
#     t2.start()
#     t2.join()
#     print("主线程中全局变量为score：{}".format(god_list))



# 问题代码
#
# from multiprocessing import Queue
#
# def product(q,q_product):  # 参数1：生产消费所共同操作的队列 参数2：生产者要生产的数据
#     while not q_product.empty():    # 如果不为空，就执行下面代码
#         num = q_product.get()   #从队列中拿出将生产的数据
#         q.put(num)  # 将生产的数据放入队列中
#         print("生产者线程：{}，生产数据：{}".format(current_thread().name,i))
#         time.sleep(1)
# def customer(q): # 消费的数据从  队列中获取
#     while True:
#         res = q.get() # block = True 阻塞，直到获取到数据为止
#         print("消费者线程：{}，消费数据：{}".format(current_thread().name,res))
#
#
# if __name__ == "__main__":
#     q = Queue() # 全局变量
#     q_product = Queue()
#     for i in range(50):
#         q_product.put(i)
#     for i in range(3):
#         t1 = Thread(target=product,args=(q,))
#         t1.start()
#     for i in range(3):
#         t2 = Thread(target=customer,args=(q,))
#         t2.start()



# 问题代码

from threading import  Thread
person_dict = {}
class Person:

    def talkToAnimal(self):
        global person_dict
        p_ob = person_dict[current_thread()]
        print("与动物说的人事",p_ob.name,p_ob.age)
        p_ob.eat()
        p_ob.sleep()


def func(name,age):
    # 创建人嘞对象
    p = Person(name,age)
    global person_dict
    person_dict[current_thread()] = p   #key:当前线程对象
    talkToAnimal()


if __name__ == "__main__":
    t1 = Thread(target=func,args=("小花",20))
    t1.start()
    t2 = Thread(target=func,args=("小黄",18))
    t2.start()


def func():
    pass

def func1():
    pass





















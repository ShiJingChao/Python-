"""
    队列:
        可以设置队列的最大长度; 如果不设置, 默认没有长度, 存储多少数据都可以;

        q = Queue(指定队列的长度)

        q.put(obj, block=True, timeout)
                1. 默认block为True, 即阻塞式, 阻塞当前程序的执行, 直到将obj放入队列中为止
                2. 设置block为False, 非阻塞式, 队列满时, 立即抛出异常
                3. 设置timeout, 阻塞时间, 如果阻塞时间, 抛出异常
        q.get(block=True, timeout)
                1. 默认block为True, 即阻塞式, 阻塞当前程序的执行, 直到获取数据为止
                2. 设置block为False, 非阻塞式, 队列空时, 立即抛出异常
                3. 设置timeout, 阻塞时间, 如果阻塞时间, 抛出异常

        q.put_nowait(obj)  如果队列已满, 抛异常
        q.get_nowait()  如果队列为空, 抛异常

        q.full()  队列是否已满
        q.empty()  队列是否为空
        q.qsize()  获取当前队列的大小(队列中元素的个数)
"""
from multiprocessing import Queue


# 创建队列对象
q = Queue(3)  # 创建一个长度为3的队列

print(q.full())  # False 判断当前队列满了吗
print(q.empty())  # True 判断当前队列是不是空的

print(q.qsize())  # 0

q.put("李小花")
q.put("王二狗")
q.put("刘三胖")

print(q.full())   # True
print(q.qsize())  # 3

# q.put("史狗剩")  # 阻塞式的, 阻塞程序的执行, 直到将"史狗剩"放到队列中为止
# q.put("刘铁蛋", timeout=3)  # 阻塞式的, 阻塞时间为timeout, 如果超出阻塞时间, 抛出异常raise Full, 打断程序的执行
# q.put("赵铁柱", block=False)  # 如果设置block为False, 非阻塞式, 代表如果队列已满, 直接抛出异常

# q.put_nowait("隔壁老王")  # raise Full
print("---------------")

print(q.get())
print(q.get())
print(q.get())

print(q.qsize())  # 0
print(q.empty())  # True

# print(q.get())  # 阻塞式的, 阻塞程序的执行, 直到取出一个数据为止
# print(q.get(timeout=3))  # 阻塞时间为timeout, 超出阻塞时间, 直接抛出异常 raise Empty
# print(q.get(block=False))  # 非阻塞式的, 如果队列为空, 直接抛出异常

# print(q.get_nowait())  # raise Empty
print("================")









"""
    进程: 一个独立的正在执行的程序;
    线程: 进程中的多条执行路径;

    进程: 系统资源分配的最小单位;
    线程: cpu调度的最小单位; 实际上cpu调度的是进程中的线程

    threading 关于线程的模块
    执行demo, 由系统创建主进程, 在主进程中创建主线程, 执行以下代码;
"""
from threading import current_thread, currentThread   # 当前线程


print("你好, 我是主进程中的主线程...")
print(currentThread().name)  # 当前线程的名字  MainThread
print(current_thread().name)  # 当前线程的名字  MainThread













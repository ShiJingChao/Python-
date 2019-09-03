"""
    写一个函数, 假装下载
        循环5次, 每次下载完成20%,
        循环1次, 随机睡0.几秒

    创建一个列表,如下
    list = ["哪吒之魔童降世",
    "喜洋洋与灰太狼", "电锯惊魂",
    "七宗罪", "洋洋大冒险",
    "熊出没之熊熊乐园"]

    创建一个进程池包含3个进程,
    让这3个进程下载
    以上列表中的所有电影
    ----------------------------
    apply_async(func, (a, b, ...), callback) 异步执行
    apply() 同步执行

        第一个参数: 进程执行的任务
        第二个参数: 是个元组, 给第一个参数(函数),传递参数用的
        第三个参数: 进程执行完毕后的回调函数, 函数如果需要参数, 参数从第一个参数的返回值获取
"""
from multiprocessing import Pool
import time
import random


# 功能: 实现电影的下载
def download_movie(movie_name):

    for x in range(5):  # 0, 1, 2, 3, 4
        print("电影{}, 已下载{}%".format(movie_name, (x + 1) * 20))

    return movie_name  # 将电影的名字返回


# 回调: 显示某个电影下载完毕
def alter(name):
    print("\t{}下载完毕".format(name))


if __name__ == "__main__":

    p = Pool(3)  # 3个进程一块干活

    movies = ["哪吒之魔童降世", "喜洋洋与灰太狼", "电锯惊魂", "七宗罪", "洋洋大冒险", "熊出没之熊熊乐园"]

    for m in movies:  # 获取每个电影的名字
        p.apply_async(download_movie, (m, ), callback=alter)  # 如果该进程任务执行完毕, 回调alter函数

    p.close()
    p.join()
    print("----主进程----")







"""
    封装一个函数，可以使用mkdir的方法， 实现创建多级目录的功能
    os.mkdir()  创建一级目录
    os.makedirs()  创建多级目录

    D:/first_level/day14/a1/b1/c1/d1/e1
思路:
    D:/    从根盘符开始, 这个根目录肯定是存在的
    D:/first_level   判断跟盘符下的第1个路径, 如果不存在, 创建; 如果存在, 继续往下判断;
    D:/first_level/day14  判断跟盘符下的第2个路径,  如果不存在, 创建; 如果存在, 继续往下判断;
    D:/first_level/day14/a1  判断跟盘符下的第3个路径,  如果不存在, 创建; 如果存在, 继续往下判断;
    .....

-------------- split ---------
    D:   first_level    day14   a1   b1   c1    d1    e1

"""
import os


def my_makedirs(path):  # path: 所创建的多级目录
    path_list = path.split("/")  # [D:, first_level, day14, a1, b1, c1, d1, e1]

    for this_path in path_list:

        if not os.path.exists(this_path):  # D:   first_level
            os.mkdir(this_path)

        print(os.getcwd())  # 当前路径
        os.chdir(this_path + "/")  # 切换到D:\没成功 --> 此时还是当前路径


my_makedirs("D:/first_level/day14/a1/b1/c1/d1/e1")




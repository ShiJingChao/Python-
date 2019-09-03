"""
6. 用户输入文件名以及开始搜索的路径，
搜索该文件是否存在，如遇到文件夹，则进入文件夹继续搜索
"""
import os


def func(s_file, path):   # 参数1: 被搜索的文件 参数2: 搜索的目录 D:/first_level/day14/a/b
    file_list = os.listdir(path)  # 将该目录下的所有文件/文件夹 获取到

    for file in file_list:  # 遍历列表, 获取列表中的每个文件  a, b, c.txt
        file_abs_path = path + "/" + file  # 获取每个文件的绝对路 "D:/first_level/day14/a/b/c.txt"

        if os.path.isdir(file_abs_path):  # 判断该文件是否是一个目录  D:/first_level/day14/a/b/c.txt
            res = func(s_file, file_abs_path)  # 递归调用自己
            if res == True:
                return True

        elif file == s_file:  # 判断遍历出的文件 是否就是 被搜索的文件
            return True

    return False


r = func("c.txt", "D:/first_level/day14")
print(r)

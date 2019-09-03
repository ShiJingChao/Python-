"""
    给定一个目录,
    列举出这个目录中的所有文件和文件夹,
        以及子文件夹中的所有文件...

"""
import os



def func(path, f):   # 参数为给定的目录  a
    file_list = os.listdir(path)  # 获取给定目录中的所有(文件, 文件夹)

    for file in file_list:  # 遍历列表, 获取其中的每个(文件, 文件夹)
        file_path = path + "/" + file  # D:/first_level/day14/a/b/c
        if os.path.isfile(file_path):  # b
            print("[文件]: ", file)
            f.write("[文件]: %s\n" % file)

        elif os.path.isdir(file_path):  # 此时该文件是个目录
            print("[目录]:", file)
            f.write("[目录]: %s\n" % file)
            func(file_path, f)  # 路径: 绝对路径  file就只是个文件名


f = open("ufile.txt", "a")  # 在递归中操作同一个文件时, 尽量把文件的打开和关闭放在函数外,避免在递归中多次打开;
func(r'D:/first_level/day14', f)
f.close()

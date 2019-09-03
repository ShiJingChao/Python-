import os
import datetime
from os import path

# file = open("D:\\songs\\1.txt", 'w', encoding='utf-8')  # open("路径名文件名","权限","转码")注意，路径名必须是已有目录，没有则会失败
# file.write("你是谁")
# file.close()

# print(os.listdir("D:"))     # 显示目录下的所有文件

# # os.mkdir("D:\\11")          # 如果目录有多级，则创建最后一级。如果最后一级目录的上级目录有不存在的，则会抛出一个OSError。也就是说只能创建单层目录
# os.makedirs("D:\\11\\22\\33")  # 用来创建目录树，如果子目录创建失败或者已经存在，会抛出一个OSError的异常，
# # Windows上Error 183即为目录已经存在的异常错误。如果path只有一级，与mkdir一样。
# path = "D:\\11\\22\\33\\"
# # file = open(path + (datetime.datetime.now().strftime("%Y-%m-%d") + ".txt"), 'w',
# #             encoding='utf-8')
# file = open(path + (datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".txt"), 'w',
#             encoding='utf-8')
# os.rmdir("D:\\11")      # rmdir()只能删除空目录，如果目录下有文件夹或者目录，会报错,如果不存在要删除的目录，也会报错


# print(os.getcwd())  # 获取当前目录,和创建目录没有关系，就是当前项目的存在目录
#
# os.chdir("D:\\songs")   # 改变当前工作目录，再创建文件和目录（不写路径的情况下，只写目录或者文件）都会在改变后的目录下创建,如果目录不存在，则报错
# print(os.getcwd())
# file = open("1.txt", 'w', encoding='utf-8')
# file.write("HELLO")
#
# print(path.isdir(""))    # 判断是否为文件夹，是返回True，不是返回False，文件不存在返回false


# Python 读取文件时同时输出行号与行内容。

# file = open("README1.txt", "r", encoding='utf-8')
# for num, value in enumerate(file,1):          # 读取文件的行数和内容    如果文件过大，则不适宜用enumerate方法
#     print("行号:%s,内容：%s" % (num, value))
# file.close()

# 遍历一个文件下所有文件的后缀名

# import os
#
# file = "C:\\Users\\Administrator\\ban"
# f = os.listdir(file)
# count = 0
# for i in f:
#     if os.path.splitext(i)[1] == '.txt':
#         count += 1
# print(count)

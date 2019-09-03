# class 449
#
# # 1.文件打开
# file = open('README1.txt', 'r', encoding='utf-8')
# # 2.读取文件内容
# text = file.read()
# print(text)
#
# # 3.关闭文件
# file.close()
# -----------------------------------------------------------------
# class 450


# # 1.文件打开
# file = open('README1.txt', 'r', encoding='utf-8')
# # 2.读取文件内容
# text = file.read()
# print(text)
# print(len(text))    # 读取到文件内容长度为38
# print("-"*60)
#
#
# read 方法后会移动指针到读取内容的末尾，
# 再调用read方法 就不会读到任何的内容
# text = file.read()
# print(text)         # 不会输出任何内容
# print(len(text))    # 读取到文件内容长度为0
# # 3.关闭文件
# file.close()
# --------------------------------------------------------------------
# class 451
# 写入文件
#
# 1.打开
# file = open("README1.txt", 'a', encoding='utf-8')   # 以追加方式打开文件，如果该文件已存在，文件指针会放在文件的末尾，
#                                                     # 如果文件不存在，则创建新文件进行写入
# file = open("README1.txt", 'w', encoding='utf-8')   # 如果文件存在  写入的内容会覆盖之前的内容，没有则创建文件并写入
#
# 2.写入文件
# file.write("hello")
#
# 3.关闭
# file.close()

# ------------------------------------------------------------
# class 452

# 按行读取文件内容
# read方法默认会把文件的所有内容一次性读取到内存
# 如果文件太大，对内存的占用会非常严重
#
# readline
# readlinre方法可以一次读取一行内容
# 方法执行后，会把文件指针移动到下一行，准备再次读取
#
# 读取大文件的正确姿势
import linecache
import os
import random

# file = open("README1.txt", 'r', encoding='utf-8')
# text = linecache.getline('README1.txt', random.randint(1, ))  # 读取文件的指定行
# print(text)
# while True:
#     # 读取一行内容
#     text = file.readline()
#
#     # 判断是否读取到内容,内容为空，跳出循环
#     if not text:
#         break
#
#     # 每读取一行的末尾已经有了一个'\n'
#     print(text, end="")
#
# # 关闭文件
# file.close()

# -----------------------------------------------------------------------

# class 453 文件复制

# 小文件的复制，读取完整内容，并写入到另一个文件中

# 1.打开文件
# file_read = open("README1.txt", "r", encoding='utf-8')
# file_write = open("README2.txt", "w", encoding='utf-8')
#
# # 2.读写
# text = file_read.read()
# file_write.write(text)
# # 3.关闭
# file_read.close()
# file_write.close()

# -----------------------------------------------------------------------------
# class 454   大文件的复制

# 1.打开文件
# file_read = open("README1.txt", "r", encoding='utf-8')
# file_write = open("README3.txt", "w", encoding='utf-8')
#
# # 2.读写
# while True:
#     text = file_read.readline()
#
#     #判断是否读取到内容
#     if not text:
#         break
#
#     file_write.write(text)
# # 3.关闭
# file_read.close()
# file_write.close()

# ------------------------------------------------------------
# class 455 文件/目录的常用管理操作
#
# import os
#
# os.rename("README3.txt", "README4.TXT")     # 重命名
#
# os.remove("README4.txt")    #删除文件README4.txt，如果文件不存在则报错
#
# print(os.listdir("."))      #查看某一个目录下的内容，. 表示当前目录
#
# print(os.path.isdir("README1.txt"))   #判断传入的参数是不是一个目录，如果是则返回True，不是则返回False
#
# os.mkdir("test")    # 创建目录 如果文件名存在，则报错
#
# os.rmdir("test")    #删除目录   如果目录不存在则报错

# ----------------------------------------------------------------------

# class 456   文本文件的编码格式
#

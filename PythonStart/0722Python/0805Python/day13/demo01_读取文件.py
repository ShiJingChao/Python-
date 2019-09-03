"""
    读取文件:
        1. 打开文件
            相对路径: 参照物(以当前工作文件路径为参照物), 例如: dragon.txt
            绝对路径: 从根盘符开始的路径; 例如:D:\first_level\day13\dragon.txt
        2. 读取文件
        3. 关闭文件

    转义字符:
        改变字符原有的意义; \n --> 换行符
        r: 原始字符串, 使当前字符串中的每个字符保留其原有的意义;

    -----------------------
    绝对路径:
        D:\first_level\day13\dragon.txt
        D:\first_level\day13\demo01_读取文件.py

        D:\first_level\message.txt
    相对路径:
        ..\message.txt   # .. 代表上一层目录


        D:\first_level\day13\inner\pizza.txt
    相对路径:
        .\inner\pizza.txt  # .代表当前目录


"""

# 打开文件, 文件的路径 文件句柄对象
# f = open(r"D:\first_level\day13\dragon.txt")
# f = open("dragon.txt")
# f = open(r"D:\first_level\day13\inner\pizza.txt")
# f = open(r".\inner\pizza.txt")
# f = open(r"D:\first_level\message.txt")
f = open("..\message.txt")

# 读取数据
print(f.read())

# 关闭文件
f.close()



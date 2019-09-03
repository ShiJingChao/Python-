"""
    1. 让用户输入一个目录
    2. 判断用户输入的是否是一个目录
        2.1 切换到用户所输入的目录中去
        2.2 获取当前目录, 并显示当前目录下的所有文件
            再分别显示每个文件是 文件 或者是 目录?
    3. 显示功能, 让用户选择, 并执行
        1. 添加前缀
        2. 删除前缀
        3. 创建文件
        4. 删除文件
        5. 重命名文件
"""
import os


def func():
    dir = input("请输入一个目录:")

    if os.path.isdir(dir):
        os.chdir(dir)  # 切换到指定目录 --> day14
        file_list = os.listdir(dir)  # 获取指定路径下的所有文件, 并返回一个列表
        # ["hw01.py", "hw02.py", "test.py", "uabc.txt",...]
        for file in file_list:  # 遍历获取列表中的每一个文件
            if os.path.isdir(file):  # 该文件的相对路径
                print("[目录]: %s" % file)
            elif os.path.isfile(file):
                print("[文件]: %s" % file)

        choice = input("---1,添加前缀;2,删除前缀;3,创建文件;4,删除文件;5,重命名文件---")
        if choice == "1":
            res = input("请输入所修改的文件和前缀, 中间以空格分开:")  # 'hw01.py m'
            name_list = res.split(" ")  # 0 文件名 1 前缀
            if name_list[0] in file_list:   # 判断该文件是否存在
                os.rename(name_list[0], name_list[1] + name_list[0])
                print("文件添加前缀成功!!!")
            else:
                print("该文件不存在, 无法改名")

        elif choice == "2":
            res = input("请输入所删除前缀的文件和前缀, 中间以空格分开:")
            name_list = res.split(" ")
            if name_list[0] in file_list:  # utext.py --> test.py
                os.rename(name_list[0], name_list[0].replace(name_list[1], "", 1))
                print("文件删除前缀成功!")
            else:
                print("该文件不存在")

        elif choice == "3":  # 创建文件
            file_name = input("请输入要创建的文件名:")
            if not os.path.exists(file_name):
                with open(file_name, "w") as f:
                    pass
                print("文件创建成功")
            else:
                print("该文件已存在")

        elif choice == "4":  # 删除文件
            file_name = input("请输入要删除的文件名:")
            if os.path.exists(file_name):
                os.remove(file_name)  # 如果文件存在, 那么删除
                print("已成功删除该文件")
            else:
                print("该文件不存在")

        elif choice == "5":  # 重命名
            res = input("请输入原文件和新文件名, 中间以空格分开:")
            name_list = res.split(" ")  # 0--> 原文件名, 1 --> 新文件名
            if name_list[0] in file_list:
                os.rename(name_list[0], name_list[1])
                print("文件重命名成功~")
            else:
                print("该文件不存在, 无法重命名...")
        else:
            print("--输入错误--")
    else:
        print("您输入的不是一个目录, %s" % dir)


func()



















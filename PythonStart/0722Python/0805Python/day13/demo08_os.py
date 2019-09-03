"""
    文件: a.txt, a.exe, a.doc, a.mp3, a.wmv
    目录: 文件夹

    os模块:
        1. 重命名
            os.rename() 只能够更改当前文件的名字
            os.renames() 可以更改上层目录, 如果上层目录不存在, 就会创建
        2. 删除文件
            os.remove() 用于删除指定路径的文件, 如果指定的路径是个目录, 报错;
        3. 创建目录
            os.mkdir() 创建目录, 如果目录已存在, 会报错;
                        只能用于创建一级目录, 创建多级目录就会报错;
            os.makedirs() 能够创建多级目录, 如果目录已存在, 会报错;
                        如果设置exist_ok=True, 目录已存在,就不会报错;
        4. 删除目录
            os.rmdir() 删除一级目录, 如果目录不存在, 报错
            os.removedirs() 删除多级目录, 若目录为空, 则删除, 直到某个目录不为空为止;

        5. 获取当前所在目录
            os.getcwd()

        6. 获取目录列表
            os.listdir()

        7. 切换所在目录
            os.chdir()

        8. 判断文件是否存在
            os.path.exists()

        9. 判断是否为文件, 目录
            os.path.isfile()
            os.path.isdir()

        10. 判断是否为绝对路径
            os.path.abs()

        11. 获取路径中的最后部分(文件名)
            os.path.basename()

        12. 获取路径中的路径部分(文件名前的所有路径)
            os.path.dirname()
"""
import os

# 重命名
# os.rename(r".\four.txt", "ffff.txt")
# os.rename(r"D:\a\b\c.txt", r"D:\a\b\cc.txt")
# os.rename(r"D:\a\b\cc.txt", r"D:\a\e\c.txt")  # FileNotFoundError:
# os.renames(r"D:\a\b\cc.txt", r"D:\a\e\c.txt")

# 删除文件
# os.remove(r"D:\a\e\c.txt")
# os.remove(r"D:\a\e")  # PermissionError:

# 创建一级目录
# os.mkdir(r'D:\a\e\f')

# 创建多级目录
# os.makedirs(r"D:\a\e\f\g\h\i", exist_ok=True)

# 删除一级目录
# os.rmdir(r"D:\a\e\f\g\h\i")

# 删除多级目录
# os.removedirs(r"D:\a\e\f\g\h")

# 获取当前所在目录
# print(os.getcwd())  # D:\first_level\day13

# 获取目录列表
# res = os.listdir(os.getcwd())
# print(res)   # 获取当前目录的列表

# 切换所在目录
# os.chdir(r'..\\')  # 相对当前路径; .当前路径; ..上一层路径;
# print(os.getcwd())  # D:\first_level

# 判断某个文件是否存在
# b1 = os.path.exists(r'D:\first_level\day13\ffff.txt')  # True
# b2 = os.path.exists(r'D:\first_level\day13\abcd.txt')  # False
# print(b1, b2)

# 判断是否为文件
# b3 = os.path.isfile("ry6.jpeg")  # True
# b4 = os.path.isfile("inner")  # False
# print(b3, b4)

# 判断是否为目录
# b5 = os.path.isdir("ry6.jpeg")  # False
# b6 = os.path.isdir("inner")  # True
# print(b5, b6)

# 判断是否为绝对路径
# b7 = os.path.isabs(r"D:\aa.txt")   # True
# b8 = os.path.isabs(r".\ry7.jpeg")   # False
# print(b7, b8)


# 获取最后部分(文件名部分)
# os.getcwd() 获取当前的工作目录: D:\first_level\day13
print(os.path.basename(os.getcwd()))  # day13

# 获取路径部分
# os.getcwd() 获取当前的工作目录: D:\first_level\day13
print(os.path.dirname(os.getcwd()))  # D:\first_level

# __file__ 获取当前文件的路径  D:/first_level/day13/demo08_os.py
# get_cwd() 获取当前文件的目录  D:/first_level/day13

print(__file__)




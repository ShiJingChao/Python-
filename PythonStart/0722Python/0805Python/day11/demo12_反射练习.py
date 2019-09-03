import my_util
import sys

# 反射函数获取一下 dragon
d = getattr(my_util, "dragon")
print(d)  # 权志龙

func = getattr(my_util, "func")
print(func) # <function func at 0x0000000001E790D8>
func()  # 你嫉妒也没用,人家就是比你帅!!!帅到没朋友

name = "水原希子"


def friend():
    print("漂亮的姑娘你看过来~~~")


print(sys.modules)  #  python中所有加载到内存中的模块  字典 ---> key --> __main__
name1 = getattr(sys.modules["__main__"], "name")
print(name1)


# 获取内置模块中的变量 --> 与获取导入模块中的方法一样
import time
print(getattr(time, "time"))



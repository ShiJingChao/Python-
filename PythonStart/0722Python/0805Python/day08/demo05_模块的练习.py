# import my_demo   # 导入的是import后边的东西
#
# r = my_demo.get_sum(10, 20, 30, 40)
# print(r)  # 100
#
# print(my_demo.g_num)  # 100
# print(my_demo.g_list)  # []

# from my_demo import get_sum

# print(get_sum(20, 20))
# 报错 print(g_num)
# 报错 print(my_demo.g_num)

# from my_demo import *
#
# print(g_list)
# print(g_num)
# print(get_sum(10, 20, 30, 40, 50))

# import my_demo  # 模块导入会将被导入的文件执行一遍
# from my_demo import *
# from my_demo import g_num

# 模块的搜索路径
import sys

print(sys.path)

"""
[
'D:\\first_level\\day08', 
'D:\\first_level\\day08', 
'C:\\py37\\python37.zip', 
'C:\\py37\\DLLs', 
'C:\\py37\\lib', 
'C:\\py37', 
'C:\\py37\\lib\\site-packages', 
'C:\\Program Files\\JetBrains\\PyCharm 2018.2\\helpers\\pycharm_matplotlib_backend'
]
"""

from my_demo import *  # 一次性将my_demo中所有的变量,函数,类

print(g_list)
print(g_num)
# print(_money)  # NameError: name '_money' is not defined

print(_money)


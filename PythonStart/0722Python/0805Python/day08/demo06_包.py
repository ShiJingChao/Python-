"""
    包:
        特点:
            python包文件中必须有一个__init__.py文件

        一个文件夹,在这个文件夹中可能存在多个.py文件;
        一个包里可以有很多模块;

        导入包中的模块(如果包在当前路径下):
            1. import 包名.模块名
                    [使用]: 包名.模块名.函数名()

            2. from 包名 import 模块名
               from 包名.模块名 import 函数名

            3. from 包名 import *
                前提: __init__.py 需要在该文件给__all__属性赋值, 赋值内容为允许导入的模块
                        __all__的类型为列表, 列表中的元素为字符串元素
                        __all__ = ["模块名", "demo2", "test_demo"]
"""
# 导入test_demo.py
# 1. import
# import test_demo 找不着
# import test.test_demo as a
#
# print(a.g_list)
# print(test.test_demo.g_num)

# 2. from
# from test import test_demo
# print(test_demo.g_list)

# from test.test_demo import g_list
# print(g_list)

# from test import test_demo.g_list 错误
# from test.test_demo.g_list 错误

# 3. from 包 import *
from test import *

print(test_demo.g_list)
print(demo2.two_num)


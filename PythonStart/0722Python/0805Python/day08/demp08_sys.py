"""
    sys:
        定义的是一些和系统相关信息的模块

        sys.path : 获取搜索模块的路径
        sys.version : 获取版本号

"""
import sys

print(sys.path)
print(sys.version)  # 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)]

print(sys.argv)  # 用于接收命令行下的参数 ['D:/first_level/day08/demp08_sys.py']

# 在命令行中输入 python D:\first_level\day08\demp08_sys.py 李小花 17 girl
# 执行的结果 ['D:\\first_level\\day08\\demp08_sys.py', '李小花', '17', 'girl']

print(sys.version_info)  # sys.version_info(major=3, minor=7, micro=4, releaselevel='final', serial=0)



"""
    dir()
        查看对象的所有方法;
    help()
        查看某个函数的使用方法, 说明文档;
"""

print(dir(str))  # 查看字符串的所有方法
print(help(str.isdigit))  # 查看isdigit函数的说明文档

# isdigit()
'abc'.isdigit()
a = 128
# a.isdigit() 错误, isdigit() 是字符串变量可以调用(使用)的方法

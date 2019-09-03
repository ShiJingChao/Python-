"""
1、定义一个函数func(filename) filename:文件的路径，
  函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误。
"""


def func(filename):
    try:
        f = open(filename)
        print(f.read())
        f.close()
    except Exception as e:  # 获取一下异常对象
        print("发生了异常, 异常的类型是:", type(e))
        print("异常的内容是, ", str(e))
    else:
        print("此时木有发生异常")
    finally:
        print("---over----")


func("abc.txt")











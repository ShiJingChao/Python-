"""
    程序员手动抛出异常:
        raise StopIteration
        raise 使用代码抛出异常的关键字

"""
# 接收用户输入的密码, 长度至少为8, 否则抛出异常
# 1. 输入
# 2. 判断长度
# 3. 不满足, 抛异常


def func():
    pw = input("请输入您的密码:")

    if len(pw) >= 8:
        print("密码设置成功")
    else:
        # 创建一个异常对象, 并抛出
        e = Exception("密码长度至少为8, 您的密码长度不够")
        raise e


func()








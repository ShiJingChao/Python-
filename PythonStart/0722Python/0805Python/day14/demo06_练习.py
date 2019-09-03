# 读取键盘输入的整数, 做除法操作, 除数是这个整数
# 没有异常, 程序执行结束
# 如果产生了异常, 再次重新输入

while True:
    try:
        num = input("请输入一个整数:")
        num = int(num)
        num = 689 / num
    except:
        continue   # 结束当前循环, 继续下一次循环
    else:
        print(num)
        break  # 结束循环, 跳出循环;








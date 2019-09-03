# 设计一段代码, 通过索引获取列表中的元素, 使其产生异常, 并捕获处理异常;


try:
    list1 = ["万启龙", "小黄龙", "小黑龙", "大花龙"]

    n = 0
    while n <= len(list1):  # n <= 4;  n = 0,1,2,3,4
        print(list1[n])
        n += 1

except IndexError:
    print("--索引越界了--")


print("-----over-----")






# 5 定义一个方法，把数组{1,2,3}按照指定个格式拼接成一个字符串。格式参照如下：[1#2#3]。
def pinjie(c):
    b = [i for i in c]
    s = ""
    for i in range(1, len(b)+2, 2):
        b.insert(i, "#")
    for i in b:
        ss = str(i)
        s += ss
    return s


a = pinjie({1, 2, 3})
print(a)

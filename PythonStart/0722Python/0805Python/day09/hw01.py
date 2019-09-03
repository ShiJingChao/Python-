import random, time, locale
"""
1.创建一个函数，输入一个大于1的整数，返回一个列表，
包含所有能够整除该整数的因子（不包含1和它本身），并且从小到大排序。
如果这个数是素数，则返回“(integer) is prime”。
  (1)使用普通函数
  (2)使用列表推导式
"""


def func(num):  # 参数为要输入的整数
    res_list = []
    for x in range(2, num):
        if num % x == 0:
            res_list.append(num)
    if res_list:
        return res_list
    else:
        return "%d is prime" % num


def func2(num):
    res_list = [x for x in range(2, num) if num % x == 0]
    return res_list if res_list else "%d is prime" % num
    # 真 if 条件 else 假

# 2.现在有一列表lst = [[1,2,3],[4,5,6],[7,8,9]]
# 要求使用列表推导式取出 1、4、7  和 1、5、9 元素，思考如何取出


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list1 = [x[0] for x in lst]
print(list1)

# 1 --> lst[0][0]
# 5 --> lst[1][1]
# 9 --> lst[2][2]

list2 = [lst[x][x] for x in range(len(lst))]
print(list2)


# 3 创建一个列表，长度为10。数据是1-100的随机数。

def func3():
    num_list = []
    for x in range(10):
        res = random.uniform(1, 100)
        num_list.append(res)
    return num_list


print(func3())


# 4. 创建一个列表，长度为10。数据是1-100内的随机偶数。
def func4():
    num_list = []
    for x in range(10):
        res = random.randrange(2, 101, 2)
        num_list.append(res)
    return num_list


print(func4())  # [42, 74, 30, 20, 80, 42, 70, 2, 78, 60]


# 打印当前的日期，按照指定的格式：
# 	格式:2017-11-27
# 	格式:2017-11-27 16:33:44
# 	格式:20:33:44
#   格式:2019年8月16日
# 分析: 字符串 <--- 获取当前的日期(时间元组) <---- time.localtime
t = time.localtime()

# 时间元组 --> 时间字符串
r1 = time.strftime("%Y-%m-%d", t)
r2 = time.strftime("%Y-%m-%d %H:%M:%S", t)
r3 = time.strftime("%H:%M:%S", t)
print(r1)
print(r2)
print(r3)

locale.setlocale(locale.LC_CTYPE, "chinese")
r4 = time.strftime("%Y年%m月%d日", t)
print(r4)  # 2019年08月16日

r5 = time.strftime("%Y{}%m{}%d{}", t).format("年", "月", "日")
print(r5)  # 2019年08月16日

# 5.让当前的程序睡眠5秒钟，再运行后面的代码
# time.sleep(5)


# 6.拼接一个字符串，长度为4。其实就是随机生成验证码
# 	内容是26个小写字母和26个大写字母。以及0-9数字。
def func5():
    res_str = ""
    for x in range(4):
        s = random.choice("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        res_str += s
    return res_str


print(func5())


# chr(), ord()  字符 <--> 编码  (utf-8)
def func6():
    res_str = ""  # 验证码的字符串
    while len(res_str) < 4:  # 条件 字符串的长度 < 4
        num = random.randrange(48, 123)
        if (num >= 48 and num <= 57) or (num >= 65 and num <= 90) or (num >= 97 and num <= 122):
            res_str += chr(num)  # 整数 --> 字符
    return res_str


print(func6())


def func7():
    list_num = [x for x in range(48, 58)]  # 48~57 --> 0-9
    list_big_alpha = [x for x in range(65, 91)]  # 65~90 ---> A-Z
    list_small_alpha = [x for x in range(97, 123)]  # 97~122 --> a~z

    res_list = list_num + list_big_alpha + list_small_alpha  # 满足验证码规则的所有字符对应的编码
    res_str = ""  # 验证码字符串
    for x in range(4):
        num = random.choice(res_list)  # 随机产生一个编码
        res_str += chr(num)  # 将编码转换成字符
    return res_str


print(func7())
# c = 0
# # while c <4:
# #     s = ''
# #     i = randint(0,122)
# #     if i  < 10:
# #         s += str(i)
# #         c+=1
# #     elif i in range(ord('a'),ord('z')+1) or i in range(ord('A'),ord('Z')+1):
# #         s +=chr(i)
# #         c+=1
# #     else:
# #         continue
# #     print(s,end='')

# 7.创建一个列表，长度为10，数据是1-10的随机数。要求去重复。


def func8():
    res_list = []
    for x in range(10):
        num = random.randint(1, 10)
        res_list.append(num)
    return set(res_list)


print(func8())


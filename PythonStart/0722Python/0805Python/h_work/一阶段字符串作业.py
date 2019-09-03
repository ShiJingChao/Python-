# 1.判断一个数是否是回文数。例如：输入：121，输出也是121，像这样的数就是回文数
# num = input('>>>')
# if num == num[::-1]:
#     print('True')
# else:
#     print('False')
# 2.查找字符串中每个字符最后出现的位置。

# text = "东边来了个喇嘛，西边来了个哑巴，" \
#        "喇嘛手里拎着五斤挞嘛，哑巴腰里别着个喇叭，" \
#        "别着喇叭的要用喇叭换手里拎着挞嘛的哑巴的挞嘛，" \
#        "拎着挞嘛的哑巴不愿意用挞嘛换手里拎着喇叭的喇嘛的喇叭。" \
#        "拎着喇叭的喇嘛用喇叭打了拎着挞嘛的哑巴，" \
#        "拎着挞嘛的哑巴也用挞嘛打了拎着喇叭的喇嘛。"
#
# for index,char in enumerate(text):
#     if index == text.rindex(char):
#         print(index,char,end=" ")

# 3.‘2018-11-12’去掉‘-’输出

# s = '2018-11-12'
# s2 = s.replace('-','')
# print(s2)

# 3.编写一个函数，接收传入的字符串，统计大写字母的个数、小写字母的个数、数字的个数、
# 其它字符的个数，并以元组的方式返回这些数，然后调用该函数。

def deal_char(li):
    list = []

    upper = 0
    lower = 0
    num = 0
    other = 0
    for i in range(li.__len__()):
        if li[i].isupper():
            upper += 1
        elif li[i].islower():
            lower += 1
        elif li[i].isnumeric():
            num += 1
        else:
            other += 1
    list.append(upper)
    list.append(lower)
    list.append(num)
    list.append(other)

    print("list:", list)
    return tuple(list)


ll = input("please input some char(or a string):", )
deal = deal_char(ll)
print(deal)
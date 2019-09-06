# sum = 0
# for i in range(2,101,2):
#     sum += i
# print(sum)
#
# s = "凉凉"
# print(s*10)

# for i in range(-5,-1):
#     print(i)

# for i in range(5,1):
#     print(i)         # 没有输出，因为没有交集


# cla1 = ['丁浩','老胡']
# cla2 = ['甲','乙','丙','丁']
#
# cla2.extend(cla1)
# cla2.insert(0,"晓慧")
# cla2.remove("丁")
# # 丁浩的下标：4
# print(cla2.index("丁浩"))
# cla2.insert(cla2.index("老胡"),"班长")
# print(cla2)

# ls = ["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", "综合", "综合",\
#       "师范", "理工", "综合", "理工", "综合", "综合", "综合", "综合", "综合","理工",\
#       "理工", "理工", "理工", "师范", "综合", "农林", "理工", "综合", "理工", "理工", \
#       "理工", "综合", "理工", "综合", "综合", "理工", "农林", "民族", "军事"]
#
# dict1 = {}
# for i in ls:
#     dict1[i] = dict1.get(i,0)+1
#
# print(dict1)

# s = set(ls)
# print(s)
# for i in s:
#     print(i,ls.count(i))

# b = (20,1,3,4,8,9,5,6)
# dic = {}
# ma = 0
# ma_i = 0
# mi = 0
# mi_i = 0
# for k,v in enumerate(b):
#     dic[k] = v
# ma = max(dic.values())
# mi = min(dic.values())
# for k,v in dic.items():
#     if v == ma:
#         ma_i = k
#     if v == mi:
#         mi_i = k
# print("最大值为：{}，下标为{}\n最小值为：{}，下标为：{}".format(ma,ma_i,mi,mi_i))
print("\"")
print(r"")
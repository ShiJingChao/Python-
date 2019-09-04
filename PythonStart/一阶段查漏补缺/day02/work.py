"""
Question 1
将价格大于100元的股票构造一个新的字典
"""


# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# prices_new = {}
# for k,v in prices.items():
#     if v>100:
#         prices_new[k] = v
#     else:
#         continue
# print(prices_new)

"""
有列表：
names = ['关羽', '张飞', '赵云']
courses = ['语文', '数学']
分别录入3名学生2门课程的成绩。
（1）最终用嵌套列表存储。
#最终效果：
list1=[[100,89],[79,89],[70,80]]
（2）用字典存储
效果：
dict1={
    "关羽":{"语文":100,"数学":89},
    "张飞":{"语文":79,"数学":89},
    "赵云":{"语文":70,"数学":80}
}
"""
# names = ['关羽', '张飞', '赵云']
# courses = ['语文', '数学']
# score = []
# l_score = []
# while True:
#     for i in names:
#         for j in courses:
#             if courses.index(j)== 0:
#                 print("请输入{}的{}成绩：".format(i,j))
#                 chinese = input()
#                 l_score.append(chinese)
#             elif courses.index(j) == 1:
#                 print("请输入{}的{}成绩：".format(i, j))
#                 math = input()
#                 l_score.append(math)
#                 ll_score = l_score.copy()
#                 score.append(ll_score)
#                 l_score.clear()
#     break
# print(score)


# 字典
# names = ['关羽', '张飞', '赵云']
# courses = ['语文', '数学']
# dict1 = {}
# dict2 = {}
# for i in names:
#     for j in courses:
#         if courses.index(j) == 0:
#             print("请输入{}的{}成绩：".format(i, j))
#             chinese = input()
#             dict2[j] = chinese
#         elif courses.index(j) == 1:
#             print("请输入{}的{}成绩：".format(i, j))
#             math = input()
#             dict2[j] = math
#             dict1[i] = dict2
#             dict2 = {}
# print(dict1)


"""
3、对列表list1按照语文成绩排序。
list1=[{"语文":100,"数学":89,"英语":90},
       {"语文":70,"数学":80,"英语":93},
       {"语文":85,"数学":87,"英语":94}]

效果：[{'语文': 70, '数学': 80, '英语': 93}, {'语文': 85, '数学': 87, '英语': 94}, {'语文': 100, '数学': 89, '英语': 90}]

"""
list1=[{"语文":100,"数学":89,"英语":90},
       {"语文":70,"数学":80,"英语":93},
       {"语文":85,"数学":87,"英语":94}]

list2 = sorted(list1,key=lambda x:x["语文"])
print(list2)




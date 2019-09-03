# 不可变数据类型和可变数据类型自加的区别
# 1. 判断gl_num和gl_list的值
# def demo(num, num_list):
#     num += num
#     num_list += num_list
#
#     print(num)
#     print(num_list)
#
#     print("函数完成")
#
#
# gl_num = 9
# gl_list = [1, 2, 3]
# demo(gl_num, gl_list)
# print(gl_num)
# print(gl_list)

"""
18
[1,2,3,1,2,3]
函数完成
9
[1,2,3,1,2,3]
"""

# 传值和传址问题

# 2.请说出 list1,list2,list3 的值是什么，并且说明为什么
# def extendlist(val, lis=[]):
#     lis.append(val)
#     return lis
#
#
# list1 = extendlist(10)
#
# list2 = extendlist(123, [])
#
# list3 = extendlist('a')
#
# print(list1)
#
# print(list2)
#
# print(list3)

"""
[10,‘a’]
[123]
[10,'a']
因为python执行程序是从上到下依次执行（遇到函数和类跳过），
list1调用函数只给val传了参数，第二个会使用默认的参数，所以lis里存放了10，
list2 给lis参数传递了一个空列表，所以将123存放在这个空列表中返回
list3,又没有给lis传参，所以‘a’也存放在了之前存10的列表中进行返回
打印的时候，所以list1和list3都是[10,'a'],list2是[123]
"""
# 匿名函数

# 3.请说出acts[0](2)的值，并且说明为什么
# def makeActions():
#     acts = []
#     for i in range(5):
#         acts.append(lambda x: i ** x)
#     return acts
#
#
# acts = makeActions()
# print(acts[0](2))
# print(acts[1](2))
# print(acts[2](2))
# print(acts[3](2))
# print(acts[4](2))
"""
16
16
16
16
16
调用函数，会把函数执行完毕返回，
列表中存的每个数据都是一个匿名函数，
也就是说acts[0],acts[1],acts[2],acts[3],acts[4]存储的都是lambda函数
后面的（）为x的值，因为函数执行完了，所以i的值为4，所以结果都是4的平方
"""
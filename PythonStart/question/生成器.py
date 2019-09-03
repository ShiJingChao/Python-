#
# def g():
#     print('a')
#     count = yield 1
#     print("--->",count)
#     print("b")
#     yield 2
# gm = g()
# next(gm)
# re2 = gm.send("123")
# print(re2)
#
# def odd():
#     n=1
#     while True:
#         yield n
#         n+=2
# odd_num = odd()
# count = 0
# for o in odd_num:
#     if count >=5: break
#     print(o)
#     count +=1

# def gen():
#     value=0
#     while True:
#         receive=yield value
#         if receive=='e':
#             break
#         value = 'got: %s' % receive
#
# g=gen()
# print(g.send(None))
# print(g.send('aaa'))
# print(g.send(3))
# print(g.send('e'))
# 执行流程：
#
# 通过g.send(None)或者next(g)可以启动生成器函数，并执行到第一个yield语句结束的位置。
# 此时，执行完了yield语句，但是没有给receive赋值。
# yield value会输出初始值0
# 注意：在启动生成器函数时只能send(None),如果试图输入其它的值都会得到错误提示信息。
# 通过g.send('aaa')，会传入aaa，并赋值给receive，然后计算出value的值，并回到while头部，执行yield value语句有停止。
# 此时yield value会输出"got: aaa"，然后挂起。
# 通过g.send(3)，会重复第2步，最后输出结果为"got: 3"
# 当我们g.send('e')时，程序会执行break然后推出循环，最后整个函数执行完毕，所以会得到StopIteration异常。
# 最后的执行结果如下：
#0
# got: aaa
# got: 3
# Traceback (most recent call last):
# File "h.py", line 14, in <module>
#   print(g.send('e'))
# StopIteration




#二分 查找

def erfen(alist,num):
    """

    :param alist:在哪个列表中查找
    :param data:查找一个数值是否在alist中
    :return:True or False，True表示找到了
    """
    n = len(alist)
    if n<1:
        print("111")
    else:
        mid = n//2
        if alist[mid]>num:
            zuolist = alist[:mid]
            erfen(zuolist,num)
        elif alist[mid]<num:
            youlist = alist[mid+1:]
            erfen(youlist,num)
        else:
            print("找到了")


alist = [1,2,3,4,5,6,7,8,9]
erfen(alist,7)








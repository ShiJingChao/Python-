# 1 While循环打印99乘法表
# i = 1
# while i< 10:
#     j = 1
#     while j <i+1:
#         print("{}*{}={}".format(j,i,j*i),end=" ")
#         j+=1
#     i+=1
#     print()

# 2 递归 斐波那契数列
# def FeiBo(n):
#     if n == 1 or n == 2:
#         num = 1
#         return num
#     else:
#         return FeiBo(n-1)+FeiBo(n-2)
#
#
# f = FeiBo(6)
# print(f)

# 3 将lis = [1,3,26,7,-5,7]绝对值从小到大排序

# lis = [1,3,26,7,-5,7]
# print(sorted(lis,key=abs))

# 4 使用递归求1到100 内的偶数和


# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return sum(n-1)+n
#
# s = sum(100)
# print(s)


# 5 将dic={‘a’:12,’b’:24,}中的键值互换

# dic={"a":12,'b':24,}
# dicc = {v:k for k,v in dic.items()}
# print(dicc)


# 6 A = {1,2,3,4,5}
# B = {4,5,6,7,8}
# 取集合ab的交集
# 						并集
# 						反交集


# A = {1,2,3,4,5}
# B = {4,5,6,7,8}
#
# print(A&B)
# print(A|B)
# print(A^B)



# 7 实现一个单例模式

# class Person:
#     __obj = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__obj is None:
#             cls.__obj = object.__new__(cls)
#         return cls.__obj
# p1 = Person()
# p2 = Person()
# print(p1)
# print(p2)


# 8 删除‘hello world’中的‘l’

# s = "hello word"
# s1 = s.replace("l","")
# print(s1)
# for i in range(len(s)):
#
# print(s)

# 11用 * 打印菱形

# def lingxing(n):
#     for i in range(1,n):
#         s = str((2*i-1)*"*")
#         print(s.center(2*n-1))
#     for i in range(n-1,0,-1):
#         s = str((2*i-1)*"*")
#         print(s.center(2*n-1))
# l = lingxing(5)

# 12 两种将十进制的‘10’转换为二进制的方法


# print(bin(10))
#
#
# s = []
# def n(m):
#     ss = ""
#     while True:
#         a = m%2
#         m = m//2
#         s.append(a)
#         if m == 0:
#             break
#     for i in s[-1::-1]:
#         ss += str(i)
#     print(ss)
# nn = n(10)

#12 代码的执行结果是什么

# def timefunc(func):
#     def inner(a,b):
#         print(a+b)
#         ret = func()
#         print('—inner—')
#         return ret
#     return inner
#
# @timefunc
# def func():
#     print('这是func函数')
#     return 'hello'
#
# ret = func(3,5)
# print(ret)

# 14创建一个只有一个元素的元祖

a = (1,)
print(type(a))
b = 1,
print(type(b))

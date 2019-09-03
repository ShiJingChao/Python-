# def func1():
#     print("你好，我是生成器")
#     yield
# g = func1()
# next(g)
#
# def func2():
#     for x in range(10):
#         yield  "猜猜我是第%d只龙" %x
# g2 = func2()
# print(next(g2))
# print(next(g2))
# next(g2)
# next(g2)
# # next(g2)
# print(next(g2))
#
# def func3():
#     print("生成器函数...")
#     d = yield "各位我去"
#     yield d
#
# g3 = func3()
# # next(g3)
# print(g3.__next__())
# print(g3.send("霸王龙"))
# # next(g3)
# #
# # next(g3)
# def func4():
#     sum = 0
#     count = 0
#     avg = 0
#     while True:
#         num = yield (sum,avg)
#         count +=1
#         sum += num
#         avg = sum/count
#
#
# g4 = func4()
# g4.__next__()
# print(g4.send(10))
# print(g4.send(5))
# print(g4.send(3))


# def fun5():
#     a = 1
#     b = 1
#     while True:
#         yield a
#         a,b = b,a+b
#
# g5 = fun5()
# for i in range(1,100):
#     print(next(g5))
# print("-"*30)
#
# class Func6:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end
#     def isPrimeNumber(self,num):
#         for x in range(2,num):
#             if num %x == 0:
#                 return False
#         return True
#     def __iter__(self):
#         for x in range(self.start,self.end+1):
#             if self.isPrimeNumber(x):
#                 yield x
#
# n = Func6(10,30)
# for x in n:
#     print(x)



def a(c):
    def b():
        print(1)
        t=c()
        return t
    print(2)
    return b()

@a
def co():
    print(999)
    return 888888888888888
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
oo=co
print(oo)

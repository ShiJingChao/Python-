# 1. 写个迭代器,传入一个数字,生成斐波那契数列;
	# 例如传入5,生成斐波那契的前5个数字;

# class Feibo:
#     def __init__(self,n):
#         self.n = n
#         self.a = 1
#         self.b = 1
#         self.count = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.count < self.n:
#             t = self.a
#             self.a,self.b = self.b,self.a+self.b
#             self.count += 1
#             return t
#         else:
#             raise StopIteration
# f = Feibo(5)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))


# print(iter(f))
# print(dir(f))
# def feibo(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a,b = b,a+b
# c = iter(feibo(5))
# for i in range(5):
#     print(next(c))


# 2.打印菱形(函数)
# 	1. 空格, *组成菱形
# 	2. 输入菱形上半部分行数即可打印

# def rhombus(n):
#     for i in range(1,2*n-1,2):
#         print(("*"*i).center(2*n-1))
#     for i in range(2*n-1,0,-2):
#         print(("*"*i).center(2*n-1))
#
# if __name__ == "__main__":
#     while True:
#         n = input("请输入菱形上半部分行数：")
#         if n.isdigit() and int(n)>0:
#             a = rhombus(int(n))
#         else:
#             print("输入不合法！")

def four(func):
    def inner():
        while True:
            func()
    return inner()

def three(func):

    def inner():
        n = input("请输入菱形上半部分的行数")
        if n.isdigit() and int(n) > 0: # 判断字符串是否全部由数字字符组成
            n = int(n)
            func(n)
        else:
            print("您的输入不合法！不能打印")

    return inner
@four
@three
def rhombus(n):
    for i in range(1,2*n-1,2):
        print(("*"*i).center(2*n-1))
    for i in range(2*n-1,0,-2):
        print(("*"*i).center(2*n-1))

rhombus()
# class test():
#     def __init__(self,data=1):
#         self.data = data
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.data > 5:
#             raise StopIteration
#         else:
#             self.data+=1
#             return self.data
#
# for item in test(3):
#     print(item)


# def fib(end = 1000):
#     prev,curr=0,1
#     while curr < end:
#         yield curr
#         prev,curr = curr,curr+prev
#
#
# print(list(fib()))
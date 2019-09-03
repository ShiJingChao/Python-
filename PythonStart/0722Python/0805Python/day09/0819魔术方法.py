# def num(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return num(n-1)+ num(n-2)
# a = num(10)
# print(a)

# class Num:
#     def __call__(self,n):
#         if n == 1 or n == 2:
#             return 1
#         else:
#             return self(n - 1) + self(n - 2)
#
# a = Num()
# print(a.__call__(10))
# class Num:
#     def __call__(self, n):
#         lis = [1,1]
#         for i in range(2,n+1):
#             lis.append(lis[i-1]+lis[i-2])
#         return lis[n-1]
# a = Num()
# print(a.__call__(3))
# class Feibo:
#     def __call__(self, n):
#         a = 1
#         b = 1
#         for i in range(n-2):
#             a,b = b,a+b
#         return b
# f = Feibo()
# print(f.__call__(3))

# class Person:
#     def __init__(self):
#         print("我是init方法")
#     def __new__(cls, *args, **kwargs):
#         print("我是new方法")
# p = Person()

class A:
    def __init__(self,a):
        self.a = a
    def __eq__(self, other):
        if self.a %6 == 0 and other.a % 6 == 0:
            return True
        else:
            return False
n = A(6)
n2 =A(12)
if n == n2:
    print("相等")

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def __hash__(self):
        return hash((self.x,self.y))

point1 = Point(3,4)
point2 = Point(3,4)
print(point1 == point2)
print(hash(point1))
print(hash(point2))
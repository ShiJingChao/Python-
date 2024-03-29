# 19.07.18作业 史景超
# 作业1 打印九九乘法表

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{}*{}={}".format(i, j, i * j), end=' ')
#     print()
# 作业2 百钱买百鸡
"""
百钱买百鸡的问题算是一套非常经典的不定方程的问题，题目很简单：公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，

用100文钱买一百只鸡,其中公鸡，母鸡，小鸡都必须要有，问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱。

分析：估计现在小学生都能手工推算这套题，只不过我们用计算机来推算，我们可以设公鸡为x，母鸡为y，小鸡为z，那么我们

         可以得出如下的不定方程，

         x+y+z=100,

         5x+3y+z/3=100，

        下面再看看x，y，z的取值范围。

        由于只有100文钱，则5x<100 => 0<x<20, 同理  0<y<33,那么z<300

由于此处我们不是数学上研究不等式解法，而是让计算机为我们计算结果，所有暂不考虑效率问题。于是，从变量上我们便可以看出可以在三个循环中，逐个选出匹配条件。

"""

# for x in range(1, 20):
#     for y in range(1, 33):
#         for z in range(1, 300):
#             if 5 * x + 3 * y + 1 / 3 * z == 100 and x + y + z == 100:
#                 print("买{}只公鸡，{}只母鸡，{}只小鸡".format(x, y, z))


# 作业3 嵌套循环输出2~100之间的素数
import math
from time import time

# begin = time()
# for i in range(2, 100):
#     a = int(math.sqrt(i))
#     for j in range(2, a + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)
# end = time()
# print(begin - end)


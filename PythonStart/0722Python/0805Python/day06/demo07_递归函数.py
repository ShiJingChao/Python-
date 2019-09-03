"""
    递归函数: 如果一个函数在内部调用自身, 这个函数就是递归函数;
            通俗点: 函数自己调用自己

    递归求1-5的和:
        1. 求1-4的和  + 5   ---> get_sum(4) + 5
        2. 求1-3的和  + 4   ---> get_sum(3) + 4
        3. 求1-2的和  + 3   ---> get_sum(2) + 3
        4. 1 + 2   递归的出口 -> 1 + 2

    def get_sum(n):  # n: 代表着求1-谁的和
        pass

"""
# 求1-n的和
def get_sum(n):  # 2
    if n == 1:
        return 1
    else:
        return get_sum(n-1) + n  # get_sum(1) + 2

print(get_sum(5))
"""
n = 5, get_sum(4) + 5 --> 1 + 2 + 3 + 4 + 5
n = 4, get_sum(3) + 4 --> 1 + 2 + 3 + 4
n = 3, get_sum(2) + 3 --> 1 + 2 + 3
n = 2, get_sum(1) + 2 --> 1 + 2
n = 1, return 1
"""

# 使用递归求n的阶乘
"""
分析: 5!
n = 5, 4! * 5
n = 4, 3! * 4
n = 3, 2! * 3
n = 2, 1 * 2
"""
def get_factorial(n):
    if n == 2:
        return 1 * 2
    else:
        return get_factorial(n-1) * n

print(get_factorial(5))

# 第一个月有一对小兔子, 小兔子成长到第三个月就变成了成熟兔子, 成熟兔子每个月都可以生一对小兔子;
# 问: 第n个月共有几对兔子?




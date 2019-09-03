"""
    函数的返回值:
        函数执行结束之后,返回给调用处的结果;

        一个函数的返回值:
            A . 有
            B . 无, 无返回值是,默认为None;

        函数的返回值:
        def 函数名(参数):
            ......
            return 返回值  # 函数的返回值

        return这个关键字的作用:
            1. 结束函数的执行;
            2. 将函数的返回值, 返回给调用处;
"""
list1 = [1, 2, 3, 4, 5, 5]

# 1. 追加元素6  append这个函数是没有返回值的, 该函数返回给调用处的结果是None
print(list1.append(6))  # 函数append()的调用, 实参为6; 此处为函数append的调用处 None

# 2. 计算元素5出现的次数  count这个函数是有返回值的, 返回值的类型为整型, 返回值为元素出现的次数
print(list1.count(5))  # 2 , 此处为count函数的调用,实参为5;

# 3. 字符串.isupper()  有返回值,返回值类型为bool
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 求1-n的阶乘
def factorial(n):  # 形参的本质 就是一个变量
    num = 1
    for x in range(1, n+1):
        num *= x
    print(num)  #  此处打印的是5的阶乘的结果

factorial(10)  # 没有对这个函数执行的结果打印,没有对这个函数的返回值打印;
print(factorial(5))  # 此处为调用处; 打印的是该函数是否有返回值;

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# 求1-n的阶乘
def factorial_new(n):
    num = 1
    for x in range(1, n+1):
        num *= x
    # 将阶乘的结果 返回给调用处
    return num


n = factorial_new(5)  # 此处是factorial_new函数的调用处, 有返回值;

print(n - 1 + 1)  # 120

"""
练习
1: 定义一个函数,接收两个参数,比较两个数大小,
将较大的返回给调用处
2: 定义一个函数,接收两个参数,将两数之和返回给调用处
"""
def big_num(a, b):
    if a > b:
        return a
    else:
        return b

print(big_num(100, 101))

def get_sum(a, b):
    return a + b

print(get_sum(10, 20))
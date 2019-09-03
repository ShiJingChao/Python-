"""
    匿名函数:
        lambda表达式, 只使用一行代码实现一个函数;

        语法规范:
            lambda 参数1, 参数2,.. : 表达式 (表达式执行的结果就是函数的返回值)

        1. 没有名字, lambda表达式相当于返回一个匿名函数(没有名的函数);
        2. 表达式只能有一行, 在这个表达式中不能出现return, 不能出现for..in.., 不能出现while...
        3. 匿名函数的参数规则 和 返回值规则 与普通函数一样

"""

# 写一个函数 用来求两个数的和
get_sum = lambda a, b: a + b
print(get_sum)  # <function <lambda> at 0x0000000002206288>
print(get_sum(1, 2))  # 3

print(lambda : 3 < 2)  # 打印的结果 <function <lambda> at 0x0000000001E76318>

print(lambda x, y, z: x + y + z)  # <function <lambda> at 0x00000000021E6168>

salary = [{"name":"rose", "salary": 1000},{"name": "jack", "salary":2000}]
# 用lambda表达式和max函数 求薪水最高的人
res1 = max(salary, key=lambda x: x.get('salary'))
print(res1)  # {'name': 'jack', 'salary': 2000}

# 用lambda写一个三元表达式
def func(x, y):
    if x > y:
        return x
    else:
        return y

res2 = lambda x, y: x if x > y else y
print(res2(30, 50))

# 内层嵌套函数修改成lambda表达式
def func1():
    x = 10
    # def inner(n , x):
    #     return x ** n
    # return inner
    return lambda n, x: x ** n

def func2():
    x = 10
    # def inner(n, x=x):
    #     return x ** n
    # return inner
    return lambda n, x=x: x ** n

print("------------------------------")

def make_actions():
    acts_list = []
    for i in range(3):  # i = 0, 1, 2
        acts_list.append(lambda x: i ** x) # 函数体调用时候执行
    return acts_list


acts_list = make_actions()  # 返回值acts_list
# i 循环结束之后的值 为2, 所以在循环结束后调用匿名函数, i的值都为2
print(acts_list[0](2))  # 4  lambda x: i ** x (x=2)  i**2 --> 2**2
print(acts_list[1](2))  # 4  lambda x: i ** x (x=2)  i**2 --> 2**2
print(acts_list[2](2))  # 4  lambda x: i ** x (x=2)  i**2 --> 2**2

def make_actions_two():
    acts_list = []
    for i in range(3):  # i = 0, 1, 2
        acts_list.append(lambda x, i=i: i ** x)  # 默认值参数, i有默认的值, 默认值参数的赋值时机,就是函数定义的时候
    return acts_list


acts_list = make_actions_two()  # 返回值acts_list
print(acts_list[0](2))  # 0  lambda x: i ** x (x=2)  i**2 --> 0**2
print(acts_list[1](2))  # 1  lambda x: i ** x (x=2)  i**2 --> 1**2
print(acts_list[2](2))  # 4  lambda x: i ** x (x=2)  i**2 --> 2**2


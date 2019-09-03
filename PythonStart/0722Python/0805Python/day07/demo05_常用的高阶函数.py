"""
    高阶函数:
        参数是一个函数的函数 ---> 高阶函数

        abs(n) : 求n的绝对值,并返回给调用处
        list.sort(key, reverse=False) : 将列表中的每个元素按照指定的规则排序;无返回值,将排序的结果直接作用于原列表;
                                        形参key的值是个函数, 这个函数用来指定列表排序的规则;
                                        这个函数必须要有一个参数, 这个参数就代表列表中的每个元素;
                                        这个函数必须要有一个返回值,这个返回值就是用来比较每个元素排序顺序的;

        sorted(iterable, key, reverse) : python内置的排序函数,将iterable中的每个元素按照指定的规则进行排序,
                                        将排序的结果形成一个新列表返回给调用处;
                                        key和reverse的用法与list.sort()函数一样;

        max(, key) : 指定某种规则,获取最大的值对应的元素
                    max(n1, n2, n3, key) : 对n1, n2, n3按照key进行比较大小, 获取最大的
                    max(容器, key) : 对容器中的元素按照key进行比较大小, 获取最大的
                    key这个形参对应的函数: 必须要有参数(比较的元素)
                                            必须要有返回值(比较的规则)

        map(function, iterable) : 将可迭代对象中的每个元素应用于key函数, 将key函数执行的结果生成一个新的可迭代对象并返回给调用处

        filter(function, iterable) : 指定一个规则, 过滤掉可迭代对象中(序列)不符合规则的元素, 并将符合规则的元素组成一个新的可迭代对象,返回给调用处
                                    function的返回值必须是bool类型, 过滤掉的返回值为False, 保留的返回值为True

        zip(iter1, iter2, ...) 压缩打包 把多个可迭代对象中相同索引值的元素,组成一个元组,然后将所有的元组组成一个新的可迭代对象,返回给调用处
"""
# abs 求绝对值的函数
res1 = abs(-609)
print(res1)

# list.sort(key, reverse=False)  默认正序
# 无返回值
# key 制定排序规则, 参数是一个函数
list1 = [99, 16, 34, -988, 0.123]
list1.sort()
print(list1)  # [-988, 0.123, 16, 34, 99]

# 按照绝对值, 由小到大排序
list1.sort(key=abs)
print(list1)  # [0.123, 16, 34, 99, -988]

# 按照平方的值, 由大到小排序
def square(n):  # 参数  功能: 求一个数的平方,并把结果返回
    return  n ** 2

list1.sort(key=square, reverse=True)
print(list1)  # [-988, 99, 34, 16, 0.123]

print("--------------------------------------")
# python内置的排序函数
res2 = sorted(list1, key=abs, reverse=True)
print(res2)  # [-988, 99, 34, 16, 0.123]
print(type(res2))  # <class 'list'>

print("-----------------------------------------")
# 按照某种规则求最大值
res3 = max(1, 200, -90)
print(res3)

# 1. 求绝对值最大的那个数
res4 = max(1, 200, -999, key=abs)
print(res4)

# 2. 求列表中绝对值最大的那个数
list2 = [1, 200, -999]
res5 = max(list2, key=abs)
print(res5)

list3 = [
    {"name": "Rose", "age": 18},
    {"name": "Jack", "age": 17},
    {"name": "Tom", "age": 16},
]

# 使用max 获取年龄最大的学生的信息
# 对谁进行比较, 谁就是指定规则函数中的参数
def get_max_age(d):  # 指定规则: 比较年龄
    return d.get('age')

res6 = max(list3, key=get_max_age)  # 形参:key --> 函数(参数->dict)
print(res6)  # {'name': 'Rose', 'age': 18}

# 使用max 获取姓名最大的学生的信息
def get_max_name(d):
    return d.get('name')

res7 = max(list3, key=get_max_name)
print(res7)  # {'name': 'Tom', 'age': 16}

print("=====================================")
# 求列表中每个元素的平平方组成的新列表
list4 = [-2, 8, 2.1, -0.4]


def get_square(n):  # 参数: 列表(可迭代对象)中的每一个元素
    return n ** 2


res8 = map(get_square, list4)  # <map object at 0x0000000001E7CA48>
print(list(res8))  # [4, 64, 4.41, 0.16000000000000003]

# 1. 求列表中每个元素对2取余的余数组成系列表
def get_nums(n):
    return n % 2

res9 = list(map(get_nums, [2, 3, 4, 5]))
print(res9)

# 2. 求列表中每个字符串的首字母大写组成的新列表
# str.capitalize 有参数有返回值
def get_first_alpha_upper(s):  # 参数s 列表中的每个字符串
    return s.title()  # s.isupper()  True / False  s.upper()

# res10 = list(map(str.capitalize, ["python", "i", "love", "you"]))
res10 = list(map(get_first_alpha_upper, ['python', 'good', 'study']))
print(res10)

# 3. 求两个列表中相同索引值的元素的和组成的新列表
list5 = [1, 2, 3, 4, 5]
list6 = [10, 10, 10, 10, 10]

def get_sum(a, b):  # a, b分别是每个列表中相同索引值的元素
    return a + b

res11 = list(map(get_sum, list5, list6))  # [11, 12, 13, 14, 15]
print(res11)

print( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# filter(function, iterable) function: 指定过滤规则  iterable:需要进行过滤的序列

list7 = ['python', "ABC", "PYTHON", "123aBcDE"]

# 1. 过滤掉list7中字母全是大写的元素
def filter_up_alpha(s):  # 功能: 过滤 参数:列表中的每个元素
    return not s.isupper()  # 返回值 必须是bool类型, False:该元素被过滤掉, True: 不被过滤掉

res12 = list(filter(filter_up_alpha, list7))  # <filter object at 0x00000000021AEA08>
print(res12)  # ['python', '123aBcDE']

# 2. 过滤掉list7中字母不全是小写字母组成的元素
res13 = list(filter(str.islower, list7))  # str.lower 是否全是由小写字母组成的, 是返回True, 不是返回False
print(res13)  # ['python']


# 4. 过滤掉列表中的所有偶数 (不要偶数)
def get_odd(n):  # 参数: 列表中的每个元素
    if n % 2 == 0:
        return False
    else:
        return True


res14 = list(filter(get_odd, [12, 13, 14, 15, 16]))
print(res14)

print("^"*30)

list8 = [1, 2, 3, 4]
list9 = ["a", "b", "c", "d"]

"""
   <zip object at 0x00000000026AF588> [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
"""

res15 = list(zip(list8, list9))  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
print(res15)

# 应用场景:
for x in zip(list8, list9):
    print(x)



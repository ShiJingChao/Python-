# 不可变数据类型和可变数据类型自加的区别
# 1. 判断gl_num和gl_list的值
def demo(num, num_list):
    num += num
    num_list += num_list

    print(num)
    print(num_list)

    print("函数完成")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)


# 传值和传址问题

# 2.请说出 list1,list2,list3 的值是什么，并且说明为什么
def extendlist(val, lis=[]):
    lis.append(val)
    return lis


list1 = extendlist(10)

list2 = extendlist(123, [])

list3 = extendlist('a')

print(list1)  

print(list2) 

print(list3)  


# 匿名函数

# 3.请说出acts[0](2)的值，并且说明为什么
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts


acts = makeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))
print(acts[4](2))

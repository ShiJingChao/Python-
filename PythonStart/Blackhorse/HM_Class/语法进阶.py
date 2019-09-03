# CLASS 227 ——CLASS 228变量的引用
# 调用函数传递实参的引用
def test(num):
    print("在函数内部%d对应的内存地址是：%d" % (num, id(num)))
    # 1.定义一个字符串变量
    result = "hello"

    print("函数要返回数据的内存地址是：%d" % id(result))
    # 2.将字符串变量返回
    return result


# 1.定义一个数字的变量
a = 10
# 数据的地址本质上就是一个数字
print("a变量保存数据的内存地址是%d" % id(a))

# 2.调用test函数
# 调用函数传参的时候并不会传递数字10，
# 而是会把变量a中保存的内存地址传递到函数内部
# 如果函数有返回值，但是没有定义变量接收，程序不会报错，但是无法获得任何的返回结果
test(a)



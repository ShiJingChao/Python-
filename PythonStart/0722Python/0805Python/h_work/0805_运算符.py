# 第一题
user = input("请输入用户名：")
pwd = input("请输入密码：")
is_pwd = input("是否记住密码：")
print(user, pwd, is_pwd)
# 第二题
num1 = int(input("请输入两个整数"))
num2 = int(input())
sum = num1 + num2
dif = num1 - num2
pro = num1 * num2
shang = num1 / num2
yushu = num1 % num2
print("和为%d，差为%d，积为：%d，商为：%d，余数为：%d"
      % (sum, dif, pro, shang, yushu))
# 第三题
a = int(input("请输入一个四位数："))
b = a // 1000
c = a % 1000 // 100
d = a % 1000 % 100 // 10
e = a % 1000 % 100 % 10
print(b, c, d, e)

# 第四题
java = 95
python = java + 2.5
print(python)

# 第五题
# 结果是：2 5

# 类型转换
# 第一个
print(True + 100)
# 第二个
a = 3.14
b = int(a)
c = bool(a)
print(b, c)
# 第三个
print(hex(20))
print(oct(20))
print(bin(20))
# 第四个
a = "123"
num = int(a)
print(type(num))
# 第五个
print(2 ** 10)
# 第六个
print(101 % 3)
# 第七个
print(chr(65))
# 第八个
print(eval("10/2"))
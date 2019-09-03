# 19.07.17作业 史景超
# 作业1.用户登录
# user= 'admin'
# pwd = '123456'
# while True:
#     in_user = input('请输入用户名：')
#     in_pwd = input('请输入密码')
#     if user == 'admin' and pwd == '123456':
#         print('登陆成功！')
#     else:
#         print('用户名或密码错误，请重新输入！')

# user = "admin"
# pwd = "000000"
# auth_code = "2346"
#
# is_user = input("请输入用户名：")
#
# if is_user != user:
#     print("用户名错误！")
# else:
#     is_pwd = input("请输入密码:")
#     if is_pwd != pwd:
#         print("密码错误")
#     else:
#         print("验证码为：2346")
#         is_auth = input("请输入验证码：")
#         if is_auth != auth_code:
#             print("验证码错误")
#         else:
#             print("登录成功！")

# 2.猜拳（石头剪刀布）
# import random
#
# while True:
#     guess = int(input("请输入你要出的手势：1：石头 2：剪刀 3：布"))
#     pc_guess = random.randint(1, 3)
#     print('电脑出的手势为：', pc_guess)
#     if guess - pc_guess == -1 or guess - pc_guess == 2:
#         print('你赢了')
#         jixu = int(input('是否继续？1：是 2：否'))
#         if jixu == 1:
#             continue
#         elif jixu == 2:
#             break
#     elif guess - pc_guess == -2 or guess -pc_guess == 1:
#         print('你输了')
#         ixu = int(input('是否继续？1：是 2：否'))
#         if jixu == 1:
#             continue
#         elif jixu == 2:
#             break


# 3.数字炸弹（猜数0-99）
import random
start = 0
end = 99
suiji = random.randint(start, end)
while True:
    guess = int(input('请输入一个数字（{}-{}）'.format(start, end)))
    if guess > suiji:
        print('你猜的数大了，轮到电脑猜了')
        end = guess - 1
        pc_guess = random.randint(start, end)
        if pc_guess > suiji:
            print("电脑猜的数为：%d，电脑猜的数大了" % pc_guess)
            end = pc_guess - 1
        elif pc_guess < suiji:
            print('电脑猜的数为：%d，电脑猜的数小了' % pc_guess)
            start = pc_guess + 1
        elif pc_guess == suiji:
            print('电脑猜中了，你输了，随机数为：', suiji)
            jixu = int(input("请输入是否继续？1：继续 2：退出"))
            if jixu == 1:
                continue
            elif jixu == 2:
                break
    if guess < suiji:
        print("你猜的数小了，轮到电脑猜了")
        start = guess + 1
        pc_guess = random.randint(start, end)
        if pc_guess > suiji:
            print("电脑猜的数为：%d，电脑猜的数大了" % pc_guess)
            end = pc_guess -1
        elif pc_guess < suiji:
            print('电脑猜的数为：%d，电脑猜的数小了' % pc_guess)
            start = pc_guess+1
        elif pc_guess == suiji:
            print('电脑猜中了，你输了，随机数为：', suiji)
            jixu = int(input("请输入是否继续？1：继续 2：退出"))
            if jixu == 1:
                continue
            elif jixu == 2:
                break
    if guess == suiji:
        print("恭喜，你猜中了！")
        jixu = int(input("请输入是否继续？1：继续 2：退出"))
        if jixu == 1:
            continue
        elif jixu == 2:
            break

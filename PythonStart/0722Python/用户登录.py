user = "admin"
pwd = "000000"
auth_code = "2346"
is_user = input("请输入用户名：")

if is_user != user:
    print("用户名错误！")
else:
    is_pwd = input("请输入密码:")
    if is_pwd != pwd:
        print("密码错误")
    else:
        print("验证码为：2346")
        is_auth = input("请输入验证码：")
        if is_auth != auth_code:
            print("验证码错误")
        else:
            print("登录成功！")

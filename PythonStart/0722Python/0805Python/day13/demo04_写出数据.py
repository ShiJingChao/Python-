"""
FileNotFoundError: [Errno 2] No such file or directory: 'first.txt'
io.UnsupportedOperation: not writable  该文件不可写

    写出数据:
        1. 打开文件 open(路径, 模式, 编码)
        2. 写出数据 write(内容)
        3. 关闭文件

    打开文件的模式: 默认是只读

    只读, 只写, 只追加写, 可读可写, 可读可追加写

    模式名     可做的操作       文件不存在
    r           可读              报错
    r+          可读可覆盖写      报错
    w           覆盖写            创建
    w+          可读可写          创建
    a           追加写            创建
    a+          可读可写          创建

* w+ 可读可写, 读不出来东西;
* a+ 可读可写, 读不出来东西;
------------------------------------
1. 文件不存在:  r, r+ --> 报错; 其他的都会创建;
2. 带 + 号的, 可读可写; a+, w+, r+
    a , append, 追加写
    w , write, 覆盖写
    r, read, 可读
"""

f = open("four.txt", mode='a+')

# f.write("!!!!!!!!")
# print(f.read())
f.writelines("qwertyuiopasdfghjklzxcvbnm")
f.writelines(["\n床前明月光\n", "疑是地上霜\n", "举头望明月\n", "低头思故乡"])

f.close()

# 1. 通过程序创建一个alpha.txt的文件, 将26个英文字母写在里边, 不要划拉键盘
# 2. 写一首诗, 每句换行
# 3. 模拟聊天记录, 循环通过键盘输入, 俩人, 将俩人的对话保存在chat.txt中
# 小花说: 用户输入说话的内容....
# 二狗说: ....
# 小花说: .....
# 二狗说: ....
# 小花说: 用户没有输入 直接回车
# 二狗说: 用户没有输入 直接回车
# 聊天结束, 将以上存在chat.txt中; 并记录聊天的日期和时间: 2019-08-21 14:12:38




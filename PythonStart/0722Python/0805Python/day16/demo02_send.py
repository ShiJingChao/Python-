from socket import *

ip = "127.0.0.1"  # 接收方的 ip地址, 本机: 127.0.0.1, localhost
port = 4444  # 端口号, 65535, 1~1023, 1024--> 以后设置
address = (ip, port)  # 接收方的地址

# 创建一个socket对象
s = socket(AF_INET, SOCK_DGRAM)

while True:
    # 发送数据
    # info = "喂, 你在吗, 找你说点数, 放心, 不借钱..."
    info = input("请输入你要发送的内容:")
    if info:
        s.sendto(info.encode('utf-8'), address)
    else:
        break
# 发送完毕 --> 关闭
s.close()






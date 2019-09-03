from socket import *

# 初始化操作
ip = "127.0.0.1"  # 接收方的ip
port = 4444  # 接收方端口
address = (ip, port)

# 创建socket对象
s = socket(AF_INET, SOCK_DGRAM)

# 绑定接收地址
s.bind(address)

while True:
    # 接收数据
    data, adr = s.recvfrom(1024)
    print("接收到{}发送的信息, 信息的内容是:{}".format(str(adr), str(data, 'utf-8')))








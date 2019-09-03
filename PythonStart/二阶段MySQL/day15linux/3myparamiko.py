import paramiko

# 创建客户端
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接
ssh.connect(hostname='10.10.107.84',port=22,username='root',password='123456')

# 创建一个shell
shell = ssh.invoke_shell()
shell.settimeout(1)
# 获取命令
command = input('>>') + '\n'
# 发送命令
shell.send(command)

while True:
    if command == 'q' + '\n':
        break
    try:
        # 获取返回的结构
        recv = shell.recv(512).decode()
        if recv:
            print(recv)
        else:
           continue
    except:
        command = input('>>') + '\n'
        # 发送命令
        shell.send(command)



ssh.close()

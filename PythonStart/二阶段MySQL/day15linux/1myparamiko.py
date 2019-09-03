import paramiko

# 创建一个客户端
ssh = paramiko.SSHClient()
# 创建一个白名单
know_host = paramiko.AutoAddPolicy()
# 设置不提醒
ssh.set_missing_host_key_policy(know_host)
# 连接服务器
ssh.connect(hostname = '10.10.107.84',port=22,username='root',password='123456')
# 执行linux命令
stdin, stdout, stderr = ssh.exec_command('mkdir /home/zhy/Desktop/g')
# stdin 标准输入     文件对象 写权限
# stout 标准的输出   文件对象 读权限
# stderr 特殊的输出  文件独享 读权限
# 查看输出结果
print(stdout.read().decode())
# 关闭连接
ssh.close()
import threading
import paramiko

class MyThread(threading.Thread):
    def __init__(self,host,user,pwd,port=22):
        self.host=host
        self.user=user
        self.pwd=pwd
        self.port=port
        super(MyThread, self).__init__()

    def run(self):
        # 创建客户端
        ssh = paramiko.SSHClient()
        # 设置白名单不提醒
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

        # 连接
        ssh.connect(hostname=self.host,port=self.port,username=self.user,password=self.pwd)

        # 执行命令
        stdin,stdout,stderr=ssh.exec_command('mkdir /opt/love')
        print(stdout.read().decode())

        # 关闭连接
        ssh.close()

if __name__ == '__main__':
    data = [
        {'host':'10.10.107.52','user':'root','password':'root123'},
        {'host': '10.10.107.84', 'user': 'root', 'password': '123456'},
        {'host': '10.10.107.114', 'user': 'root', 'password': '970220..'},
        {'host': '10.10.107.173', 'user': 'root', 'password': '940315'},
    ]
    tlist = []
    for i in data:
        t = MyThread(host=i['host'],user=i['user'],pwd=i['password'])
        tlist.append(t)

    for i in tlist:
        i.start()

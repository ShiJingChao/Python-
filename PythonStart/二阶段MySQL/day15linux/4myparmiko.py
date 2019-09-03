import paramiko

trans = paramiko.Transport(sock=('10.10.107.84'))

trans.connect(username='root',password='123456')

sftp = paramiko.SFTPClient.from_transport(trans)

# put('你要上传的文件','上传的位置')
# sftp.put('jiandandian','/opt/newjdd')
# get('你要下载的文件','下载的位置')
sftp.get('/opt/newjdd','love')

sftp.close()


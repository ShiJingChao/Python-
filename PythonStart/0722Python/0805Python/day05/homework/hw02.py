"""
2. 给定一个路径名：
String pathName="http://192.168.10.1:8080/Day33_Servlet/aa.jpeg";
获取文件名称：aa.jpeg
"""

pathName="http://192.168.10.1:8080/Day33_Servlet/aa.jpeg"

index = pathName.rfind('/')  # 查找获取索引值

file_s = pathName[index+1::]  # 通过索引值切片

print(file_s)  # aa.jpeg


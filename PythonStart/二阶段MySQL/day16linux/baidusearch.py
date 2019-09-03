import requests

base_url = 'http://www.baidu.com/s?wd='

# 提示用户输入要搜多的内容
msg = input('请输入你要搜索的内容:')

# 拼接url地址
base_url+=msg

# 发送请求
response = requests.get(base_url)

print(response.content.decode('utf-8'))
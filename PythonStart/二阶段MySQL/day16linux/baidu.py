import requests

# 确定 url地址
base_url = 'http://www.baidu.com/'
'''
    get 
        以url地址进行传参，参数明文显示 以？进行拼接 参数和参数之间用&间隔
        相对不安全 而且受浏览器影响数据有大小限制
    post
        参数不会明文显示，
        相对安全
        理论数据没有大小限制
'''
# 发送请求
response = requests.get(base_url)

# 将爬取到的源代码 存入到本地文件
with open('baidu.html','w',encoding='utf-8') as f:
    f.write(response.content.decode())


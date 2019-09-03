"""
                发送请求                返回响应

   百度一下     浏览器www.baidu.com     百度服务器返回给我们页面信息

   人脸识别     请求识别人脸信息        识别后的人脸信息
                (人脸图片)

    * 可以通过request模块发起请求, 请求之后的响应, 可以通过调用函数后的返回值来获取;

    get请求: 获取服务器资源的;
    post请求: 提交数据, 提交给服务器资源的;
    response = requests.post(网址, 数据信息...)

    url参数:
        http://www.baidu.com/tieba/fangzuming?name=lixue&age=18
        url中?后边接的是参数, 参数格式为: 参数名=参数值, 多个参数之间用?连接.
        
    name=lixue
    name: 参数名
    lixue: 参数值

    age=18
    age: 参数名
    18: 参数值
"""
import requests

# 百度一下 --> 浏览器,地址栏-->输入 http://www.baidu.com
response = requests.get("http://www.baidu.com")

# print(response.text)  # text --> 自己挑选解码方式进行解码, 如果不对--->出现乱码
print(response.content.decode('utf-8'))  # 用指定的方式进行解码








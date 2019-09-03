"""
    json:
        作用: 传输数据
        本质: 字符串

        字典, 列表;

    "[
    {"name": "张碧正",  "age": 18},
    {"name": "任思锦", "age": 17},
    .....
    ]"
"""
import requests
import base64
import json

# 获取access_token的值
def get_access_token():
    # 折行显示
    url = "https://aip.baidubce.com/oauth/2.0/token?" \
          "grant_type=client_credentials&" \
          "client_id=SdnZagCfatQDEtjoPIKhf2zR&" \
          "client_secret=bL1bA9Gs3HnSoGfiR3Mix88Gg3YjIURI"

    r = requests.post(url)  # 发起请求, 通过返回值获得响应
    res = r.json()  # 将响应中的json文本 ---> python中对应的数据类型
    return res.get('access_token')  # 获取access_token的值


# 活体检测
def face_liveness():

    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceverify?access_token=%s" % get_access_token()

    header = {"Content-Type": "application/json"}

    with open(r"D:\1.png", "rb") as f:
        pic = base64.b64encode(f.read())
        # print(type(pic))  # <class 'bytes'>

    body = [
        {
            "image": str(pic, 'utf-8'),  # 将字节类型数据 --> 字符串, 编码方式utf-8
            "image_type": "BASE64"
         }
    ]
    body = json.dumps(body)  # 把python的字典/列表类型数据 --->  json文本字符串
    # print(type(body))  # <class 'str'>

    r = requests.post(url, headers=header, data=body)
    # r = requests.post(url, headers=header, json=body)
    print(r.json())


face_liveness()



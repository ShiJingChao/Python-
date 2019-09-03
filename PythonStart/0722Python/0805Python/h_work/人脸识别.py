import base64

import requests

"""
json：
    作用：
    容器：可变容器，列表，字典
    
"""


# 请求地址
# url ="https://aip.baidubce.com/oauth/2.0/token?" \


def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token?"\
          "grant_type=client_credentials&"\
          "client_id=XoPA0jSLHB7jOGfg1sl86EbN&"\
          "client_secret=sOsBA8zG6njpZrhXLvPUKpKsDF6cBe1o"
    response = requests.post(url)  # 发起请求，获得相应
    res = response.json()  # response.text,response.decode("utf-8"),response.json()获取相应的json内容
    # print(type(res))
    # print(res)
    return res.get('access_token')  # 返回access_token的值


def detect_face():
    url = "https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=%s" % get_access_token()

    header = {
        "Content-Type": "application/json"
    }
    with open(r"C:\Users\Administrator\Desktop\images\7.jpg", "rb") as f:
        b64_img = base64.b64encode(f.read())
    data = {
        "image": b64_img,
        "image_type": "BASE64",
        "face_field":"age,beauty,expression,face_shape,gender,glasses",
        }

    # 发起请求 --》获取响应对象
    r = requests.post(url, headers=header, data=data)

    print(r.json())


detect_face()
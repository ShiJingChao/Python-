# encoding:utf-8
import json
import requests

"""
在线活体检测

"""

def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token?"\
          "grant_type=client_credentials&"\
            "client_id=XoPA0jSLHB7jOGfg1sl86EbN&"\
            "client_secret=sOsBA8zG6njpZrhXLvPUKpKsDF6cBe1o"
    response = requests.post(url)
    res = response.json()

    return res.get('access_token')

def detect_face():
    url = "https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=%s" % get_access_token()
    header = {
        "Content-Type": "application/json"
    }
    data = {
        "image": "https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/crop%3D0%2C0%2C769%2C507%3Bc0%3Dbaike92%2C5%2C5%2C92%2C30/sign=7f680ee44b34970a533c4a6fa8fafdf8/a5c27d1ed21b0ef4cc6e5e95d7c451da80cb3e73.jpg",
        "image_type": "URL",
        "face_field": "age,beauty,expression"
    }
    s = json.dumps(data)
    print(s)
    r = requests.post(url, headers=header, data=s)

    print(r.json())


detect_face()
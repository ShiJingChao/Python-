"""
json:
    作用: 数据存储/数据传输
    本质: 字符串

    容器: 可变容器, 列表, 字典

    "["李小花", "王二狗"]"

    "{
        "name": "李小花",
        "age": 18
    }"
"""
import requests, base64


# 获取access_token
def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token?" \
          "grant_type=client_credentials&" \
          "client_id=SdnZagCfatQDEtjoPIKhf2zR&" \
          "client_secret=bL1bA9Gs3HnSoGfiR3Mix88Gg3YjIURI"
    r = requests.post(url)  # 发起请求, 获取响应
    res = r.json()  # r.text, r.content.decode('utf-8'), r.json() 获取响应的json内容
    # print(type(res))  # <class 'dict'>
    # print(res)
    return res.get('access_token')  # 返回值为access_token的值


def detect_face():
    # 请求的地址
    url = "https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=%s" % get_access_token()

    header = {"Content-Type": "application/json"}

    with open(r"C:\Users\ThinkPad\Documents\Tencent Files\1099569458\FileRecv\MobileFile\1.JPG", "rb") as f:
        b64_img = base64.b64encode(f.read())

    data = {
        "image": b64_img,
        "image_type": "BASE64",
        "face_field": "age,beauty,expression,face_shape,gender,glasses"
    }

    # 发起请求 --> 获取响应对象r
    r = requests.post(url, headers=header, data=data)
    print(r.json())  # 获取响应的json格式数据


detect_face()








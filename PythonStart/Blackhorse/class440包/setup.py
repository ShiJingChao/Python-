from distutils.core import setup

setup(name="class440包", #包名
      version="1.0", #版本
      description = "sanren 发送和接收模块",   #描述信息
      long_description="完整的发送和接收消息模块",  #完整描述信息
      author="sanren",  # 作者
      author_email= "1015174363@qq.com",
      url = "www.sanren.com", #主页
      py_modules = ["receive_message",
                    "send_message"]


      )
# 2 在D盘根目录下有一个名为"exam.txt"的文本文件，编写程序读取其文本信息
file = open("D:\\exam.txt",'r')
text = file.read()
print(text)
file.close()
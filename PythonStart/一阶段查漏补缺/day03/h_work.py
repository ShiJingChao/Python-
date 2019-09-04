b = (20,1,3,4,8,9,5,6)
print("最大值为：{}，下标为{}\n最小值为：{}，下标为：{}".format(max(b),b.index(max(b)),min(b),b.index(min(b))))


# 或者

b = (20,1,3,4,8,9,5,6)
dic = {}
ma = 0
ma_i = 0
mi = 0
mi_i = 0
for k,v in enumerate(b):
    dic[k] = v
ma = max(dic.values())
mi = min(dic.values())
for k,v in dic.items():
    if v == ma:
        ma_i = k
    if v == mi:
        mi_i = k
print("最大值为：{}，下标为{}\n最小值为：{}，下标为：{}".format(ma,ma_i,mi,mi_i))
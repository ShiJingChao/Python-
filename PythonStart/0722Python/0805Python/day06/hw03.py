"""
4.
创建一个字典 姓名：范冰冰 身高：168 身份：女神 爱好：打黑牛

	请循环遍历出所有的KEY
	请循环遍历出所有的value
	请循环遍历出所有的KEY和VALUE
	请在字典中添加一个键值对，兴趣：李晨,输出添加后的字典
	请删除字典中键值对身高：168 ,并输出删除后的字典
	请删除字典中键‘范丞丞’对应的键值对，如果字典中不存在键‘范丞丞’，则不报错，并且让其返回none
	请获取字典中’身份‘对应的值
	请获取字典中’弟弟’对应的值，如果’弟弟’不存在，则不报错，并且让其返回None

"""
dict1 = {
    "姓名": "范冰冰",
    "身高": 168,
    "身份": "女神",
    "爱好": "大黑牛"
}

for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)

for k, v in dict1.items():  # [(key, value), ()]
    print(k, v)

# dict1["兴趣"] = "李晨"
dict1.update(兴趣="李晨")
print(dict1)

dict1.pop('身高')
print(dict1)

# step1:  查找 范丞丞 这个key是否存在
# step2: 存在删除, 不存在返回none

# if dict1["范丞丞"]:    # KeyError: '范丞丞'

# if "" ---> if False
# if " " ---> if True
# if []: ---> if False
# if none:  ---> if False

if dict1.get('范丞丞'):  # 如果 范丞丞这个键存在
    print(dict1["范丞丞"])
else:  # 如果 范丞丞这个键不存在
    print("none")

print(dict1["身份"])
print(dict1.get('身份'))

print(dict1.get('弟弟'))  # none;



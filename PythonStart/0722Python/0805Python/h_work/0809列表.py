# 【列表专项练习】
# 北京相声社团相声德云社将于2018年5月9日到访北网,1803c班特编写了一个欢迎程序,
# 1.请定义一个列表visitor_list存储德云社到访人员,郭德纲,于谦,王尚举,小岳岳,郭麒麟
visitor_list = ["郭德纲", "于谦", "王尚举", "小岳岳", "郭麒麟"]
# 2.夏日炎炎,但是9号当日天空中飘起了鹅毛大雪,原来是窦娥也要来校参观,请在vistor_list中添加窦娥
visitor_list.append("窦娥")
# 3.张驴儿闻说此事,也追赶至此,对窦娥实施迫害,请在vistor_list中窦娥前插入张驴儿
visitor_list.insert(5, "张驴儿")
# 4.世界上那里有黑暗,哪里就存在着光明,开封府包黑炭包青天包拯包大人决定为民除害,押走了张驴儿,请根据人名,删除vistor_list中张驴儿
visitor_list.remove("张驴儿")
# 5.天有不测风云,小岳岳后院起火,不能如期来我校到访,特托孙越来救场,故更改到访人员vistor_list中小岳岳为孙越
visitor_list[3] = "孙越"
# 6.9号当天,原本到访的人中,第二个人没有来,请将位于到访名单中第二个位置的人删除
del visitor_list[1]
# 7. 郭德纲讲话说"演艺的道路不好走啊, 我走这一辈子可能都收获不了影帝, 但是影后能收获好几个 比如范冰冰 章子怡 巩俐 贾玲"
# 请定义一个列表movie_queen存储郭德纲收获的影后
movie_queen = ["范冰冰", "章子怡", "巩俐", "贾玲"]
# 8. 有一天老郭越想越觉得自己某一时刻一定是被什么蒙了眼睛,决定删除movie_queen中最后一个美女
del movie_queen[-1]
# 9. 世上哪有不透风的墙, 老郭媳妇听到了些许风言风语, 最近对老郭看的非常紧,老郭决定这段日子,要金盆洗手,严防后院起火,故打算解散自己的movie_queen,让该列表不复存在
del movie_queen

# 1.遍历列表：
nums = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]
for i in nums:
    for j in i:
        print(j, end=" ")
# 2.给定一个含有n个元素的整型数组，如果元素出现的次数为奇数次，就输出
nums = [2, 1, 2, 1, 3, 1, 4, 5, 3]
for i in nums:
    if nums.count(i) % 2 != 0:
        print(i, end='')
# 3.有两个有序列表，[1，3，5，7，9]和[2，4，6，7，8]，设计使两个数组合并，并且剔除掉两个数组里重复的元素。{1,2,3,4,5,6,7,8,9}。
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 7, 8]
c = set(a + b)
print(c)

# 4.给定两个含有n个元素的有序（非降序）整型列表a和b，求出其共同元素
a = [0, 1, 2, 3, 4]
b = [1, 3, 5, 7, 9]
c = set(a)
d = set(b)
print(c & d)

4.
# 创建一个字典 姓名：范冰冰 身高：168 身份：女神 爱好：打黑牛

# 请循环遍历出所有的KEY
# 请循环遍历出所有的value
# 请循环遍历出所有的KEY和VALUE
# 请在字典中添加一个键值对，兴趣：李晨,输出添加后的字典
# 请删除字典中键值对身高：168 ,并输出删除后的字典
# 请删除字典中键‘范丞丞’对应的键值对，如果字典中不存在键‘范丞丞’，则不报错，并且让其返回none
# 请获取字典中’身份‘对应的值
# 请获取字典中’弟弟’对应的值，如果’弟弟’不存在，则不报错，并且让其返回None


dirt_bb = {"姓名": "范冰冰", "身高": 168, "身份": "女神", "爱好": "打黑牛"}
for i in dirt_bb.keys():
    print(i, end="  ")
for j in dirt_bb.values():
    print(j, end="  ")
for k in dirt_bb.items():
    print(k, end="  ")
dirt_bb["兴趣"] = "李晨"
print(dirt_bb)
dirt_bb.pop("身高")
print(dirt_bb)
print(dirt_bb.pop("范丞丞",[None]))
for i in dirt_bb.keys():
    if "范丞丞" in dirt_bb:
        del dirt_bb["范丞丞"]
else:
    print(dirt_bb.get("范丞丞"))

dirt_bb.pop("身份")
print(dirt_bb)
print(dirt_bb.get("弟弟"))

# 5.ECALIYHWEQAEFSZCVZTWEYXCPIURVCSWTDBCIOYXGTEGDTUMJHUMBJKHFGUKNKN
# 每个字母出现的次数
# 	提示：字典{字母：count}

a = "ECALIYHWEQAEFSZCVZTWEYXCPIURVCSWTDBCIOYXGTEGDTUMJHUMBJKHFGUKNKN"
b = set(a)
c = {}
for i in b:
    c[i] = a.count(i)
print(c)
# 6.动态给字典输入五个姓名与手机号
dirt = {}
for i in range(5):
    a = input("请输入姓名：")
    b = input("请输入手机号：")
    dirt[a] = b
print(dirt)

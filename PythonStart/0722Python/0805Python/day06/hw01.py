"""
【列表专项练习】
北京相声社团相声德云社将于2018年5月9日到访,0805班特编写了一个欢迎程序,
1.请定义一个列表visitor_list存储德云社到访人员,郭德纲,于谦,王尚举,小岳岳,郭麒麟
"""
# 1
visitor_list = ["郭德纲", "于谦", "王尚举", "小岳岳", "郭麒麟"]

# 2 2.夏日炎炎,但是9号当日天空中飘起了鹅毛大雪,原来是窦娥也要来校参观,请在vistor_list中添加窦娥
visitor_list.append('窦娥')  # ["郭德纲", "于谦", "王尚举", "小岳岳", "郭麒麟", "窦娥"]
# visitor_list.insert(0, '窦娥')  # ["窦娥", "郭德纲", "于谦", "王尚举", "小岳岳", "郭麒麟"]

# 3.张驴儿闻说此事,也追赶至此,对窦娥实施迫害,请在vistor_list中窦娥前插入张驴儿
# 插入谁前边, insert的第一个参数,就应该是插入谁的索引值
visitor_list.insert(-1, "张驴儿")  # ["郭德纲", "于谦", "王尚举", "小岳岳", "郭麒麟", "张驴儿", "窦娥"]

# 4.请根据人名,删除vistor_list中张驴儿
visitor_list.remove('张驴儿')
print(visitor_list)  # ['郭德纲', '于谦', '王尚举', '小岳岳', '郭麒麟', '窦娥']

# 5.更改到访人员vistor_list中小岳岳为孙越
visitor_list[3] = "孙越"  # ['郭德纲', '于谦', '王尚举', '孙越', '郭麒麟', '窦娥']
print(visitor_list)

# 6.请将位于到访名单中第二个位置的人删除
visitor_list.pop(1)  # ['郭德纲', '王尚举', '孙越', '郭麒麟', '窦娥']
print(visitor_list)

# 7. movie_queen
movie_queen = ["章子怡", "范冰冰", "巩俐", "贾玲"]

# 8.删除最后一个
movie_queen.pop()
print(movie_queen)  # ['章子怡', '范冰冰', '巩俐']

# 9. 解散自己的movie_queen,让该列表不复存在
del movie_queen
# print(movie_queen)  # NameError: name 'movie_queen' is not defined



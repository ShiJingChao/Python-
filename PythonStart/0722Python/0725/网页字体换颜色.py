list = ["#FF0000", "#00FF00", "#0000FF"]
a = "con"
web = open('chat.html', 'w')
for i in range(3):
    web.write('<font color = {}>{}</font>'.format(list[i], a[i]))
    print("\t")
web.close()

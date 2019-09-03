# 所有消费记录
customer_bill = []

# 零售
def sale():
    print("=" * 38)
    print("1. 肉丝打卤面  20".center(30))
    print("2. 披萨饼  80".center(30))
    print("3. 汉堡包  8".center(30))
    print("4. 肥宅快乐水  4.5".center(30))
    print("=" * 38)

    this_bill = {}
    money = 0  # 用来记录总价格
    while True:
        goods = input("请输入您要购买的商品序号:")
        if not goods:  # "" --> False
            print("总共需要支付: %.2f元" % money)
            u_money = float(input("请输入您支付的金额:"))
            print("本次支付%.2f元, 应找零%.2f元" % (u_money, u_money - money))
            this_bill["消费金额"] = money
            this_bill["支付金额"] = u_money
            this_bill["找零金额"] = u_money - money
            customer_bill.append(this_bill)  # 记录本次消费记录
            break  # 如果啥也没输入,代表不买了,跳出循环
        count = int(input("请输入您要购买的数量:"))

        if goods == "1":
            this_bill["肉丝打卤面"] = count
            money += 20 * count
        elif goods == "2":
            this_bill["披萨饼"] = count
            money += 80 * count
        elif goods == "3":
            this_bill["汉堡包"] = count
            money += 8 * count
        elif goods == "4":
            this_bill["肥宅快乐水"] = count
            money += 4.5 * count
        else:
            print("您当前输入有误, 请重新输入")
            continue


# 查询消费记录
def query_bill():
    u_input = input("请输入您要哪次的消费记录,如不输入,代表查询全部:")
    if u_input == "":  # 查询全部
        for bill in customer_bill:  # 遍历获取每次的消费记录
            print("-----------------------")
            for k, v in bill.items():  # 遍历一次消费记录, 获取其中存储的键值对
                print(k, v)
    else:
        count = int(u_input) - 1  # 第一次: 1 ---> list 索引为0
        bill = customer_bill[count]
        print("~~~~~bill~~~~~~")
        for k, v in bill.items():
            print(k, v)


# 主函数
def main():
    while True:
        print("=" * 38)
        print("欢迎来到AI牌自动贩卖机".center(30))
        print("1.零售".center(30))
        print("2.退出".center(30))
        print("3.查询消费记录".center(30))
        print("=" * 38)

        res = input("请输入您的选择:")

        if res == "1":
            sale()
        elif res == "3":
            query_bill()
        elif res == "2":
            break
        else:
            print("您输入有误, 请仔细阅读,重新输入")


if __name__ == "__main__":
    main()






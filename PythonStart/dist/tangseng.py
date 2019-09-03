player = "唐僧"
print("=" * 20, "欢迎来到《{}大战白骨精》休闲小游戏".format(player), "=" * 20)
cos = input("请输入你要扮演的角色：\n\t1：{}\n\t2：白骨精\n请选择（1-2）：".format(player))
health_point = 2
attack = 2
judge = True
boss_health = 50
boss_attack = 10
if cos == "1":
    print("恭喜你将以{}的身份进行游戏!\n".format(player), "=" * 60)
elif cos == "2":
    print("什么？！看看游戏名，太不要脸了，你竟然选择白骨精，白骨精可是BOSS\n"
          "你已经被系统分配以->{}-<身份进行游戏\n".format(player), "=" * 60)
else:
    print("你输入的信息有误，系统自动分配，你将以->{}<-的身份进行游戏".format(player))
print("\n你的身份是->{}<-,你的攻击力是2 你的生命值是：2\n".format(player))
while True:
    choose = input("请选择你要进行的操作：\n\t1:练级\n\t2:打BOSS\n\t3:逃跑"
                   "\n请选择要做的操作[1-3]:")
    if choose == "1":
        health_point += 2
        attack += 2
        print("恭喜你升级了，你现在的生命值为{}，攻击力为{}\n".format(health_point, attack), "-" * 60)
    elif choose == "2":
        while True:
            print("-" * 20, "\n->{}攻击了->白骨精,白骨精受到了{}点伤害".format(player, attack))
            boss_health -= attack
            if boss_health > 0:
                print("-" * 20, "\n白骨精没有死，轮到白骨精攻击，{}受到{}点伤害".format(player, boss_attack))
            if boss_health <= 0:
                print("{}打败了白骨精，{}是比白骨精更磨人的小妖精~".format(player, player))
                game_over = input("游戏结束，请输入任意键退出")
                if game_over == "Y":
                    judge = False
                    break
                else:
                    judge = False
                    break
            else:
                health_point -= boss_attack
                if health_point <= boss_attack:
                    game_over1 = input("{}太弱了，被白骨精的妖娆迷惑住了，你挂了\n游戏结束，请输入任意键退出".format(player, boss_attack))
                    if game_over1 == "Y":
                        judge = False
                        break
                    else:
                        judge = False
                        break
    elif choose == "3":
        print("{}迅雷不及掩耳之势神扭头，拍屁股撒腿就跑~".format(player))
        game_over2 = input("游戏结束，请输入任意键退出")
        if game_over2 == "Y":
            break
        else:
            break
    elif choose != "1" or choose != "2" or choose != "3":
        print("输入错误，请重新输入！")
    if judge == False:
        break
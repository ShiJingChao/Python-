# 1.
# 请解释以下概念：
# 类：对同一类事物抽象的描述, 抽象的概念
# 对象(实例)：真实存在的, 类的具体的一个实例;
# 对象: 也叫做实例;
#
# 2.
# 银行卡作为类，
# 属性：账户名，余额
# 方法：存款，取款，转账(转账就是给其他银行卡转账)

# class BankCard:
#     def __init__(self,user_name,free_money):
#         self.user_name = user_name
#         self.free_money = free_money
#     def add_money(self,money):
#         self.free_money += money
#         print("存了%.2f元，现在银行卡一共%.2f元" % (money,self.free_money))
#     def use_money(self,u_money):
#         if self.free_money > u_money:
#             self.free_money -= u_money
#             print("您取了%.2f元，银行卡剩余%.2f元" % (u_money,self.free_money))
#         else:
#             print("余额不足")
#     def to_other_money(self,other,bank_obj):
#         if self.free_money > other:
#             self.free_money -= other
#             bank_obj.free_money += other
#             print("您给%s转了%.2f元，银行卡剩余%.2f元" % (bank_obj.user_name,other, self.free_money))
#         else:
#             print("余额不足")
#
#
# c = BankCard("小晓",3000)
# c1 = BankCard("小小",2000)
# c.add_money(500)
# c.use_money(200)
# c.to_other_money(1000,c1)
# 3.
# 手机作为类：
# 属性：品牌，型号
# 方法：show_info()
# 显示自己的属性信息，打电话()

# class Phone:
#     def __init__(self,brand,version,phone_number):
#         self.brand = brand
#         self.version = version
#         self.phone_number = phone_number
#     def show_info(self):
#         print("用%s品牌%s型号的手机打电话" % (self.brand,self.version))
#     def call_phone(self,mobile_obj):
#         print("呼叫方为：%s"% self.phone_number)
#         print("被呼叫方：%s"% mobile_obj.phone_number)
#         print("wuwuwu~")
# call = Phone("华为","P30pro","13231456797")
# call1 = Phone("荣耀","v20","13180302561")
# call.show_info()
# call1.show_info()
# call.call_phone(call1)
# 4.
# 创建学生类：
# 属性：姓名，年龄，学校名
# 方法：吃饭，学习

# class Student:
#     def __init__(self,name,age,school_name):
#         self.name = name
#         self.age = age
#         self.school_name = school_name
#         print(self.name,self.age,self.school_name)
#     def eat(self):
#         print("大吃特吃....")
#     def learn(self):
#         print("学无止境....")
#
# stu = Student("小小","18","清华大学")
# stu.eat()
# stu.learn()


# 1.
# 员工和部门练习题
# A：员工类：(Employee)
# 属性：
# 员工姓名(name)
# 所在的部门名字(department_name), 字符串即可
# 入职时间(hiredate)，例如"2017年11月"
# B：公司类：(Company)
# 属性：
# 公司名称(com_name)
# 部门(department_dict),（类型是一个字典dict，key是部门的名字，value是员工列表，列表中是每个员工对象）
# 方法：
# 添加员工(add_emp)
# 要求：首先员工姓名和入职时间不能同时重复。 如果添加的员工所在部门不存在，你需要帮他创建该部门，
# 并且把他加入到该部门中，如果存在直接加入该部门即可。
#
# 显示所有员工信息的方法(show_company)
# 要求输出格式：
# xxx部门：
# 姓名：小花花
# 入职时间：2017年9月
# 姓名：小二黑
# 入职时间：2014年3月
#
# xxx部门：
# 姓名：王二狗
# 入职时间：2016年10月
#
# 部门：字典
# {}
# 无序的键值对组合
# key：部门的名称
# value：该部门的员工的列表
#
# 人事部：[emp1, emp2, emp3....]
# 技术部：[emp4, emp5]
# 后勤部：[emp6, emp7, emp8...]
employee_all_list = []  # 所有员工
department_dict = {}  # 所有部门员工信息
class Employee:  # 员工类
    def __init__(self, name, department_name, hiredate):
        self.name = name  # 员工姓名
        self.department_name = department_name  # 部门名字
        self.hiredate = hiredate  # 入职时间



class Company:  # 公司类
    com_name = "华为"
    def add_emp(self,name,department_name,hiredate):  # 添加员工

        if name in employee_all_list and employee_all_list[employee_all_list.index(name) + 1] == hiredate:
            print("已经有一个员工和即将入职员工重名且入职时间相同")
        else:
            employee_all_list.append(name)  # 员工列表增加员工
            employee_all_list.append(hiredate)  # 员工列表增加员工入职时间
            department_dict.setdefault(department_name, []).append(name)    # 对应部门字典增加员工姓名
            department_dict.setdefault(department_name, []).append(hiredate) # 对应部门字典增加员工入职时间
            print("添加成功!")

    def show_company(self):  # 显示所有员工信息
        print("%s公司所有员工信息如下：" % self.com_name)
        for k, v in department_dict.items():    # 遍历员工字典
            print(k,":")
            for i in range(0,len(v)):   # 遍历部门列表
                if i % 2 == 0:
                    print("姓名：", v[i])
                else:
                    print("入职时间：", v[i])



def main():
    while True:
        print("=" * 30, "\n欢迎来到员工录入系统\n", "1.添加员工\n2.显示所有员工\n3.退出系统")
        choose = input()
        if choose == "1":
            in_name = input("请输入员工姓名：")
            in_dep = input("请输入员工部门名称:")
            in_hir = input("请输入员工入职时间：")
            Employee(in_name, in_dep, in_hir)   # 调用员工类
            Company().add_emp(in_name,in_dep,in_hir)    # 调用公司类

        elif choose == "2":
            Company().show_company()
        elif choose == "3":
            exit()
        else:
            print("输入错误！")

if __name__ == "__main__":
    main()

# class Raw_materials_prince:
#     def __init__(self,a_p,b_p,c_p): # A、B、C单价
#         self.a_p =a_p
#         self.b_p = b_p
#         self.c_p = c_p
#     def num(self,count):    # 给出生产个数得出原材料总成本
#         res = self.
#
#
#     def one_cost(self):    # 生产一个的成本钱
#         cost1 = self.a_p/100*50+self.b_p/100*100+self.c_p/100*30
#         print("生产一个的成本钱：%.2f" % cost1)
#     def one_mater(self,n,a_p, b_p, c_p): # 给出生产个数得出每种材料的使用量及成本
#         Raw_materials_prince(a_p, b_p, c_p)
#         print("制作{}个，需要A材料{}克，需要{}钱，B材料{}克，需要{}钱，C材料{}克，需要{}钱".format(n,50*n,50*n/100*a_p,100*n,100*n/100*b_p,30*n,30*n/100*c_p))
# class Materials:    # 生产一个需要的材料
#     resin = 50
#     rolled_steel = 100
#     rubber = 30
#     def one_cost(self,a_p,b_p,c_p):    # 生产一个的成本钱
#         Raw_materials_prince(a_p,b_p,c_p)
#         cost1 = a_p/100*50+b_p/100*100+c_p/100*30
#         return cost1
#     def num(self,n,re,ro,ru):    # 给出生产个数得出原材料总成本
#         m = self.one_cost(re,ro,ru)
#         all_cost = n*m.cost1
#         return all_cost
#
#
#
# r = Raw_materials_prince(50,30,100)
# m = Materials()
# m.one_cost(50,30,100)
# m.num(10)

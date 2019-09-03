"""
    员工VS公司
"""


class Employee:
    def __init__(self, name, d_name, h_date):
        self.name = name
        self.department_name = d_name
        self.hire_date = h_date


class Company:
    def __init__(self, name):
        self.name = name
        self.department_dict = {}  # 装着所有员工信息

    def add_emp(self, emp):  # emp:需要添加的员工对象
        # 1. 姓名和入职时间是否同时重复
        for v in self.department_dict.values():  # 遍历字典,获取每个部门的员工列表
            for old_emp in v:  # 遍历员工列表, 获取每个已存在的员工对象
                if old_emp.name == emp.name and old_emp.hire_date == emp.hire_date:
                    print("该员工已存在, 不能重复添加.")
                    return  # 1.结束函数的执行 2.把函数执行的结果返回给调用处;

        # 2. 部门存在, 直接添加; 部门不存在,创建部门,再添加员工
        if emp.department_name in self.department_dict.keys():
            # 部门存在  员工列表 = self.department_dict["技术部"]
            self.department_dict[emp.department_name].append(emp)  # 将当前员工追加到部门列表中
            print("该部门已存在, 员工添加成功")
        else:
            self.department_dict[emp.department_name] = [emp, ]
            print("该部门已创建, 员工添加成功")

    def show_department(self):
        for k, v in self.department_dict.items():
            print("{}:".format(k))
            for emp in v:  # 遍历字典的value(也就是员工列表), 依次获取每一个员工对象
                print("\t姓名: {}".format(emp.name))
                print("\t入职时间: {}".format(emp.hire_date))


"""
员工列表 = self.department_dict[emp.department_name]
{
    "技术部" : [emp1, emp2, emp3, ...],  # 部门列表中的元素, 为员工类的对象;
    "行政部" : [emp1],
}
"""
e1 = Employee("李小花", "宣传部", "2019-07")
c = Company("巨无霸")
c.add_emp(e1)

e2 = Employee("小二黑", "技术部", "2019-07")
c.add_emp(e2)

e3 = Employee("李小花", "行政部", "2019-07")
c.add_emp(e3)

e4 = Employee("刘三胖", "技术部", "2018-04")
c.add_emp(e4)

e5 = Employee("刘三胖", "技术部", "2019-08")
c.add_emp(e5)

c.show_department()


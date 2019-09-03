
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
# class Employee:
#     def __init__(self,name,department_name,hiredate):
#         pass
# class Company:
#     com_name = "华为"
#
#     def __init__(self):

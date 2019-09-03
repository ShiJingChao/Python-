import pymysql

class MyDB:
    def __init__(self,h='localhost',u='root',p=None,db=None):
        # 连接数据库 创建游标对象
        # host 主机的ip地址
        # user 数据库的用户名
        # password 数据库的密码
        # database 指定要操作的数据库
        # cursorclass 指定返回的数据格式 默认返回元组
        self.db = pymysql.connect(host=h,user=u,
                                  password=p,database=db,
                                  cursorclass = pymysql.cursors.DictCursor
                                  )
        # 创建游标 所有的操作都要通过此对象
        self.cursor = self.db.cursor()

    # 做查询
    def query(self,sql):
        # 调用游标对象中的 execute 执行sql语句
        self.cursor.execute(sql)
        # 将查询到的数据进行返回
        return self.cursor.fetchall()
    # 做添加 删除 修改
    def change(self,sql):
        self.cursor.execute(sql)
        # 如果对数据的数据做修改 必须commit
        self.db.commit()
        # 返回数据操作影响的行
        return self.cursor.rowcount

    # 析构函数
    def __del__(self):
        # 关闭数据库连接
        self.cursor.close()
        self.db.close()


if __name__ == '__main__': # 主程序的入口 一般用于测试
    #  实例化对象
    database = MyDB(p='123123',db='demo1')
    res = database.query('select * from user')
    print(res)
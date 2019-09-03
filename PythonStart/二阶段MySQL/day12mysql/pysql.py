# 导包
import pymysql

# 1.连接数据库
db = pymysql.connect(host='localhost', user='root', password="123123",database='demo1',
                     cursorclass=pymysql.cursors.DictCursor)
# 2.创建游标对象
cursor = db.cursor()
# 3.定义sql语句
# sql = 'select version()'
# 定义查询的sql语句
sql = 'select * from user'
# 定义添加数据数据
# sql = 'insert into user(id,name) values(25,"明明")'
# 定义更新数据
# sql = 'update user set age=16 where name="明明"'
# 删除数据
# sql = "delete from user where name='靠脸'"
# 4.执行sql语句
cursor.execute(sql)
# 获取返回的结构
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchall())
print(cursor.rowcount)
# 如果操作对数据库中的数据产生了影响必须执行提交
db.commit()
# 5.断开连接
cursor.close()
db.close()
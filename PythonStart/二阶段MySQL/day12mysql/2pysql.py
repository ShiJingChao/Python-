from mydb import  MyDB

# 实例化数据库对象
database = MyDB(h='localhost',u='root',p='123123',db='demo1')


# 插入数据
sql = 'insert into user(id,name) values(30,"祎")'
print(database.change(sql))

# 定义sql语句
sql = 'select * from user'
print(database.query(sql))

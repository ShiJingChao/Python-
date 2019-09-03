#!/usr/bin/env pytho

# -*- coding:utf-8 -*-

import pymysql

# 创建连接

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='000000',
    db='db1',
    charset='utf8')

# 创建游标

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行SQL，并返回收影响行数
# sql = 'CREATE TABLE TEST(id int ,name varchar(20))'

# ret = cursor.execute("INSERT INTO test VALUE (1,'alex'),(2,'alvin')")
# print(ret)
resurt = cursor.execute("SELECT * FROM test")
print(resurt)
print(cursor.fetchone())
cursor.scroll(-1,mode="relative")
print(cursor.fetchone())
# print(cursor.fetchall())
# result = cursor.fetchall()
# print(result)
# 执行SQL，并返回受影响行数

# effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))


# 执行SQL，并返回受影响行数,执行多次

# effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])


# 提交，不然无法保存新建或者修改的数据

conn.commit()

# 关闭游标

cursor.close()

# 关闭连接

conn.close()
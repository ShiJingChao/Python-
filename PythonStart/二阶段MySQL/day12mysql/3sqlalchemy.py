import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
# 类似于 pymysql中的游标
from sqlalchemy.orm import sessionmaker


# 1.创建连接
# 数据库类型+数据库操作的包:// 用户名:密码@主机地址/你要操作的数据库
# mysql://scott:tiger@hostname/dbname
db = sqlalchemy.create_engine('mysql://root:123123@localhost/sqlorm')

# 2.创建基类
base = declarative_base(db)

# 3.创建类 必须继承基类  创建模型
class User(base):
    # 表名
    __tablename__='user'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32)) # varchar()
    age = sqlalchemy.Column(sqlalchemy.Integer)

class Userinfo(base):
    __tablename__='userinfo'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    phone = sqlalchemy.Column(sqlalchemy.String(20))

class Shop(base):
    __tablename__='shop'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))




if __name__ == '__main__':
    # 执行数据库迁移 创建表
    base.metadata.create_all(db)
    # 绑定一个实例
    s = sessionmaker(bind=db)
    # 创建回话对象  类似于游标
    session = s()

    # 添加
    # user = User(name='hello',age=16)
    # session.add(user)
    # session.commit()
    # session.add_all([
    #     User(name='world',age=1),
    #     User(name='python',age=28),
    #     User(name='PHP', age=30),
    # ])
    # session.commit()
    # 查询
    # 查询所有的数据 返回一个列表
    # res = session.query(User).all()
    # for i in res:
    #     print(i.name,i.age)
    # 通过主键查询一条数据 返回一个对象
    # res = session.query(User).get(1)
    # print(res.name,res.age)
    # 条件查询 返回的是一个列表
    # res = session.query(User).filter_by(name='hello').all()
    # print(res)
    # res = session.query(User).filter(User.name=='hello').all()
    # print(res)
    # 修改数据
    # res = session.query(User).get(1)
    # print(res.name)
    # res.name='HELLO'
    # session.commit()
    # 删除数据
    res = session.query(User).get(1)
    session.delete(res)
    session.commit()



import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy import Column,Integer,String,text

from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:mysql@localhost/cq",
                       encoding="utf-8")
# engine = create_engine("mysql+pymysql://root:mysql@localhost/cq",
#                        encoding="utf-8",echo=True)

Base = declarative_base()

class Roommate(Base):
    __tablename__ = "Roommate"
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(32))
    def __repr__(self):
        return "<%s name:%s password:%s>" % (self.id,self.name,self.password)
Base.metadata.create_all(engine)

session_class = sessionmaker(bind=engine)
session = session_class()

# user1 = Roommate(name="alex",password="123")
# user2 = Roommate(name="jack",password="122")

# session.add(user1)  以对象的形式传参数，添加新的元组
# session.add(user2)
# session.add_all([     添加多条元组
#     Users(name="alex1", extra='sb'),
#     Users(name="alex2", extra='sb'),
# ])
data  = session.query(Roommate).filter(Roommate.id>0).filter(Roommate.id<3).first()
print(data)
data.name = "bob"#可以直接对数据对象进行修改，最后在commit一下修改数据库
#  data = session.query(Users).filter(Users.name.like('e%')).all()    模糊查询

# data = session.query(Users).order_by(Users.name.desc()).all()       结果排序

#data = session.query(Roommate,user).filter(Roommate.name==user.name).all()  连接表

# data = session.query(Roommate).join(user).all  有外键关联时才可以用join连接

# data = session.query(Roommate).join(user,isouter=True).all

# session.query(Roommate).filter(Roommate.id > 2).update({"name" : "099"})   对查询到的数据直接修改

# session.query(Roommate).filter(Roommate.id > 2).update({Roommate.name: Roommate.name + "099"}, synchronize_session=False)  不论删除对象是否一直存在，都会执行删除。

# session.query(Roommate).filter(Roommate.id > 2).update({"num": Roommate.num + 1}, synchronize_session="evaluate")  删除对象不存在与session中的，会报错

# session.query(Roommate).filter(Roommate.id > 2).delete()  对查询到的数据进行删除操作

# ret = session.query(Roommate).group_by(Roommate.extra).all()  分组查询
# ret = session.query(                                           函数
#     func.max(Roommate.id),
#     func.sum(Roommate.id),
#     func.min(Roommate.id)).group_by(Roommate.name).all()

# q1 = session.query(Users.name).filter(Users.id > 2)              组合查询
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union_all(q2).all()

# ret = session.query(Roommate).filter(text("id<:value and name=:name")).params(value=224, name='fred').order_by(Roommate.id).all()  参数条件指定

# ret = session.query(Roommate).from_statement(text("SELECT * FROM users where name=:name")).params(name='ed').all()   使用原生SQL语句

session.commit()

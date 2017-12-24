import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:mysql@localhost/cq"
                       ,encoding='utf-8')#,echo=True)
Base = declarative_base()
class User(Base):
    __tablename__= 'user_info'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user = Column(String(20))
    passwd = Column(String(30))
    def __repr__(self):
        return "<User(name='%s',  password='%s')>" % (
            self.user, self.passwd)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
Session = Session_class()
# usr_obj = User(user="aa",passwd="123")
# usr_obj2 = User(user="bb",passwd="250")
#
# Session.add(usr_obj)
# Session.add(usr_obj2)
from sqlalchemy import func
print(Session.query(User).filter(User.id>3).all())
print(Session.query(User).filter_by(id=3).all())
print(Session.query(User).filter(User.id>1).filter(User.id<4).all())
print(Session.query(User.user,func.count(User.user)).group_by(User.user).all())
Session.commit()

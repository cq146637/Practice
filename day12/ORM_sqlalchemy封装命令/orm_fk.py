import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine("mysql+pymysql://root:mysql@localhost/cq"
                       ,encoding='utf-8')#,echo=True)
Base = declarative_base()

Session_class = sessionmaker(bind=engine)
Session = Session_class()
class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(32), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", backref="addresses")  # 这个nb，允许你在user表里通过backref字段反向查出所有它在addresses表里的关联项

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

Base.metadata.create_all(engine)
obj = Session.query(User).first()
for i in obj.addresses:  # 通过user对象反查关联的addresses记录
    print(i)
addr_obj = Session.query(Address).first()
print(addr_obj.user.name)  # 在addr_obj里直接查关联的user表

obj = Session.query(User).filter(User.name == 'rain').all()[0]
print(obj.addresses)

obj.addresses = [Address(email_address="r1@126.com"),  # 添加关联对象
                 Address(email_address="r2@126.com")]

Session.commit()




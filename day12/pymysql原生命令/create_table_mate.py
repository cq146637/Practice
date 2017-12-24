from sqlalchemy import Column,Integer,String,Table,MetaData

from sqlalchemy.orm import mapper

metadata = MetaData()

user = Table(
    "user_center",metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(32)),
    Column("fullname",String(48)),
    Column("password",String(20)),
)

class User(object):
    def __init__(self,name,fullname,password):
        self.name = name
        self.fullname = fullname
        self.password = password

mapper(User,user)
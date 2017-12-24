from sqlalchemy import Integer, ForeignKey, String, Column,DATE,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

zhongjian = Table("zhongjian",Base.metadata,
            Column("book_id",Integer,ForeignKey("books.id")),
            Column("author_id",Integer,ForeignKey("authors.id"))
            )

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False)
    public_date = Column(DATE)
    authors = relationship('Author',secondary=zhongjian,backref="books.id")
class Author(Base):
    __tablename__='authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
engine = create_engine("mysql+pymysql://root:mysql@localhost/cq"
                       ,encoding='utf-8')#,echo=True)
Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
Session = Session_class()

# b1
# b2
# b3
#
# a1
# a2
# a3
#
# b1.author[a1,a2,a3]
# b2.author[a1,a3]
#
#
# Session.add_all([b1,b2,b3,a1,a2,a3])
# Session.commit()
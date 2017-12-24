from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:mysql@localhost/cq?charset=utf8",
                       encoding="utf-8")#支持中文写入数据库

Base = declarative_base()

book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books')

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name


Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
s = Session_class()  # 生成session实例

b1 = Book(name="跟Alex学Python")
b2 = Book(name="跟Alex学把妹")
b3 = Book(name="跟Alex学装逼")
b4 = Book(name="跟Alex学开车")

a1 = Author(name="Alex")
a2 = Author(name="Jack")
a3 = Author(name="Rain")

b1.authors = [a1, a2]
b2.authors = [a1, a2, a3]

s.add_all([b1, b2, b3, b4, a1, a2, a3])

s.commit()

print('--------通过书表查关联的作者---------')

book_obj = s.query(Book).filter_by(name="跟Alex学Python").first()
print(book_obj.name, book_obj.authors)

print('--------通过作者表查关联的书---------')
author_obj = s.query(Author).filter_by(name="Alex").first()
print(author_obj.name, author_obj.books)
s.commit()

author_obj = s.query(Author).filter_by(name="Jack").first()

book_obj = s.query(Book).filter_by(name="跟Alex学把妹").first()

book_obj.authors.remove(author_obj)  # 从一本书里删除一个作者
s.commit()


author_obj =s.query(Author).filter_by(name="Alex").first()
# print(author_obj.name , author_obj.books)
s.delete(author_obj)
s.commit()
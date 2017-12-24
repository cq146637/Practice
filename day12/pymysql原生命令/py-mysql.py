import pymysql

conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="mysql",db="cq",charset="utf8")

# cursor = conn.cursor()

# effect_row = cursor.execute("insert into user(name,age,register_date) values('cc',19,'2017-05-07')")
# effect_row = cursor.execute("select * from user")

# print(effect_row)
print(cursor.fetchone())
for i in cursor.fetchall():
    print(i)

conn.commit()
cursor.close()
conn.close()
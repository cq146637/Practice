import pymysql

conn = pymysql.connect(host="localhost",port=3306,user="cq",passwd="mysql",db="cq",charset='utf8')

cursor = conn.cursor()

insert_info = [
    ("1507084141","陈乾",20,"男","学生"),
    ("1507084142","陈乾1",21,"男","学生"),
    ("1507084143","陈乾2",22,"男","学生"),
    ("1507084144","陈乾3",23,"男","学生"),
]

effect_rows = cursor.execute("select * from student")

for i in cursor.fetchall():
    print(i)
conn.commit()
cursor.close()
conn.close()
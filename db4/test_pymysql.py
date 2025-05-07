import pymysql

# 데이터베이스 연결 설정
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='testdatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

sql = "SELECT * FROM uusers"
cursor.execute(sql)

users = cursor.fetchall()
print(users)

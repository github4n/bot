import sqlite3
from webLogin import webLogin

email = '549705907@qq.com'
passwd = 'DAda549705907'
refreshToken = webLogin(email,passwd)
print(refreshToken)
conn = sqlite3.connect("user.db")
cursor = conn.cursor()
sql = "INSERT INTO user (email, passwd, refreshToken) VALUES ('%s','%s','%s');" % (email,passwd,refreshToken)
print(sql)
cursor.execute(sql)
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()


import sqlite3
conn = sqlite3.connect("user.db")
cursor = conn.cursor()
sql = "SELECT * FROM user;"
cursor.execute(sql)
result = cursor.fetchall()
print(result)

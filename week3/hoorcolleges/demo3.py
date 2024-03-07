import sqlite3

conn = sqlite3.connect('C:\\Users\\rote\\Programmeren\\webtech\\hc-week3\\test.sqlite')
cursor = conn.cursor()
cursor.execute('select * from users;')

row = cursor.fetchone()
print(row)

for row in cursor.fetchmany(3):
    print(row)
    
for row in cursor.fetchall():
    print(row)
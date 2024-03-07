import sqlite3

search_name = input('Geef een naam om op te zoeken: ')

db = sqlite3.connect("rekeningen.sqlite") # C:\\Users\\rote\\Programmeren\\webtech\\ch3-sql\\
cursor = db.cursor()
sql = 'SELECT * FROM rekeningen WHERE naam LIKE ?'
t_params = ('%' + search_name + '%',)
rows = cursor.execute(sql, t_params)

print('Ik heb de volgende contacten gevonden:')
for row in rows:
    print(row)

cursor.close()
db.close()
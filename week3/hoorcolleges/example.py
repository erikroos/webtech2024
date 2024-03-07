import sqlite3

db = sqlite3.connect("music.sqlite") # C:\\Users\\rote\\Programmeren\\webtech\\ch3-sql\\
cursor = db.cursor()

resultset = cursor.execute('SELECT * FROM albums JOIN artists ON albums.artist = artists._id WHERE artists.name = "Pink Floyd"')
print("Row for row:")
for row in resultset:
    print(row)

# Opnieuw resultset ophalen want pointer staat aan het einde en resetten kan niet
resultset = cursor.execute('SELECT * FROM albums JOIN artists ON albums.artist = artists._id WHERE artists.name = "Pink Floyd"')
print("Row for row using fetchone:")
while row := resultset.fetchone():
    print(row)

# Opnieuw resultset ophalen want pointer staat aan het einde en resetten kan niet
resultset = cursor.execute('SELECT * FROM albums JOIN artists ON albums.artist = artists._id WHERE artists.name = "Pink Floyd"')
print("Using fetchall:")
all_rows = resultset.fetchall()
print(all_rows)
#print(f"Aantal volgens rowcount: {cursor.rowcount}")
#print(f"Aantal volgens lengte van resultset: {len(all_rows)}")

cursor.close()
db.close()
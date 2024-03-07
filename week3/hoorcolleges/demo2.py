class Database:
    import sqlite3
    
    def save(table, *data):
        q_marks = '?,'*len(data)
        q_marks = f'({q_marks[:-1]})'
        sql = f'insert into {table} values {q_marks}'
        conn = Database.sqlite3.connect('demo.sqlite')
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        id = cursor.lastrowid
        return str(id)
    
    def better_save(table, **data):
        fields = tuple([k for k in data.keys()])
        values = tuple([v for v in data.values()])
        q_marks = '?,' * len(data)
        q_marks = f'({q_marks[:-1]})'
        sql = f'insert into {table} {fields} values {q_marks}'
        conn = Database.sqlite3.connect('demo.sqlite')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        id = cursor.lastrowid
        return str(id)


class User:
    table = 'users'

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def save(self):
        return Database.save(User.table, self.name, self.password)

    def better_save(self):
        return Database.better_save(User.table, username = self.name, password = self.password)
        

erik = User('Erik', 'supergeheim')
bart = User('Bart', 'veelbeterwachtwoord')

print(erik.better_save())
print(bart.better_save())

import sqlite3

def save_data(data):
    conn = sqlite3.connect("C:\\Users\\rote\\Programmeren\\webtech\\hc-week3\\test.sqlite")
    cursor = conn.cursor()
    u_name = data["naam"]
    u_pass = data["wachtwoord"]
    sql = f"INSERT INTO users (username, password) VALUES ('{u_name}', '{u_pass}');"
    print(sql)
    cursor.executescript(sql)
    conn.commit()
    id = cursor.lastrowid
    return str(id)

def save_data_better(data):
    conn = sqlite3.connect("C:\\Users\\rote\\Programmeren\\webtech\\hc-week3\\test.sqlite")
    cursor = conn.cursor()
    u_name = data["naam"]
    u_pass = data["wachtwoord"]
    sql = f"INSERT INTO users (username, password) VALUES ('{u_name}', '{u_pass}');"
    print(sql)
    cursor.execute(sql)
    conn.commit()
    id = cursor.lastrowid
    return str(id)

def save_data_best(data):
    conn = sqlite3.connect("C:\\Users\\rote\\Programmeren\\webtech\\hc-week3\\test.sqlite")
    cursor = conn.cursor()
    u_name = data["naam"]
    u_pass = data["wachtwoord"]
    u_tuple = (u_name, u_pass)
    sql = "INSERT INTO users (username, password) VALUES (?, ?);"
    print(sql)
    cursor.execute(sql, u_tuple)
    conn.commit()
    id = cursor.lastrowid
    return str(id)

#data = {"naam": "bart", "wachtwoord": "geheimst"}
#data = {"naam": "erik", "wachtwoord": "geheim'); DROP TABLE important_data; --"}
result = save_data_best(data)
print(result)
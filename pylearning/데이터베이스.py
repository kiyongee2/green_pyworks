import sqlite3

def select():
    conn = sqlite3.connect("d:/dbworks/pydb/mydb.db")
    cur = conn.cursor()
    sql = "SELECT * FROM test"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()

select()
import sqlite3
"""
def select():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    sql = "SELECT * FROM employee"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()

def insert():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    sql = "INSERT INTO employee VALUES ('e104', '이강인', 22, 15000)"
    cur.execute(sql)
    conn.commit()
    conn.close()

def select_one():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    sql = "SELECT * FROM employee WHERE empid='e102'"
    cur.execute(sql)
    rs = cur.fetchone()
    print(rs)
    conn.close()

"""
def getconn():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    return conn

def select():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM employee"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()

select()



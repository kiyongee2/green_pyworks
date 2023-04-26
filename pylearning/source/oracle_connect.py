
import cx_Oracle

def getconn():
    conn = cx_Oracle.connect('system', '12345', 'localhost:1521/xe')
    return conn

def select():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM pytest"
    cursor.execute(sql)
    rs = cursor.fetchall()
    for i in rs:
        print(i)
    conn.close()

def insert():
    conn = getconn()
    cursor = conn.cursor()
    sql = "INSERT INTO pytest VALUES ('행운이 함께 하길 빌어요..')"
    cursor.execute(sql)
    conn.commit()
    conn.close()

# insert()
select()

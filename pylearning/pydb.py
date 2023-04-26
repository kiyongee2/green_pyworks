
import sqlite3

def getconn():
    conn = sqlite3.connect("./output/bookdb.db")
    return conn

def create():
    conn = getconn()
    cursor = conn.cursor()
    sql = """
        CREATE TABLE book(
            book_no INTEGER PRIMARY KEY AUTOINCREMENT,
            title   TEXT NOT NULL,
            author TEXT NOT NULL,
            page INTEGER
        )
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()

def insert():
    conn = getconn()
    cursor = conn.cursor()
    sql = "INSERT INTO book(title, author, page) VALUES (?, ?, ?)"
    # cursor.execute(sql, ('반응형 웹페이지', '김운아', 300))
    cursor.execute(sql, ('혼자 공부하는 자바', '신용권', 650))
    conn.commit()
    conn.close()

def select():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    rs = cursor.fetchall()
    for i in rs:
        print(i)
    conn.close()

def select_one():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM book WHERE book_no = ?"
    cursor.execute(sql, (2, )) # 튜플은 1개일때 쉼표 붙임
    rs = cursor.fetchone()
    print(rs)
    conn.commit()
    conn.close()

def update():
    conn = getconn()
    cursor = conn.cursor()
    sql = "UPDATE book SET page = ? WHERE book_no = ? "
    # 1번 책의 페이지수를 350으로 변경함
    cursor.execute(sql, (350, 1))
    conn.commit()
    conn.close()

def delete():
    conn = getconn()
    cursor = conn.cursor()
    # 2번 책을 삭제함
    sql = "DELETE FROM book WHERE book_no = ? "
    cursor.execute(sql, (2, ))
    conn.commit()
    conn.close()

# create()
#insert()
#select_one()
#update()
delete()
select()

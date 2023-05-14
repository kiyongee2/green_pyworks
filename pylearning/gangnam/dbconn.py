# db 연동
import sqlite3

def getconn():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    return conn

def create_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = """
        CREATE TABLE board(
            bno     INTEGER PRIMARY KEY AUTOINCREMENT,
            title   TEXT NOT NULL,
            content TEXT NOT NULL,
            createdate DATETIME DEFAULT (datetime ('now', 'localtime')),
            modifydate DATETIME,
            hit INTEGER DEFAULT 0,
            memberid TEXT NOT NULL,
            FOREIGN KEY(memberid) REFERENCES member(memberid) ON DELETE CASCADE
        )
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()

def drop_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = "DROP TABLE board"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def insert_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = "INSERT INTO board(title, content, memberid) VALUES (?, ?, ?)"
    cursor.execute(sql, ('가입인사', '안녕하세요~ 가입 합니다.', 'test'))
    conn.commit()
    conn.close()

def select_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM board ORDER BY createdate DESC"
    cursor.execute(sql)
    boardlist = cursor.fetchall()
    for board in boardlist:
        print(board)
    conn.close()

def select_one_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM board WHERE bno = ?"
    cursor.execute(sql, (1, ))
    board = cursor.fetchone()
    print(board)
    conn.close()

def board_delete():
    conn = getconn()
    cursor = conn.cursor()
    sql = "DELETE FROM board WHERE bno = ?"
    cursor.execute(sql, (2, ))
    conn.commit()
    conn.close()

def board_update():
    conn = getconn()
    cursor = conn.cursor()
    sql = "UPDATE board SET title = ?, content = ? WHERE bno = ?"
    cursor.execute(sql, ('공지', '공지사항', 6))
    conn.commit()
    conn.close()

create_board()
# drop_board()
# insert_board()
# board_delete()
# board_update()
# select_board()
# select_one_board()
from flask import Flask, render_template, request, \
    redirect, url_for, session
import sqlite3

app = Flask(__name__)

# 로그인시 암호키 설정
app.secret_key = "asdfqwer1234"

# db 객체 생성
def getconn():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    return conn

# 메인 페이지
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

# 회원 가입
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        # 데이터 수집
        id = request.form['memberid']
        pw = request.form['passwd1']
        name = request.form['name']
        gender = request.form['gender']
        # DB에 저장
        conn = getconn()
        cur = conn.cursor()
        sql = f"INSERT INTO member(memberid, passwd, name, gender) " \
              f"VALUES ('{id}', '{pw}', '{name}', '{gender}')"
        # 자동 로그인(세션 발급)
        session['userid'] = request.form['memberid']
        cur.execute(sql)
        conn.commit()
        conn.close()
        return redirect(url_for('memberlist')) # url 경로임 - memberlist
    else:
        return render_template('register.html')

# 회원 목록
@app.route('/memberlist', methods = ['GET'])
def memberlist():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member ORDER BY regdate DESC"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()
    return render_template('memberlist.html', rs=rs)

# 로그인
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        # 데이터 넘겨 받기
        id = request.form['memberid']
        pw = request.form['passwd']
        conn = getconn()
        cursor = conn.cursor()
        sql = f"SELECT * FROM member " \
              f"WHERE memberid='{id}' AND passwd='{pw}'"
        cursor.execute(sql)
        rs = cursor.fetchone()
        print(rs)
        conn.close()

        if rs:
            session['userid'] = rs[0]   # memberid에 세션 발급
            return redirect(url_for('index'))
        else:
            error_message = "아이디나 비밀번호를 확인해주세요"
            return render_template('login.html', error_msg = error_message)
    else:
        return render_template('login.html')

# 로그 아웃
@app.route('/logout')
def logout():
    session.clear()  #모든 세션 삭제
    return redirect(url_for('index'))

# 게시글 목록
@app.route('/boardlist', methods = ['GET'])
def boardlist():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM board ORDER BY createdate DESC"
    cursor.execute(sql)
    boardlist = cursor.fetchall()
    return render_template('boardlist.html', boardlist = boardlist)

# 게시글 쓰기
@app.route('/writing', methods = ['GET', 'POST'])
def writing():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        memberid = session.get('userid')

        conn = getconn()
        cursor = conn.cursor()
        sql = f"INSERT INTO board(title, content, memberid) VALUES ('{title}', '{content}', '{memberid}')"
        cursor.execute(sql)
        conn.commit()
        conn.close()
        return redirect(url_for('boardlist'))
    else:
        return render_template('writing.html')

# 게시글 상세 보기
@app.route('/detail/<int:bno>', methods = ['GET'])
def detail(bno):
    conn = getconn()
    cursor = conn.cursor()
    sql = f"SELECT * FROM board WHERE bno = {bno}" #숫자 - 따옴표 붙이지 않음
    cursor.execute(sql)
    board = cursor.fetchone()
    conn.close()
    return render_template('detail.html', board=board)

# 게시글 삭제
@app.route('/delete/<int:bno>', methods = ['GET'])
def delete(bno):
    conn = getconn()
    cursor = conn.cursor()
    sql = f"DELETE FROM board WHERE bno = {bno}"
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return redirect(url_for('boardlist'))

# 게시글 수정
@app.route('/update/<int:bno>', methods=['GET', 'POST'])
def update(bno):
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']

        conn = getconn()
        cursor = conn.cursor()
        sql = f"UPDATE board SET title = '{title}', content = '{content}' WHERE bno = {bno}"
        cursor.execute(sql)
        conn.commit()
        conn.close()
        return redirect(url_for('detail', bno=bno))
    else:
        conn = getconn()
        cursor = conn.cursor()
        sql = f"SELECT * FROM board WHERE bno = {bno}"
        cursor.execute(sql)
        board = cursor.fetchone()
        conn.close()
        return render_template('update.html', board=board)

app.run()

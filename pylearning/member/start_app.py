from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def getconn():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        # 데이터 수집
        id = request.form['memberid']
        pwd = request.form['passwd']
        name = request.form['name']
        gender = request.form['gender']

        # DB에 저장
        conn = getconn()
        cur = conn.cursor()
        sql = f"INSERT INTO member VALUES ('{id}', '{pwd}', '{name}', '{gender}')"
        cur.execute(sql)
        conn.commit()
        conn.close()

        return redirect(url_for('memberlist'))
    else:
        return render_template('register.html')

@app.route('/memberlist')
def memberlist():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()
    return render_template('memberlist.html', rs=rs)

app.run()
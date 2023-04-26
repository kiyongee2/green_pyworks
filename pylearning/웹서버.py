# flask 서버
from flask import Flask

app = Flask(__name__)  #app 객체 생성

@app.route('/') #http://127.0.0.1:5000/
def index():
    return "Hello~ Flask"

@app.route('/login') #http://127.0.0.1:5000/login
def login():
    return "<h2><i>로그인</i> 페이지입니다.</h2>"

@app.route('/register')
def register():
    return "<h2>회원가입 페이지입니다.</h2>"

@app.route('/board/view')
def view():
    return "<h2>게시글 상세 페이지입니다.</h2>"


app.run()